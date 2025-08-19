from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import ScrapRejection
from .serializers import ScrapRejectionSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# POST API - Create a new Scrap Rejection (with auto-generated scrap_rejection_no)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ScrapRejection
from .serializers import ScrapRejectionSerializer

class ScrapRejectionCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Extract shortyear (the last 2 digits of the year) from the scrap_rejection_no
        # Assuming the format for scrap_rejection_no is "Line R YYYYxxxxxx"
        scrap_rejection_no = request.data.get("scrap_rejection_no", "")
        if not scrap_rejection_no.startswith("Line R"):
            return Response({"error": "Invalid scrap_rejection_no format."}, status=status.HTTP_400_BAD_REQUEST)

        shortyear = scrap_rejection_no.split(' ')[1][:2]  # Get the last 2 digits of the year
        
        if not shortyear:
            return Response({"error": "Invalid scrap_rejection_no format."}, status=status.HTTP_400_BAD_REQUEST)

        # Generate the next scrap rejection number
        next_scrap_rejection_no = ScrapRejection.generate_next_scrap_rejection_no(shortyear)

        # Add the generated number to the request data
        request.data["scrap_rejection_no"] = next_scrap_rejection_no
        
        # Proceed with creating the ScrapRejection
        serializer = ScrapRejectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET API - List Scrap Rejections
class ScrapRejectionListAPIView(ListCreateAPIView):
    queryset = ScrapRejection.objects.all()
    serializer_class = ScrapRejectionSerializer

# GET API - Retrieve Single Scrap Rejection by ID
class ScrapRejectionDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ScrapRejection.objects.all()
    serializer_class = ScrapRejectionSerializer

# GET API - Retrieve next scrap rejection number based on Shortyear
class NextScrapRejectionAPIView(APIView):
    def get(self, request, *args, **kwargs):
        shortyear = request.query_params.get('Shortyear')
        if not shortyear:
            raise NotFound("Shortyear parameter is missing.")
        
        try:
            next_scrap_rejection_no = ScrapRejection.generate_next_scrap_rejection_no(shortyear)
            return Response({"next_scrap_rejection_no": next_scrap_rejection_no})
        except ScrapRejection.DoesNotExist:
            return Response({"next_scrap_rejection_no": None}, status=status.HTTP_404_NOT_FOUND)


# Production Entry
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import ProductionEntry,MachineIdleTime
from .serializers import ProductionEntrySerializer, OOPurchaseSerializer

class ProductionEntryViewSet(viewsets.ModelViewSet):
    queryset = ProductionEntry.objects.all()
    serializer_class = ProductionEntrySerializer

    @action(detail=False, methods=['get'])
    def get_prod_no(self, request):
        series = request.query_params.get('series', None)
        year = request.query_params.get('year', None)
        
        if not series or not year:
            return Response({"error": "Series and Year are required"}, status=400)
        
        try:
            prod_no = ProductionEntry.generate_prod_no(series, int(year))
            return Response({"prod_no": prod_no})
        except ValueError as e:
            return Response({"error": str(e)}, status=400)

    def create(self, request, *args, **kwargs):
        # Handling the creation of a new ProductionEntry with nested ItemDetail
        serializer = OOPurchaseSerializer(data=request.data)
        if serializer.is_valid():
            production_entry = serializer.save()  # This automatically saves both ProductionEntry and ItemDetail
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from .models import ProductionEntry

def generate_production_pdf(request, pk):
    entry = get_object_or_404(ProductionEntry, pk=pk)
    idle_times = entry.MachineIdleTime_Detail_Enter.all()

    template = get_template('ProductionEntry.html')  # Ensure this uses only ProductionEntry and MachineIdleTime
    html = template.render({
        'entry': entry,
        'idle_times': idle_times,
    })

    pdf_file = HTML(string=html).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="production_{pk}.pdf"'
    return response


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProductionEntry

class ProductionSummaryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        plant = request.query_params.get('plant')
        prod_no = request.query_params.get('prod_no')

        queryset = ProductionEntry.objects.all()

        if plant:
            queryset = queryset.filter(mill_name__icontains=plant)
        if prod_no:
            queryset = queryset.filter(Prod_no__icontains=prod_no)

        data = []
        for entry in queryset:
            data.append({
                "id": entry.id,
                "mill_name": entry.mill_name,
                "Prod_no": entry.Prod_no,
                "Date": entry.Date,
                "Time": entry.Time,
                "shift": entry.shift,
                "contractor": entry.contractor,
                "operator": entry.operator,
                "item": entry.item,
                "prod_qty": entry.prod_qty,
                "reject_qty": entry.reject_qty,
                "rework_qty": entry.rework_qty,
                "View": f"/Production/ProductionEntry/pdf/{entry.id}/",
                "Edit": f"/Production/api/production-entries/{entry.id}/"
            })

        return Response(data)

    

# Production Entry Shift Time Serailizer :- Fetch   
from rest_framework import generics
from All_Masters.models import Shift_Master_Model
from .serializers import ProductionEntryShift

class ProductionEntryShiftDetail(generics.ListAPIView):
    queryset = Shift_Master_Model.objects.all()
    serializer_class = ProductionEntryShift

    

# Production Entry Contractor:- Fetch
from All_Masters.models import Contractor_Master_Model
from .serializers import ProductionEntryContractor

class ProductionEntryContractorListView(generics.ListAPIView):
    queryset = Contractor_Master_Model.objects.all()
    serializer_class = ProductionEntryContractor


# Production Entry Operator and Supervisor and Helper 
from rest_framework.generics import ListAPIView
from All_Masters.models import Add_New_Operator_Model
from .serializers import ProductionOperatorSupervisor

class ProductionOperatorListView(ListAPIView):
    queryset = Add_New_Operator_Model.objects.filter(Type='operator')
    serializer_class = ProductionOperatorSupervisor
    filter_backends = [SearchFilter]
    search_fields = ['Name','Code']

class ProductionSupervisorListView(ListAPIView):
    queryset = Add_New_Operator_Model.objects.filter(Type='supervisor')
    serializer_class = ProductionOperatorSupervisor
    filter_backends = [SearchFilter]
    search_fields = ['Name','Code']

class ProductionHelperListView(ListAPIView):
    queryset = Add_New_Operator_Model.objects.all()
    serializer_class = ProductionOperatorSupervisor
    filter_backends = [SearchFilter]
    search_fields = ['Name','Code']


# Production Entry Fetch Unit Machine from Work Center Master
from All_Masters.models import Work_Center_Model
from .serializers import ProductionEntryUnitMachine

class ProductionEntryUnitMachineListView(generics.ListAPIView):
    queryset = Work_Center_Model.objects.all()
    serializer_class = ProductionEntryUnitMachine
    filter_backends = [SearchFilter]
    search_fields = ['WorkCenterCode', 'WorkCenterName']\
    




# Rework Production Entry 2
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import ProductionEntry2
from .serializers import ProductionEntrySerializer2, OOPurchaseSerializer2

class ProductionEntryViewSet2(viewsets.ModelViewSet):
    queryset = ProductionEntry2.objects.all()
    serializer_class = ProductionEntrySerializer2

    @action(detail=False, methods=['get'])
    def get_next_rework_no(self, request):
        # Get the year from the query params
        year = request.query_params.get('year', None)
        
        if not year:
            return Response({"error": "Year is required"}, status=400)
        
        try:
            # Generate the next rework number for the provided year
            next_rework_no = ProductionEntry2.generate_next_rework_no(int(year))
            return Response({"next_rework_no": next_rework_no})
        except ValueError as e:
            return Response({"error": str(e)}, status=400)


    def create(self, request, *args, **kwargs):
        # Handling the creation of a new ProductionEntry with nested ItemDetail
        serializer = OOPurchaseSerializer2(data=request.data)
        if serializer.is_valid():
            production_entry = serializer.save()  # This automatically saves both ProductionEntry and ItemDetail
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

# Rework Production: Rework production Entry

from rest_framework import viewsets
from .models import ProductDetail2
from .serializers import ProductDetailSerializer

