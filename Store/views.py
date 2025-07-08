from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max
import re
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Store Module:- Gate Inward Entry:- General Details


class GeneralDetailsViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = GeneralDetails.objects.all()
    serializer_class = GeneralDetailsSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class GetNextGeneralDetails(APIView):
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
        latest_GE_No = GeneralDetails.objects.filter(GE_No__startswith=f"GE {prefix}").aggregate(Max('GE_No'))

        if latest_GE_No['GE_No__max']:
            # Extract the numeric part of the last dp_no (the part after the "MRN {year}")
            last_code = latest_GE_No['GE_No__max']
            number_part = int(last_code[len(f"GE {prefix}"):])  # Skip the "MRN {year}" part and get the number
            next_code_number = number_part + 1
        else:
            # If no rework_no exists for this year, start from 1
            next_code_number = 1
        
        # Format the next number with leading zeros (6 digits, e.g., 000001 for next_code_number = 1)
        next_code_number_str = f"{next_code_number:05d}"
        
        # Generate the new MRN number (e.g., "DP 232400001")
        next_GE_No = f"GE {prefix}{next_code_number_str}"
        
        return Response({"next_GE_No": next_GE_No}, status=status.HTTP_200_OK)

# Store Module:- NEW MRN
class NewMrnView(viewsets.ModelViewSet):
    queryset = NewMrn.objects.all()
    serializer_class = NewMrnSerializer

class GetNextMrnNo(APIView):
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
        latest_MRN_no = NewMrn.objects.filter(MRN_no__startswith=f"MRN {prefix}").aggregate(Max('MRN_no'))

        if latest_MRN_no['MRN_no__max']:
            # Extract the numeric part of the last dp_no (the part after the "MRN {year}")
            last_code = latest_MRN_no['MRN_no__max']
            number_part = int(last_code[len(f"MRN {prefix}"):])  # Skip the "MRN {year}" part and get the number
            next_code_number = number_part + 1
        else:
            # If no rework_no exists for this year, start from 1
            next_code_number = 1
        
        # Format the next number with leading zeros (6 digits, e.g., 000001 for next_code_number = 1)
        next_code_number_str = f"{next_code_number:05d}"
        
        # Generate the new MRN number (e.g., "DP 232400001")
        next_MRN_no = f"MRN {prefix}{next_code_number_str}"
        
        return Response({"next_mrn_no": next_MRN_no}, status=status.HTTP_200_OK)

# New MRN Item Search View
from All_Masters.models import ItemTable as ItemSearchView
from .serializers import NewMRNItemSerializer
from rest_framework.filters import SearchFilter 

class NewMRNItemSearchListView(generics.ListAPIView):
    queryset = ItemSearchView.objects.all()
    serializer_class = NewMRNItemSerializer
    filter_backends = [SearchFilter]
    search_fields = ['part_no', 'Part_Code', 'Item_Size', 'Name_Description']
    

# New MRN Employee Depatment Search Api

from All_Masters.models import Add_New_Operator_Model
from .serializers import NewMRNEmployeeDeptSerializer

class NewMRNEmployeeDeptListView(generics.ListAPIView):
    queryset = Add_New_Operator_Model.objects.all()
    serializer_class = NewMRNEmployeeDeptSerializer
    filter_backends = [SearchFilter]
    search_fields = ['Code', 'Name', 'Type', 'Department']



# Store Module:- SubCon GRN: 57F4 Inward Challan
class InwardChallanListCreate(generics.ListCreateAPIView):
    queryset = InwardChallan.objects.all()
    serializer_class = InwardChallanSerializer

class InwardChallanRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = InwardChallan.objects.all()
    serializer_class = InwardChallanSerializer


# Store Module:- SubCon GRN: Job Work Inward Challan
class Job_WorkListCreate(generics.ListCreateAPIView):
    queryset = Job_Work.objects.all()
    serializer_class = Job_WorkSerializer

class Job_WorkRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job_Work.objects.all()
    serializer_class = Job_WorkSerializer

# Store Module:- SubCon GRN: Vendor Scrap Inward
class VendorScrap_ListCreate(generics.ListCreateAPIView):
    queryset = VendorScrap.objects.all()
    serializer_class = VendorScrapSerializer

class VendorScrap_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = VendorScrap.objects.all()
    serializer_class = VendorScrapSerializer

# Store Module:- Material Issue Challan
class MaterialIssue_ListCreate(generics.ListCreateAPIView):
    queryset = MaterialIssue.objects.all()
    serializer_class = MaterialIssueSerializer

class MaterialIssue_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaterialIssue.objects.all()
    serializer_class = MaterialIssueSerializer

# Store Module:- Material Issue General
class Material_Issue_General_ListCreate(generics.ListCreateAPIView):
    queryset = Material_Issue_General.objects.all()
    serializer_class = Material_Issue_GeneralSerializer

class Material_Issue_General_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material_Issue_General.objects.all()
    serializer_class = Material_Issue_GeneralSerializer

# Store Module:- DeliveryChallan
class DeliveryChallan_ListCreate(generics.ListCreateAPIView):
    queryset = DeliveryChallan.objects.all()
    serializer_class = DeliveryChallan_GeneralSerializer

class DeliveryChallan_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryChallan.objects.all()
    serializer_class = DeliveryChallan_GeneralSerializer


# Store Module:- SecondDeliveryChallan
class SecondDeliveryChallann_ListCreate(generics.ListCreateAPIView):
    queryset = SecondDeliveryChallan.objects.all()
    serializer_class = SecondDeliveryChallan_Serializer

class SecondDeliveryChallan_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SecondDeliveryChallan.objects.all()
    serializer_class = SecondDeliveryChallan_Serializer

# Store Module:- DC_GRN
class DC_GRN_ListCreate(generics.ListCreateAPIView):
    queryset = DC_GRN.objects.all()
    serializer_class = DC_GRN_Serializer

class DC_GRN_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = DC_GRN.objects.all()
    serializer_class = DC_GRN_Serializer


#testing 

class MainGroupListCreateAPIView(generics.ListCreateAPIView):
    queryset = MainGroup.objects.all()
    serializer_class = MainGroupSerializer

class MainGroupList_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = MainGroup.objects.all()
    serializer_class = MainGroupSerializer

class ItemGroupListCreateAPIView(generics.ListCreateAPIView):
    queryset = ItemGroup.objects.all()
    serializer_class = ItemGroupSerializer

class ItemGroup_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemGroup.objects.all()
    serializer_class = ItemGroupSerializer

class ItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = ItemTable.objects.all()
    serializer_class = ItemSerializer