class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = ProductDetail2.objects.all()
    serializer_class = ProductDetailSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_serializer_context(self):
        return {'request': self.request}

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import ProductDetailSerializer
from .models import ProductDetail2

class ProductDetailBulkCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        user = request.user

        if not isinstance(data, list):
            return Response({"error": "Expected a list of items."}, status=status.HTTP_400_BAD_REQUEST)

        # Pass the request in context for each item to access the user in the serializer
        serializer = ProductDetailSerializer(data=data, many=True, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max
from .models import ProductDetail2  

class GetNextReworkNo(APIView):
    def get(self, request, *args, **kwargs):
        # Get the year from the query parameters
        year = request.GET.get('year', None)

        if not year:
            return Response({"error": "Year is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            year = int(year)
        except ValueError:
            return Response({"error": "Invalid year format"}, status=status.HTTP_400_BAD_REQUEST)

        # Define the prefix, which includes the year (e.g., "2324" for year 2324)
        prefix = f"{year}"

        # Get the maximum rework_no for the given year, filtering based on the year part
        latest_rework_no = ProductDetail2.objects.filter(rework_no__startswith=f"REWPRO {prefix}").aggregate(Max('rework_no'))

        if latest_rework_no['rework_no__max']:
            # Extract the numeric part of the last rework_no (the part after the "REWPRO {year}")
            last_code = latest_rework_no['rework_no__max']
            number_part = int(last_code[len(f"REWPRO {prefix}"):])  # Skip the "REWPRO {year}" part and get the number
            next_code_number = number_part + 1
        else:
            # If no rework_no exists for this year, start from 1
            next_code_number = 1
        
        # Format the next number with leading zeros (6 digits, e.g., 000001 for next_code_number = 1)
        next_code_number_str = f"{next_code_number:05d}"
        
        # Generate the new rework_no (e.g., "REWPRO 232400001")
        next_rework_no = f"REWPRO {prefix}{next_code_number_str}"
        
        return Response({"next_rework_no": next_rework_no}, status=status.HTTP_200_OK)
    

    



# Production Entry Assembly:-


from rest_framework import viewsets
from .models import AssemblyProductionDetails
from .serializers import AssemblyProductionDetailsSerializer

class AssemblyProductionDetailsViewSet(viewsets.ModelViewSet):  # Renamed ProductDetailViewSet
    queryset = AssemblyProductionDetails.objects.all()
    serializer_class = AssemblyProductionDetailsSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max
from .models import AssemblyProductionDetails

class GetNextDpNo(APIView):
    def get(self, request, *args, **kwargs):
        # Get the year from the query parameters
        year = request.GET.get('year', None)

        if not year:
            return Response({"error": "Year is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            year = int(year)
        except ValueError:
            return Response({"error": "Invalid year format"}, status=status.HTTP_400_BAD_REQUEST)

        # Define the prefix, which includes the year (e.g., "2324" for year 2324)
        prefix = f"{year}"

        # Get the maximum rework_no for the given year, filtering based on the year part
        latest_dp_no = AssemblyProductionDetails.objects.filter(Prod_no__startswith=f"DP {prefix}").aggregate(Max('Prod_no'))

        if latest_dp_no['Prod_no__max']:
            # Extract the numeric part of the last dp_no (the part after the "DP {year}")
            last_code = latest_dp_no['Prod_no__max']
            number_part = int(last_code[len(f"DP {prefix}"):])  # Skip the "DP {year}" part and get the number
            next_code_number = number_part + 1
        else:
            # If no rework_no exists for this year, start from 1
            next_code_number = 1
        
        # Format the next number with leading zeros (6 digits, e.g., 000001 for next_code_number = 1)
        next_code_number_str = f"{next_code_number:05d}"
        
        # Generate the new DP number (e.g., "DP 232400001")
        next_dp_no = f"DP {prefix}{next_code_number_str}"
        
        return Response({"next_dp_no": next_dp_no}, status=status.HTTP_200_OK)


from .serializers import ReworkReason2Serializer,RejectReason2Serializer
from .models import ReworkReason2,RejectReason2

class ReworkReason2ListCreate(generics.ListCreateAPIView):
    queryset = ReworkReason2.objects.all()
    serializer_class = ReworkReason2Serializer

class ReworkReason2RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReworkReason2.objects.all()
    serializer_class = ReworkReason2Serializer


class RejectReason2ListCreate(generics.ListCreateAPIView):
    queryset = RejectReason2.objects.all()
    serializer_class = RejectReason2Serializer

class RejectReason2RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = RejectReason2.objects.all()
    serializer_class = RejectReason2Serializer

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from .models import AssemblyProductionDetails

def generate_assembly_pdf(request, pk):
    entry = get_object_or_404(AssemblyProductionDetails, pk=pk)
    idle_times = entry.MachineIdleTimeAss.all()
    item_stocks = entry.ItemStockDetails.all()
    rework_reasons = entry.ReworkReason.all()
    reject_reasons = entry.RejectReason.all()

    template = get_template('ProductionEntryAssembly.html')  # Must be created
    html = template.render({
        'entry': entry,
        'idle_times': idle_times,
        'item_stocks': item_stocks,
        'rework_reasons': rework_reasons,
        'reject_reasons': reject_reasons,
    })

    pdf_file = HTML(string=html).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="assembly_production_{pk}.pdf"'
    return response


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AssemblyProductionDetails

class AssemblyProductionSummaryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        plant = request.query_params.get('plant')
        prod_no = request.query_params.get('prod_no')

        queryset = AssemblyProductionDetails.objects.all()
        if plant:
            queryset = queryset.filter(Plant__icontains=plant)
        if prod_no:
            queryset = queryset.filter(Prod_no__icontains=prod_no)

        data = []
        for entry in queryset:
            data.append({
                "id": entry.id,
                "Plant": entry.Plant,
                "Prod_no": entry.Prod_no,
                "Date": entry.Date,
                "Time": entry.Time,
                "Shift": entry.shift,
                "Contractor": entry.contractor,
                "Operator": entry.operator,
                "FGItem": entry.FGItem,
                "ProdQty": entry.ProdQty,
                "ReworkQty": entry.Rework_Qty,
                "RejectQty": entry.Reject_Qty,
                "View": f"/Production/ProductionEntryAssembly/pdf/{entry.id}/",
                "Edit": f"/Production/api/production-entriesAss/{entry.id}/"
            })

        return Response(data)



# Contractor Production Entry

from rest_framework import viewsets
from .models import ProductionRecord
from .serializers import ProductSerializer

class ProductionRecordViewSet(viewsets.ModelViewSet):
    queryset = ProductionRecord.objects.all()
    serializer_class = ProductSerializer


# FG Scrap Rejection Note

from rest_framework import viewsets
from .models import FGScrapDetails
from .serializers import FGScrapDetailsSerializer

class FGScrapDetailsViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = FGScrapDetails.objects.all()
    serializer_class = FGScrapDetailsSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max
from .models import FGScrapDetails

class GetNextNoteNo(APIView):
    def get(self, request, *args, **kwargs):
        year = request.GET.get('year', None)

        if not year:
            return Response({"error": "Year is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            year = int(year)
        except ValueError:
            return Response({"error": "Invalid year format"}, status=status.HTTP_400_BAD_REQUEST)

        prefix = f"{year}"

        latest_note_no = FGScrapDetails.objects.filter(NoteNo__startswith=f"FGSR {prefix}").aggregate(Max('NoteNo'))

        if latest_note_no['NoteNo__max']:
            last_code = latest_note_no['NoteNo__max']
            number_part = int(last_code[len(f"FGSR {prefix}"):])  
            next_code_number = number_part + 1
        else:
            next_code_number = 1
        
        next_code_number_str = f"{next_code_number:05d}"
        next_note_no = f"FGSR {prefix}{next_code_number_str}"
        
        return Response({"next_note_no": next_note_no}, status=status.HTTP_200_OK)


from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from .models import FGScrapDetails

def generate_FGScrap_pdf(request, pk):
    scrap_detail = get_object_or_404(FGScrapDetails, pk=pk)
    scrap_items = scrap_detail.scrap_items.all()

    template = get_template('FGScrapLineRejectionNote.html')  # Create this template
    html = template.render({
        'scrap_detail': scrap_detail,
        'scrap_items': scrap_items,
    })

    pdf_file = HTML(string=html).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="fgscrap_{pk}.pdf"'
    return response

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from .models import FGScrapDetails
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class FGScrapDetailsAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = FGScrapDetails.objects.all()

        # Optional search filter
        search_query = request.GET.get("search", "")
        if search_query:
            queryset = queryset.filter(
                Q(Plant__icontains=search_query) |
                Q(Series__icontains=search_query) |
                Q(NoteNo__icontains=search_query) |
                Q(ItemCode__icontains=search_query) |
                Q(PartCode__icontains=search_query)
            )

        data = []
        for detail in queryset:
            data.append({
                "id": detail.id,
                "Plant": detail.Plant,
                "Series": detail.Series,
                "NoteType": detail.NoteType,
                "NoteNo": detail.NoteNo,
                "NoteDate": detail.NoteDate,
                "ItemCode": detail.ItemCode,
                "PartCode": detail.PartCode,
                "Stock": detail.Stock,
                "Rework": detail.Rework,
                "Reject": detail.Reject,
                "ScrapReason": detail.ScrapReason,
                "User": detail.created_by.username if detail.created_by else None,  
                "Auth": detail.is_verified,  
                "View": f"/Production/FGScrap/pdf/{detail.id}/",
                "Edit": f"/Production/api/FGScrapDetails/{detail.id}/",
            })

        return Response(data)



# Scrap Line Rejection Note
from rest_framework import viewsets
from .models import ScrapLineRejectionNote
from .serializers import ScrapRejectDetailsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max
from .models import ScrapLineRejectionNote

class ScrapRejectionNoteViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ScrapLineRejectionNote.objects.all()
    serializer_class=ScrapRejectDetailsSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class GetNextNote(APIView):
    def get(self, request, *args, **kwargs):
        year = request.GET.get('year', None)

        if not year:
            return Response({"error": "Year is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            year = int(year)
        except ValueError:
            return Response({"error": "Invalid year format"}, status=status.HTTP_400_BAD_REQUEST)

        prefix = f"{year}"

        latest_note_no = ScrapLineRejectionNote.objects.filter(ScrapRejectionNo__startswith=f"Line R {prefix}").aggregate(Max('ScrapRejectionNo'))

        if latest_note_no['ScrapRejectionNo__max']:
            last_code = latest_note_no['ScrapRejectionNo__max']
            number_part = int(last_code[len(f"Line R {prefix}"):])  
            next_code_number = number_part + 1
        else:
            next_code_number = 1
        
        next_code_number_str = f"{next_code_number:05d}"
        next_ScrapRejectionNo = f"Line R {prefix}{next_code_number_str}"
        
        return Response({"next_ScrapRejectionNo": next_ScrapRejectionNo}, status=status.HTTP_200_OK)

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from .models import ScrapLineRejectionNote

def generate_scrap_line_rejection_pdf(request, pk):
    rejection_note = get_object_or_404(ScrapLineRejectionNote, pk=pk)
    rejection_items = rejection_note.scrap_items.all()

    template = get_template('ScrapLineRejectionNote.html')  # You must create this template
    html = template.render({
        'rejection_note': rejection_note,
        'rejection_items': rejection_items,
    })

    pdf_file = HTML(string=html).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="scrap_rejection_{pk}.pdf"'
    return response


from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import ScrapLineRejectionNote

class ScrapLineRejectionAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = ScrapLineRejectionNote.objects.all()
        filters = {
            "ScrapRejectionNo__icontains": request.GET.get("scrap_rejection_no"),
            "TrnType__icontains": request.GET.get("trn_type"),
            "Series__icontains": request.GET.get("series"),
            "cust_SuppName__icontains": request.GET.get("cust_supp_name"),
            "ScrapRejectionItem__icontains": request.GET.get("scrap_rejection_item"),
            "created_by__username__icontains": request.GET.get("user"),
        }

        # Apply non-null filters
        for key, value in filters.items():
            if value:
                queryset = queryset.filter(**{key: value})

        # Date filtering
        date_from = request.GET.get("date_from")
        date_to = request.GET.get("date_to")

        if date_from:
            try:
                date_from_parsed = datetime.strptime(date_from, "%Y-%m-%d")
                queryset = queryset.filter(ScrapRejectionNoteDate__gte=date_from_parsed)
            except ValueError:
                return Response({"error": "Invalid date_from format. Use YYYY-MM-DD."}, status=400)

        if date_to:
            try:
                date_to_parsed = datetime.strptime(date_to, "%Y-%m-%d")
                queryset = queryset.filter(ScrapRejectionNoteDate__lte=date_to_parsed)
            except ValueError:
                return Response({"error": "Invalid date_to format. Use YYYY-MM-DD."}, status=400)

        # Serialize results
        data = []
        for note in queryset:
            data.append({
                "id": note.id,
                "Plant": note.Plant,
                "ScrapRejectionNo": note.ScrapRejectionNo,
                "ScrapRejectionNoteDate": note.ScrapRejectionNoteDate,
                "TrnType": note.TrnType,
                "ItemNo": note.ItemNo,
                "RejectReason": note.RejectReason,
                "ScrapRejectRemark": note.ScrapRejectRemark,
                "ScrapRejectionItem": note.ScrapRejectionItem,
                "ScrapQty": note.ScrapQty,
                "cust_SuppName": note.cust_SuppName,
                "User": note.created_by.username if note.created_by else None,
                "Auth": note.is_verified,
                "View": f"/Production/scrap-line-rejection/pdf/{note.id}/",
                "Edit": f"/Production/api/ScrapLineRejectionNote/{note.id}/",
            })

        return Response(data)




# Work Order Customer Supplier Search
from All_Masters.models import Item
from .serializers import WO_Customer_Serializer
class Work_Order_Customer_Search(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = WO_Customer_Serializer
    filter_backends = [SearchFilter]
    search_fields = ['Name', 'number']


# Work Order Entry api
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max
from .models import WorkOrderEntry
from .serializers import WorkOrderSerializer

class WorkOrderView(viewsets.ModelViewSet):  
    queryset = WorkOrderEntry.objects.all()
    serializer_class = WorkOrderSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max
from .models import WorkOrderEntry

class WOGetNextDpNo(APIView):
    def get(self, request, *args, **kwargs):
        # Get the year from the query parameters
        year = request.GET.get('year', None)

        if not year:
            return Response({"error": "Year is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            year = int(year)
        except ValueError:
            return Response({"error": "Invalid year format"}, status=status.HTTP_400_BAD_REQUEST)

        # Define the prefix, which includes the year (e.g., "2324" for year 2324)
        prefix = f"{year}"

        # Get the maximum wo_no for the given year, filtering based on the year prefix
        latest_wo_no = WorkOrderEntry.objects.filter(wo_no__startswith=prefix).aggregate(Max('wo_no'))

        if latest_wo_no['wo_no__max']:
            # Extract the numeric part of the last wo_no (the part after the year prefix)
            last_code = latest_wo_no['wo_no__max']
            number_part = int(last_code[len(prefix):])  # Skip the year prefix and get the number
            next_code_number = number_part + 1
        else:
            # If no wo_no exists for this year, start from 1
            next_code_number = 1
        
        # Format the next number with leading zeros (5 digits, e.g., 00001)
        next_code_number_str = f"{next_code_number:05d}"
        
        # Generate the new number without DP prefix (e.g., "232400001")
        next_wo_no = f"{prefix}{next_code_number_str}"
        
        return Response({"next_wo_no": next_wo_no}, status=status.HTTP_200_OK)
    
#
from rest_framework.generics import ListAPIView
from .models import ProductDetail2
from .serializers import ProductDetailGetSerializer

class ProductDetailGetView(ListAPIView):
    queryset = ProductDetail2.objects.all()
    serializer_class = ProductDetailGetSerializer



# production me allmaster itemtable data
from All_Masters.models import *
from .serializers import ItemdropdownSerializer
class ItemdropdownAPIView(generics.ListAPIView):
    serializer_class = ItemdropdownSerializer
    def get_queryset(self):
        query = self.request.query_params.get('q', '').strip()
        if query:
            return ItemTable.objects.filter(
                Q(Part_Code__icontains=query)|
                Q(Name_Description__icontains=query)|
                Q(part_no__icontains=query)
            )
        return ItemTable.objects.all()
    
from .serializers import BOMItemdropSerializer
class BOMItemByPartCodeAPIView(APIView):
    def get(self, request):
        part_code = request.query_params.get('part_code')
        if not part_code:
            return Response({'error': 'part_code is required'}, status=status.HTTP_400_BAD_REQUEST)

        items = ItemTable.objects.filter(Part_Code=part_code)
        if not items.exists():
            return Response({'error': 'Item with given Part_Code not found'}, status=status.HTTP_404_NOT_FOUND)

        bom_items = BOMItem.objects.filter(item__in=items)
        serializer = BOMItemdropSerializer(bom_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



from Store.models import  NewGrnList
class HeatNoListAPIView(APIView):
    """
    API to get distinct Heat Numbers from GRN
    """
    def get(self, request):
        try:
            part_code = request.GET.get("part_code", "").strip()

            # fetch heat numbers from NewGrnList
            queryset = NewGrnList.objects.all()

            if part_code:
                queryset = queryset.filter(ItemNoCode__iexact=part_code)

            # get distinct heat numbers
            heat_nos = queryset.values_list("HeatNo", flat=True).distinct()

            return Response({
                "success": True,
                "message": "Heat numbers fetched successfully",
                "heat_numbers": [hn for hn in heat_nos if hn]  # remove None/empty
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "success": False,
                "message": f"Error fetching heat numbers: {str(e)}",
                "heat_numbers": []
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# from .serializers import WipSerializer
# class WIPStockreport(APIView):
#     def get(self, request):
#         part_code= request.query_params.get('part_code')
#         if not part_code:
#             return Response({'error':'part_code is required'}, status=status.HTTP_400_BAD_REQUEST)
#         items =ItemTable.objects.filter(Part_Code=part_code)
#         if not items.exists():
#             return Response({'error': 'Item with given Part_Code not found'}, status=status.HTTP_404_NOT_FOUND)
#         bom_items= BOMItem.objects.filter(item__in=items)
#         serializer= WipSerializer(bom_items, many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

# class WIPStockreport(APIView):
#     def get(self, request):
#         query = request.query_params.get('q', '').strip()
#         if not query:
#             return Response({'error': 'Search query "q" is required'}, status=status.HTTP_400_BAD_REQUEST)

#         # Filter ItemTable with any match of part_code, part_no or name_description
#         items = ItemTable.objects.filter(
#             Q(Part_Code__icontains=query) |
#             Q(part_no__icontains=query) |
#             Q(Name_Description__icontains=query)
#         )

#         if not items.exists():
#             return Response({'error': 'No items found matching your query'}, status=status.HTTP_404_NOT_FOUND)

#         bom_items = BOMItem.objects.filter(item__in=items)
#         serializer = WipSerializer(bom_items, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)   
#fetch data for wip production
# from All_Masters.serializers import BOMItemSerializer 
# class WIPProduction(APIView):
#     def get(self, request):
#         grouped_data = {}
#         all_items = ItemTable.objects.all()

#         for item in all_items:
#             bom_items = BOMItem.objects.filter(item=item)
#             if not bom_items.exists():
#                 continue

#             serializer = BOMItemSerializer(bom_items, many=True)
            
#             # grouped_data[item.Part_Code] = {
#             #     "item_id": item.id,
#             #     "bom_items": serializer.data
#             # }

#             grouped_data[f"{item.Part_Code} - {item.Name_Description}"] = {
#                 "item_id": item.id,
#                 "bom_items": serializer.data
#              }

#         if not grouped_data:
#             return Response(
#                 {"message": "No BOM data found."},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         return Response(grouped_data, status=status.HTTP_200_OK)