class NextPartNoByTypeAPIView(generics.GenericAPIView):
    def get(self, request):
        item_group_type = request.query_params.get('type', None)
        if not item_group_type:
            return Response({'error': 'ItemGroup type is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            item_group = ItemGroup.objects.get(name=item_group_type)

            # Get the last item for the specified ItemGroup type
            last_item_group = ItemTable.objects.filter(item_group=item_group).order_by('-id').first()
            if last_item_group:
                # Extract numeric part from the part_no
                match = re.search(r'\d+', last_item_group.part_no)
                last_group_number = int(match.group()) if match else 0
            else:
                last_group_number = 0  # No items yet

            # Generate next part number
            next_item_part_no = f"{item_group.name[:2].upper()}{str(last_group_number + 1).zfill(3)}"

            return Response({'next_item_part_no': next_item_part_no}, status=status.HTTP_200_OK)

        except ItemGroup.DoesNotExist:
            return Response({'error': 'ItemGroup not found'}, status=status.HTTP_404_NOT_FOUND)

# views.py


class ItemCreateAPIView(generics.CreateAPIView):
    queryset = ItemTable.objects.all()
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        serializer.save()  # Save the instance


# views.py




class ItemCreateAPIView(generics.CreateAPIView):
    queryset = ItemTable.objects.all()
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        serializer.save()

class ItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemTable.objects.all()
    serializer_class = ItemSerializer

class NextPartNoAPIView(APIView):
    def get(self, request):
        main_group_name = request.query_params.get('main_group')
        item_group_name = request.query_params.get('item_group')

        if not main_group_name or not item_group_name:
            return Response({'error': 'Both main_group and item_group are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            main_group = MainGroup.objects.get(name=main_group_name)
            item_group = ItemGroup.objects.get(name=item_group_name)

            next_part_no = self.generate_part_no(main_group, item_group)
            return Response({'next_part_no': next_part_no}, status=status.HTTP_200_OK)
        except MainGroup.DoesNotExist:
            return Response({'error': 'MainGroup not found.'}, status=status.HTTP_404_NOT_FOUND)
        except ItemGroup.DoesNotExist:
            return Response({'error': 'ItemGroup not found.'}, status=status.HTTP_404_NOT_FOUND)

    def generate_part_no(self, main_group, item_group):
        main_group_code = f"{main_group.name[:2].upper()}{item_group.name[:2].upper()}"
        last_item = ItemTable.objects.filter(item_group=item_group).order_by('-id').first()
        last_group_number = 0 if not last_item else int(last_item.part_no[4:]) + 1
        return f"{main_group_code}{str(last_group_number).zfill(3)}"

 
from rest_framework import viewsets
from .models import GrnGenralDetail
from .serializers import GrnGenralDetailSerializer

class GrnGenralDetailViewSet(viewsets.ModelViewSet):
    queryset = GrnGenralDetail.objects.all()
    serializer_class = GrnGenralDetailSerializer


from rest_framework import status
from django.db.models import Max
from .models import GrnGenralDetail

class GetNextGrnNo(APIView):
    def get(self, request, *args, **kwargs):
        year = request.GET.get('year', None)

        if not year:
            return Response({"error": "Year is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            year = int(year)
        except ValueError:
            return Response({"error": "Invalid year format"}, status=status.HTTP_400_BAD_REQUEST)

        prefix = f"{year}"

        latest_Grn_No = GrnGenralDetail.objects.filter(GrnNo__startswith=f"GRN {prefix}").aggregate(Max('GrnNo'))

        if latest_Grn_No['GrnNo__max']:
            last_code = latest_Grn_No['GrnNo__max']
            number_part = int(last_code[len(f"GRN {prefix}"):])  
            next_code_number = number_part + 1
        else:
            next_code_number = 1
        
        next_code_number_str = f"{next_code_number:05d}"
        next_GrnNo = f"GRN {prefix}{next_code_number_str}"
        
        return Response({"next_GrnNo": next_GrnNo}, status=status.HTTP_200_OK)


# New Mrn List With Pdf Generate
from .models import GrnGenralDetail, NewGrnList
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from .serializers import GrnGenralDetailSerializer

class GrnDetailAPIView(generics.ListAPIView):
    queryset = GrnGenralDetail.objects.all()
    serializer_class = GrnGenralDetailSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []
        for grn in queryset:
            grn_items = grn.NewGrnList.all()  # Related items
            items_data = [
                {
                    "ItemNoCode": item.ItemNoCode,
                    "Description": item.Description,
                    "UnitCode": item.UnitCode,
                    "ChalQty": item.ChalQty,
                    "ShortExcessQty": item.ShortExcessQty,
                    "Rate": item.Rate
                }
                for item in grn_items
            ]
            data.append({
                "id": grn.id, 
                "Plant": grn.Plant,
                "GrnNo": grn.GrnNo,
                "GrnDate": grn.GrnDate,
                "GrnTime": grn.GrnTime,
                "InvoiceNo": grn.InvoiceNo,
                "InvoiceDate": grn.InvoiceDate,
                "ChallanNo": grn.ChallanNo,
                "ChallanDate": grn.ChallanDate,
                "LrNo": grn.LrNo,
                "VehicleNo": grn.VehicleNo,
                "Transporter": grn.Transporter,
                "SelectSupplier": grn.SelectSupplier,
                "SelectPO": grn.SelectPO,
                "SelectItem": grn.SelectItem,
                "EWayBillNo": grn.EWayBillNo,
                "EWayBillDate": grn.EWayBillDate,
                "PDF_Link": f"/Store/pdf/{grn.id}/",
                "Items": items_data
            })
        return Response(data)

def generate_pdf(request, id):
    grn_detail = get_object_or_404(GrnGenralDetail, id=id)
    grn_items = grn_detail.NewGrnList.all()  # Fetch related items

    template = get_template('PurchaseGRN.html')
    html_content = template.render({'grn_detail': grn_detail, 'grn_items': grn_items})

    pdf_file = HTML(string=html_content).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="grn_{id}.pdf"'
    return response


# Fetch Code for PurchaseGRN
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import GeneralDetails
from .serializers import GeneralDetailsLimitedSerializer

@api_view(['GET'])
def get_general_details_limited(request, id=None):
    if id is not None:
        try:
            instance = GeneralDetails.objects.get(id=id)
            serializer = GeneralDetailsLimitedSerializer(instance)
            return Response(serializer.data)
        except GeneralDetails.DoesNotExist:
            return Response({'error': 'Data not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        data = GeneralDetails.objects.all()
        serializer = GeneralDetailsLimitedSerializer(data, many=True)
        return Response(serializer.data)


# Fetch PO Item
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Purchase.models import PurchasePO, ItemDetail
from .serializers import PurchasePOSerializer, ItemDetailSerializer,GSTDetailSerializer

# GET API 1: Search by PoNo
class PurchasePODetailByPoNo(APIView):
    def get(self, request, pono):
        try:
            # Fetch PurchasePO by PoNo
            po = PurchasePO.objects.get(PoNo=pono)

            # Serialize Item_Detail_Enter with PoNo and PoDate included inside each item
            item_details_serializer = ItemDetailSerializer(po.Item_Detail_Enter.all(), many=True)

            # Add PoNo and PoDate inside each Item_Detail_Enter object
            for item in item_details_serializer.data:
                item['PoNo'] = po.PoNo
                item['PoDate'] = po.PoDate

            # Serialize Gst_Details as before
            gst_details_serializer = GSTDetailSerializer(po.Gst_Details.all(), many=True)

            # Return the data without PoNo and PoDate at the top level
            data = {
                "Item_Detail_Enter": item_details_serializer.data,
                "Gst_Details": gst_details_serializer.data
            }

            return Response(data, status=status.HTTP_200_OK)

        except PurchasePO.DoesNotExist:
            return Response({"error": "PO not found"}, status=status.HTTP_404_NOT_FOUND)


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from Purchase.models import PurchasePO
from .serializers import ItemDetailSerializer, GSTDetailSerializer
from rest_framework.exceptions import ValidationError

class GetByPoNoAndItem(APIView):
    def get(self, request):
        pono = request.query_params.get('PoNo')
        item = request.query_params.get('Item')

        if not pono or not item:
            raise ValidationError("Both 'PoNo' and 'Item' query parameters are required.")

        try:
            po = PurchasePO.objects.get(PoNo=pono)
        except PurchasePO.DoesNotExist:
            return Response({"error": "PO with the provided PoNo not found."}, status=status.HTTP_404_NOT_FOUND)

        matching_items = po.Item_Detail_Enter.filter(Item=item)
        matching_gst = po.Gst_Details.filter(ItemCode=item)

        if not matching_items.exists():
            return Response({"error": "No matching Item_Detail_Enter found for the given PoNo and Item."}, status=status.HTTP_404_NOT_FOUND)

        if not matching_gst.exists():
            return Response({"error": "No matching Gst_Details found for the given PoNo and Item."}, status=status.HTTP_404_NOT_FOUND)

        # Serialize Item_Detail_Enter
        item_serializer = ItemDetailSerializer(matching_items, many=True)
        item_data = item_serializer.data

        # Inject PoNo and PoDate into each item
        for item_obj in item_data:
            item_obj["PoNo"] = po.PoNo
            item_obj["PoDate"] = po.PoDate

        # Serialize GST details
        gst_serializer = GSTDetailSerializer(matching_gst, many=True)

        return Response({
            "Item_Detail_Enter": item_data,
            "Gst_Details": gst_serializer.data
        }, status=status.HTTP_200_OK)




# New Material Issue
from .models import MaterialChallan
from .serializers import MaterialChallanSerializer
from rest_framework import viewsets

class MaterialChallanView(viewsets.ModelViewSet):
    queryset = MaterialChallan.objects.all()
    serializer_class = MaterialChallanSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max

class GetNextChallanNo(APIView):
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
        latest_challan_no = MaterialChallan.objects.filter(ChallanNo__startswith=f"Challan No : {prefix}").aggregate(Max('ChallanNo'))

        if latest_challan_no['ChallanNo__max']:
            # Extract the numeric part of the last dp_no (the part after the "Challan {year}")
            last_code = latest_challan_no['ChallanNo__max']
            number_part = int(last_code[len(f"Challan No : {prefix}"):])  # Skip the "Challan {year}" part and get the number
            next_code_number = number_part + 1
        else:
            # If no rework_no exists for this year, start from 1
            next_code_number = 1
        
        # Format the next number with leading zeros (6 digits, e.g., 000001 for next_code_number = 1)
        next_code_number_str = f"{next_code_number:05d}"
        
        # Generate the new Challan number (e.g., "Challan No : 232400001")
        next_challan_no = f"Challan No : {prefix}{next_code_number_str}"
        
        return Response({"next_challan_no": next_challan_no}, status=status.HTTP_200_OK)
    


# New Gate Entry:- Fetch Supplier with PDF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from All_Masters.models import Item as Item2
from Purchase.models import PurchasePO
from .serializers import ItemSearchResultSerializer


class ItemSearchAPIView(APIView):
    def get(self, request):
        search_term = request.GET.get('query', '')
        if not search_term:
            return Response({"error": "Missing query parameter."}, status=status.HTTP_400_BAD_REQUEST)

        items = Item2.objects.filter(is_verified=True).filter(
            models.Q(Name__icontains=search_term) | models.Q(number__icontains=search_term)
        )

        results = []
        for item in items:
            matching_pos = PurchasePO.objects.filter(CodeNo=item.number)
            for po in matching_pos:
                results.append({
                    "Name": item.Name,
                    "number": item.number,
                    "Type": item.type,
                    "PoNo": po.PoNo,
                    "po_id": po.id,
                })

        serializer = ItemSearchResultSerializer(results, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


# Gate Inward Entry Registered
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from .models import GeneralDetails

def generate_gateinward_pdf(request, pk):
    entry = get_object_or_404(GeneralDetails, pk=pk)
    item_details = entry.ItemDetails.all()

    template = get_template('gate_inward_pdf.html')  # Make sure this template exists
    html = template.render({
        'entry': entry,
        'item_details': item_details,
    })

    pdf_file = HTML(string=html).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="gateinward_{pk}.pdf"'
    return response


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import GeneralDetails
from datetime import datetime

class GateInwardSummaryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        ge_no = request.query_params.get('ge_no')
        type_param = request.query_params.get('type')
        supp_cust = request.query_params.get('supp_cust')
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')

        queryset = GeneralDetails.objects.all()

        if ge_no:
            queryset = queryset.filter(GE_No__icontains=ge_no)
        if type_param:
            queryset = queryset.filter(Type__icontains=type_param)
        if supp_cust:
            queryset = queryset.filter(Supp_Cust__icontains=supp_cust)
        if from_date:
            try:
                from_date_obj = datetime.strptime(from_date, "%Y-%m-%d")
                queryset = queryset.filter(GE_Date__gte=from_date_obj)
            except ValueError:
                pass  # ignore invalid date
        if to_date:
            try:
                to_date_obj = datetime.strptime(to_date, "%Y-%m-%d")
                queryset = queryset.filter(GE_Date__lte=to_date_obj)
            except ValueError:
                pass  # ignore invalid date

        data = []
        for entry in queryset:
            data.append({
                "id": entry.id,
                "Plant": entry.Plant,
                "GE_No": entry.GE_No,
                "GE_Date": entry.GE_Date,
                "GE_Time": entry.GE_Time,
                "Type": entry.Type,
                "Supp_Cust": entry.Supp_Cust,
                "ChallanNo": entry.ChallanNo,
                "ChallanDate": entry.ChallanDate,
                "InVoiceNo": entry.InVoiceNo,
                "Invoicedate": entry.Invoicedate,
                "User": entry.created_by.username if entry.created_by else None,
                "View": f"/Store/gate-inward/pdf/{entry.id}/",
                "Edit": f"/Store/api/general-details/{entry.id}/"
            })

        return Response(data) 
    

# New DC GRN Serilaizer

from .models import NewDCgrn
from .serializers import NewDcgrnSerilaizer
from django.http import Http404
# List and Create View
class NewDCgrnCreateView(APIView):
    def get(self, request):
        try:
            details = NewDCgrn.objects.all()
            serializer = NewDcgrnSerilaizer(details, many=True)
            return Response({
                "message": "Data fetched successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "error": "An error occurred while fetching data.",
                "details": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = NewDcgrnSerilaizer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                "message": "Data created successfully.",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        except ValidationError as ve:
            return Response({
                "error": "Validation failed.",
                "details": ve.detail
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "error": "An unexpected error occurred while creating data.",
                "details": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Retrieve, Update, Delete View
class NewDCgrnDetailView(APIView):
    def get_object(self, pk):
        try:
            return get_object_or_404(NewDCgrn, pk=pk)
        except Http404:
            raise Http404("Object with the provided ID does not exist.")

    def get(self, request, pk):
        try:
            detail = self.get_object(pk)
            serializer = NewDcgrnSerilaizer(detail)
            return Response({
                "message": "Data retrieved successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                "error": "Object not found.",
                "details": f"No NewDCgrn found with ID {pk}."
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "error": "An error occurred while retrieving the data.",
                "details": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            detail = self.get_object(pk)
            serializer = NewDcgrnSerilaizer(detail, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                "message": "Data updated successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except ValidationError as ve:
            return Response({
                "error": "Validation failed during update.",
                "details": ve.detail
            }, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return Response({
                "error": "Update failed.",
                "details": f"No NewDCgrn found with ID {pk}."
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "error": "An unexpected error occurred while updating data.",
                "details": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, pk):
        try:
            detail = self.get_object(pk)
            detail.delete()
            return Response({
                "message": "Data deleted successfully."
            }, status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response({
                "error": "Delete failed.",
                "details": f"No NewDCgrn found with ID {pk}."
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "error": "An unexpected error occurred while deleting data.",
                "details": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# 57-F4 GRN(Inward Challan)
# from .models import InwardChallan
# from .serializers import InwardChallanSerializer
# from rest_framework import viewsets

# class InwardChallanListViews(viewsets.ModelViewSet):
#     queryset = InwardChallan.objects.all()
#     serializer_class = InwardChallanSerializer

from django.shortcuts import get_object_or_404
from .models import InwardChallan2
from .serializers import InwardChallanSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.http import Http404

# List and Create View
class InwardChallanCreateView(APIView):
    def get(self, request):
        try:
            details = InwardChallan2.objects.all()
            serializer = InwardChallanSerializer(details, many=True)
            return Response({
                "message": "Data fetched successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "error": "An error occurred while fetching data.",
                "details": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = InwardChallanSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                "message": "Data created successfully.",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        except ValidationError as ve:
            return Response({
                "error": "Validation failed.",
                "details": ve.detail
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "error": "An unexpected error occurred while creating data.",
                "details": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Retrieve, Update, Delete View
class InwardChallanDetailView(APIView):
    def get_object(self, pk):
        try:
            return get_object_or_404(InwardChallan2, pk=pk)
        except Http404:
            raise Http404("Object with the provided ID does not exist.")

    def get(self, request, pk):
        try:
            detail = self.get_object(pk)
            serializer = InwardChallanSerializer(detail)
            return Response({
                "message": "Data retrieved successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                "error": "Object not found.",
                "details": f"No InwardChallan found with ID {pk}."
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "error": "An error occurred while retrieving the data.",
                "details": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            detail = self.get_object(pk)
            serializer = InwardChallanSerializer(detail, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                "message": "Data updated successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except ValidationError as ve:
            return Response({
                "error": "Validation failed during update.",
                "details": ve.detail
            }, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return Response({
                "error": "Update failed.",
                "details": f"No InwardChallan found with ID {pk}."
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "error": "An unexpected error occurred while updating data.",
                "details": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, pk):
        try:
            detail = self.get_object(pk)
            detail.delete()
            return Response({
                "message": "Data deleted successfully."
            }, status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response({
                "error": "Delete failed.",
                "details": f"No InwardChallan found with ID {pk}."
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "error": "An unexpected error occurred while deleting data.",
                "details": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

# Subcon GRN Jobwark-Inward-Challan Views
from .models import JobworkInwardChallan
from .serializers import JobworkInwardChallanSerializer
# List and Create View
class JobworkInwardChallanCreateView(APIView):
    def get(self, request):
        try:
            details = JobworkInwardChallan.objects.all()
            serializer = JobworkInwardChallanSerializer(details, many=True)
            return Response({
                "message": "Data fetched successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "error": "An error occurred while fetching data.",
                "details": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = JobworkInwardChallanSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                "message": "Data created successfully.",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        except ValidationError as ve:
            return Response({
                "error": "Validation failed.",
                "details": ve.detail
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "error": "An unexpected error occurred while creating data.",
                "details": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Subcon GRN:- JobWork Inward-Challan
class JobworkInwardChallanDetailView(APIView):
    def get_object(self, pk):
        try:
            return get_object_or_404(JobworkInwardChallan, pk=pk)
        except Http404:
            raise Http404("Object with the provided ID does not exist.")

    def get(self, request, pk):
        try:
            detail = self.get_object(pk)
            serializer = JobworkInwardChallanSerializer(detail)
            return Response({
                "message": "Data retrieved successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                "error": "Object not found.",
                "details": f"No JobworkInwardChallan found with ID {pk}."
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "error": "An error occurred while retrieving the data.",
                "details": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            detail = self.get_object(pk)
            serializer = JobworkInwardChallanSerializer(detail, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                "message": "Data updated successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except ValidationError as ve:
            return Response({
                "error": "Validation failed during update.",
                "details": ve.detail
            }, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return Response({
                "error": "Update failed.",
                "details": f"No JobworkInwardChallan found with ID {pk}."
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "error": "An unexpected error occurred while updating data.",
                "details": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, pk):
        try:
            detail = self.get_object(pk)
            detail.delete()
            return Response({
                "message": "Data deleted successfully."
            }, status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response({
                "error": "Delete failed.",
                "details": f"No JobworkInwardChallan found with ID {pk}."
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "error": "An unexpected error occurred while deleting data.",
                "details": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




# Purchase se po details get api
from Purchase.models import NewJobWorkPoInfo
from Purchase.serializers import NewJobWorkPoInfoSerializer

class newjobworkpodetails(APIView):
    def get(self, request):
        supplier = request.query_params.get('supplier')
        if not supplier:
            return Response({"error": "supplier parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        pos = NewJobWorkPoInfo.objects.filter(Supplier__iexact=supplier)
        serializer = NewJobWorkPoInfoSerializer(pos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
