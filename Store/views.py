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
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import NewMrn
from .serializers import NewMrnSerializer

class NewMRNEmployeeDeptListView(generics.ListAPIView):
    queryset = Add_New_Operator_Model.objects.all()
    serializer_class = NewMRNEmployeeDeptSerializer
    filter_backends = [SearchFilter]
    search_fields = ['Code', 'Name', 'Type', 'Department']

class PendingMrnListView(generics.ListAPIView):
    serializer_class = NewMrnSerializer
    
    def get_queryset(self):
        return NewMrn.objects.filter(Approve_status=['Pending', 'pending'])


@api_view(['GET'])
def get_pending_mrns(request):
    try:
        pending_mrns = NewMrn.objects.filter(Approve_status__in=['Pending', 'pending'])
        serializer = NewMrnSerializer(pending_mrns, many=True)
        return Response({
            'success': True,
            'count': pending_mrns.count(),
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success': False,
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# Store Module:- SubCon GRN: 57F4 Inward Challan
class InwardChallanListCreate(generics.ListCreateAPIView):
    queryset = InwardChallan2.objects.all()
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
                "Edit": f"/Store/grn/edit/{grn.id}/",
                "delete":f"/Store/grn/delete/{grn.id}/",
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
from Purchase.models import PurchasePO,NewJobWorkPoInfo
from .serializers import ItemSearchResultSerializer
class ItemSearchAPIView(APIView):
    def get(self, request):
        search_term = request.GET.get('query', '')
        if not search_term:
            return Response({"error": "Missing query parameter."}, status=status.HTTP_400_BAD_REQUEST)

        results = []

        # 1. Item → PurchasePO
        items = Item2.objects.filter(is_verified=True).filter(
            models.Q(Name__icontains=search_term) | models.Q(number__icontains=search_term)
        )

        for item in items:
            matching_pos = PurchasePO.objects.filter(CodeNo=item.number)
            for po in matching_pos:
                results.append({
                    "source": "purchase",
                    "Name": item.Name,
                    "number": item.number,
                    "Type": item.type,
                    "PoNo": po.PoNo,
                    "po_id": po.id,
                })

        # 2. Direct search in NewJobWorkPoInfo (Supplier ya PoNo se)
        jobwork_pos = NewJobWorkPoInfo.objects.filter(
            models.Q(Supplier__icontains=search_term) | models.Q(PoNo__icontains=search_term)
        )

        for jw in jobwork_pos:
            results.append({
                "source": "jobwork",
                "Name": jw.Supplier,
                "number": item.number,
                "Type": "JobWorkPO",
                "PoNo": jw.PoNo,
                "po_id": jw.id,
            })

        if not results:
            return Response({"error": "No results found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSearchResultSerializer(results, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


# class ItemSearchAPIView(APIView):
#     def get(self, request):
#         search_term = request.GET.get('query', '')
#         if not search_term:
#             return Response({"error": "Missing query parameter."}, status=status.HTTP_400_BAD_REQUEST)

#         items = Item2.objects.filter(is_verified=True).filter(
#             models.Q(Name__icontains=search_term) | models.Q(number__icontains=search_term)
#         )

#         results = []
#         for item in items:
#             matching_pos = PurchasePO.objects.filter(CodeNo=item.number)
#             for po in matching_pos:
#                 results.append({
#                     "Name": item.Name,
#                     "number": item.number,
#                     "Type": item.type,
#                     "PoNo": po.PoNo,
#                     "po_id": po.id,
#                 })

#         serializer = ItemSearchResultSerializer(results, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)



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
                "Edit": f"/Store/api/general-details/{entry.id}/",
                "Delete": f"/Store/gate/entry/delete/{entry.id}/"
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
@api_view(['GET'])
def get_purchase_orders_by_supplier(request):
    """
    Get Purchase Orders by supplier name
    URL: /api/purchase-orders/?supplier=<supplier_name>
    """
    supplier_name = request.query_params.get('supplier')
    
    if not supplier_name:
        return Response(
            {'error': 'Supplier parameter is required'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        # Filter purchase orders by supplier (case-insensitive search)
        purchase_orders = PurchasePO.objects.filter(
            Supplier__icontains=supplier_name
        ).prefetch_related(
            'Item_Detail_Enter',
            'Gst_Details',
            'Item_Details_Other',
            'Schedule_Line',
            'Ship_To_Add'
        )
        
        if not purchase_orders.exists():
            return Response(
                {'message': f'No purchase orders found for supplier: {supplier_name}'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = PurchasePOSerializer(purchase_orders, many=True)
        
        return Response({
            'count': purchase_orders.count(),
            'supplier': supplier_name,
            'purchase_orders': serializer.data
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response(
            {'error': f'An error occurred: {str(e)}'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )



from weasyprint import HTML
from django.http import HttpResponse
from django.template.loader import get_template

# def generate_inwardchallan_pdf(request, pk):
#     challan = get_object_or_404(InwardChallan2, pk=pk)

#     serializer = InwardChallanSerializer(challan)
#     challan_data = serializer.data
#     # context = {
#     #     'challan': challan_data 
#     # }
#     combined_items = zip(
#     challan_data.get("InwardChallanGSTDetails", []),
#     challan_data.get("InwardChallanTable", [])    
# )
#     suppliername = challan.SupplierName
#     grn_detail = GrnGenralDetail.objects.filter(SelectSupplier__iexact=suppliername).first()
#     heat_no = grn_detail.HeatNo if grn_detail else None

    
#     table_items = challan_data.get("InwardChallanTable", [])
#     total_qty_no = 0
#     for item in table_items:
#         qty_str = item.get('InQtyNOS')
#         if qty_str:
#         # Remove "Nos", strip whitespace
#             qty_str = qty_str.replace("Nos", "").strip()
#         try:
#             total_qty_no += float(qty_str)
#         except (ValueError, TypeError):
#             pass

#     context = {
#     "challan": challan_data,
#     "items": combined_items,
#     "heat_no": heat_no,
#     "total_qty": total_qty_no

# }


#     # Render HTML
#     template = get_template('inwardchallan_detail.html')
#     html_content = template.render(context)

#     # Convert to PDF
#     pdf_file = HTML(string=html_content).write_pdf()

#     response = HttpResponse(pdf_file, content_type='application/pdf')
#     response['Content-Disposition'] = f'inline; filename="inwardchallan_{pk}.pdf"'
#     return response

# views.py
def generate_inwardchallan_pdf(request, pk):
    challan = get_object_or_404(InwardChallan2, pk=pk)

    serializer = InwardChallanSerializer(challan)
    challan_data = serializer.data
    
    combined_items = zip(
        challan_data.get("InwardChallanGSTDetails", []),
        challan_data.get("InwardChallanTable", [])    
    )
    
    # Get all GRN records with the same gate entry number
    gate_entry_no = challan.GateEntryNo
    grn_details = GrnGenralDetail.objects.filter(GateEntryNo__iexact=gate_entry_no)
    
    print(f"Found {grn_details.count()} GRN records for gate entry: {gate_entry_no}")
    
    # Get all related NewGrnList items for these GRN records
    grn_items = NewGrnList.objects.filter(New_MRN_Detail__in=grn_details)
    
    print(f"Found {grn_items.count()} GRN items")
    
    # Create a mapping of ItemCode and Description to HeatNo
    item_heat_mapping = {}
    description_heat_mapping = {}
    
    for grn_detail in grn_details:
        for grn_item in grn_detail.NewGrnList.all():
            item_code = grn_item.ItemNoCode
            description = grn_item.Description
            heat_no = grn_item.HeatNo
            
            if item_code and heat_no:
                item_heat_mapping[item_code] = heat_no
                print(f"Mapped ItemCode '{item_code}' to HeatNo '{heat_no}'")
            
            if description and heat_no:
                description_heat_mapping[description] = heat_no
                print(f"Mapped Description '{description}' to HeatNo '{heat_no}'")
    
    # Get ItemCodes from inward challan table
    table_items = challan_data.get("InwardChallanTable", [])
    inward_item_codes = []
    
    print("Inward challan table items:")
    for item in table_items:
        print(f"  Item: {item}")
        item_code = item.get('ItemDescription')  # or whatever field contains the item code
        if item_code:
            inward_item_codes.append(item_code)
    
    print(f"Inward challan item codes: {inward_item_codes}")
    
    # Find matching heat numbers - check both ItemCode and Description mappings
    matched_heat_numbers = []
    for item_code in inward_item_codes:
        heat_no = None
        
        # First try to match by ItemCode
        if item_code in item_heat_mapping:
            heat_no = item_heat_mapping[item_code]
            print(f"Found match by ItemCode: '{item_code}' -> HeatNo '{heat_no}'")
        
        # If not found, try to match by Description
        elif item_code in description_heat_mapping:
            heat_no = description_heat_mapping[item_code]
            print(f"Found match by Description: '{item_code}' -> HeatNo '{heat_no}'")
        
        if heat_no:
            matched_heat_numbers.append(heat_no)
    
    # Use the first matched heat number, or combine all if needed
    heat_no = matched_heat_numbers[0] if matched_heat_numbers else None
    
    # If you want all heat numbers as a comma-separated string:
    # heat_no = ", ".join(set(matched_heat_numbers)) if matched_heat_numbers else None
    
    print(f"Final heat_no used: {heat_no}")
    
    # Calculate total quantity
    total_qty_no = 0
    for item in table_items:
        qty_str = item.get('InQtyNOS')
        if qty_str:
            qty_str = qty_str.replace("Nos", "").strip()
            try:
                total_qty_no += float(qty_str)
            except (ValueError, TypeError):
                pass

    context = {
        "challan": challan_data,
        "items": combined_items,
        "heat_no": heat_no,
        "total_qty": total_qty_no,
        "matched_heat_numbers": matched_heat_numbers  # In case you want to show all
    }

    # Render HTML
    template = get_template('inwardchallan_detail.html')
    html_content = template.render(context)

    # Convert to PDF
    pdf_file = HTML(string=html_content).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="inwardchallan_{pk}.pdf"'
    return response




# views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import GrnGenralDetail, NewGrnList
from .serializers import GrnGenralDetailSerializer

@api_view(['GET'])
def get_grn_heat_numbers(request):
    """
    Get heat numbers from GRN records based on part number and/or item code
    
    Query Parameters:
    - part_no: Part number to search for
    - item_code: Item code to search for
    - gate_entry_no: Gate entry number to filter by (optional)
    
    Returns:
    - List of heat numbers with associated item details
    """
    
    part_no = request.GET.get('part_no')
    item_code = request.GET.get('item_code')
    gate_entry_no = request.GET.get('gate_entry_no')
    
    if not part_no and not item_code:
        return Response(
            {"error": "At least one of 'part_no' or 'item_code' parameter is required"}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Build the query
    grn_query = GrnGenralDetail.objects.all()
    
    # Filter by gate entry number if provided
    if gate_entry_no:
        grn_query = grn_query.filter(GateEntryNo__iexact=gate_entry_no)
    
    # Get all GRN records
    grn_details = grn_query.all()
    
    heat_numbers_data = []
    found_items = []
    
    for grn_detail in grn_details:
        # Get all NewGrnList items for this GRN
        grn_items = grn_detail.NewGrnList.all()
        
        for grn_item in grn_items:
            # Check if the item matches the search criteria
            matches = False
            
            # Check part number (assuming it's stored in Description field)
            if part_no and grn_item.Description and part_no.lower() in grn_item.Description.lower():
                matches = True
            
            # Check item code
            if item_code and grn_item.ItemNoCode and item_code.lower() == grn_item.ItemNoCode.lower():
                matches = True
            
            if matches and grn_item.HeatNo:
                item_data = {
                    'grn_no': grn_detail.GrnNo,
                    'gate_entry_no': grn_detail.GateEntryNo,
                    'grn_date': grn_detail.GrnDate,
                    'supplier': grn_detail.SelectSupplier,
                    'item_code': grn_item.ItemNoCode,
                    'description': grn_item.Description,
                    'heat_no': grn_item.HeatNo,
                    'quantity': grn_item.GrnQty,
                    'unit': grn_item.UnitCode,
                    'mfg_date': grn_item.MfgDate,
                    'po_no': grn_item.PoNo
                }
                
                heat_numbers_data.append(item_data)
                found_items.append(grn_item.ItemNoCode)
    
    # Remove duplicates while preserving order
    unique_heat_numbers = []
    seen_heat_nos = set()
    
    for item in heat_numbers_data:
        heat_no = item['heat_no']
        if heat_no not in seen_heat_nos:
            unique_heat_numbers.append(item)
            seen_heat_nos.add(heat_no)
    
    response_data = {
        'search_criteria': {
            'part_no': part_no,
            'item_code': item_code,
            'gate_entry_no': gate_entry_no
        },
        'total_records_found': len(heat_numbers_data),
        'unique_heat_numbers_count': len(unique_heat_numbers),
        'heat_numbers': unique_heat_numbers,
        'all_records': heat_numbers_data  # Include all records for detailed view
    }
    
    return Response(response_data, status=status.HTTP_200_OK)



from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404
from .models import FGMovement
from .serializers import FGMovementSerializer

# class FGMovementListCreateView(ListCreateAPIView):
#     queryset = FGMovement.objects.all()
#     serializer_class = FGMovementSerializer
#     permission_classes = [IsAuthenticated]
    
#     def get_queryset(self):
#         queryset = FGMovement.objects.all()
        
#         # Filter by date range if provided
#         start_date = self.request.query_params.get('start_date')
#         end_date = self.request.query_params.get('end_date')
        
#         if start_date:
#             queryset = queryset.filter(date__gte=start_date)
#         if end_date:
#             queryset = queryset.filter(date__lte=end_date)
        
#         # Filter by item code if provided
#         item_code = self.request.query_params.get('item_code')
#         if item_code:
#             queryset = queryset.filter(fg_item_code__icontains=item_code)
        
#         return queryset

# class FGMovementDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = FGMovement.objects.all()
#     serializer_class = FGMovementSerializer
#     permission_classes = [IsAuthenticated]

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_fg_movement(request):
    """
    Create a new FG Movement entry
    """
    serializer = FGMovementSerializer(data=request.data, context={'request': request})
    
    if serializer.is_valid():
        fg_movement = serializer.save()
        return Response({
            'success': True,
            'message': 'FG Movement created successfully',
            'data': FGMovementSerializer(fg_movement).data
        }, status=status.HTTP_201_CREATED)
    
    return Response({
        'success': False,
        'message': 'Validation error',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_fg_movements(request):
    """
    Get all FG Movements with optional filtering
    """
    try:
        movements = FGMovement.objects.all()
        
        # Apply filters
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        item_code = request.GET.get('item_code')
        
        if start_date:
            movements = movements.filter(date__gte=start_date)
        if end_date:
            movements = movements.filter(date__lte=end_date)
        if item_code:
            movements = movements.filter(fg_item_code__icontains=item_code)
        
        serializer = FGMovementSerializer(movements, many=True)
        
        return Response({
            'success': True,
            'count': movements.count(),
            'data': serializer.data
        })
    
    except Exception as e:
        return Response({
            'success': False,
            'message': f'Error fetching FG movements: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_fg_movement_by_id(request, movement_id):
    """
    Get a specific FG Movement by ID
    """
    try:
        movement = get_object_or_404(FGMovement, id=movement_id)
        serializer = FGMovementSerializer(movement)
        
        return Response({
            'success': True,
            'data': serializer.data
        })
    
    except Exception as e:
        return Response({
            'success': False,
            'message': f'Error fetching FG movement: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_fg_movement(request, movement_id):
    """
    Update an existing FG Movement
    """
    try:
        movement = get_object_or_404(FGMovement, id=movement_id)
        serializer = FGMovementSerializer(movement, data=request.data, partial=True)
        
        if serializer.is_valid():
            updated_movement = serializer.save()
            return Response({
                'success': True,
                'message': 'FG Movement updated successfully',
                'data': FGMovementSerializer(updated_movement).data
            })
        
        return Response({
            'success': False,
            'message': 'Validation error',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response({
            'success': False,
            'message': f'Error updating FG movement: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_fg_movement(request, movement_id):
    """
    Delete an FG Movement
    """
    try:
        movement = get_object_or_404(FGMovement, id=movement_id)
        movement.delete()
        
        return Response({
            'success': True,
            'message': 'FG Movement deleted successfully'
        })
    
    except Exception as e:
        return Response({
            'success': False,
            'message': f'Error deleting FG movement: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Purchase.models import PurchasePO, ItemDetail
from .models import GeneralDetails, ItemDetails
from .serializers import PurchasePOSerializer, ItemDetailSerializer, GSTDetailSerializer
from decimal import Decimal


class GRNQuantityCalculation(APIView):
    def get(self, request, pono):
        try:
            # Fetch PurchasePO by PoNo
            po = PurchasePO.objects.get(PoNo=pono)
            
            # Get all gate entries related to this PO (you might need to add a field to link them)
            # For now, I'll assume you link them by some identifier or manual matching
            gate_entries = GeneralDetails.objects.filter(
                # Add your condition here to link PO with Gate Entry
                 po_reference=pono 
            )
            
            # Serialize PO Item_Detail_Enter
            po_items_serializer = ItemDetailSerializer(po.Item_Detail_Enter.all(), many=True)
            po_items_data = po_items_serializer.data
            
            # Get all gate entry items
            gate_entry_items = []
            for gate_entry in gate_entries:
                gate_items = ItemDetails.objects.filter(Work_Order_detail=gate_entry)
                for gate_item in gate_items:
                    gate_entry_items.append({
                        'ItemNo': gate_item.ItemNo,
                        'Description': gate_item.Description,
                        'Qty_NOS': gate_item.Qty_NOS,
                        'QTY_KG': gate_item.QTY_KG,
                        'Unit_Code': gate_item.Unit_Code,
                        'GE_No': gate_entry.GE_No,
                        'GE_Date': gate_entry.GE_Date,
                        'ChallanNo': gate_entry.ChallanNo,
                        'ChallanDate': gate_entry.ChallanDate
                    })
            
            # Calculate GRN quantities
            grn_items = []
            
            for po_item in po_items_data:
                # Add PoNo and PoDate to each item
                po_item['PoNo'] = po.PoNo
                po_item['PoDate'] = po.PoDate
                
                # Find matching gate entry items (match by ItemNo or Description)
                received_quantity = 0
                received_weight = 0
                matching_gate_entries = []
                
                for gate_item in gate_entry_items:
                    # Match items by ItemNo or Description
                    if (gate_item['ItemNo'] and po_item.get('ItemNo') and 
                        gate_item['ItemNo'].strip().lower() == po_item.get('ItemNo', '').strip().lower()) or \
                       (gate_item['Description'] and po_item.get('Description') and 
                        gate_item['Description'].strip().lower() == po_item.get('Description', '').strip().lower()):
                        
                        # Add to received quantity
                        try:
                            if gate_item['Qty_NOS']:
                                received_quantity += float(gate_item['Qty_NOS'])
                        except (ValueError, TypeError):
                            pass
                        
                        try:
                            if gate_item['QTY_KG']:
                                received_weight += float(gate_item['QTY_KG'])
                        except (ValueError, TypeError):
                            pass
                        
                        matching_gate_entries.append(gate_item)
                
                # Calculate GRN quantity (PO quantity - received quantity)
                po_quantity = float(po_item.get('Qty', 0) or 0)
                grn_quantity = po_quantity - received_quantity
                
                grn_item = {
                    **po_item,  # Include all PO item details
                    'ReceivedQuantity': received_quantity,
                    'ReceivedWeight': received_weight,
                    'GRNQuantity': grn_quantity,
                    'PendingQuantity': max(0, grn_quantity),  # Ensure non-negative
                    'MatchingGateEntries': matching_gate_entries,
                    'Status': 'Completed' if grn_quantity <= 0 else 'Pending'
                }
                
                grn_items.append(grn_item)
            
            # Serialize GST details as before
            gst_details_serializer = GSTDetailSerializer(po.Gst_Details.all(), many=True)
            
            # Prepare summary data
            total_po_items = len(grn_items)
            completed_items = len([item for item in grn_items if item['Status'] == 'Completed'])
            pending_items = total_po_items - completed_items
            
            summary = {
                'TotalPOItems': total_po_items,
                'CompletedItems': completed_items,
                'PendingItems': pending_items,
                'CompletionPercentage': round((completed_items / total_po_items * 100), 2) if total_po_items > 0 else 0
            }
            
            data = {
                "PoNo": po.PoNo,
                "PoDate": po.PoDate,
                "Summary": summary,
                "GRN_Items": grn_items,
                "Gst_Details": gst_details_serializer.data
            }
            
            return Response(data, status=status.HTTP_200_OK)
            
        except PurchasePO.DoesNotExist:
            return Response({"error": "PO not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GRNQuantityByMultiplePOs(APIView):
    """
    Alternative view to handle multiple POs or get GRN data for all pending POs
    """
    def get(self, request):
        try:
            # Get query parameters
            po_numbers = request.query_params.get('po_numbers', '').split(',')
            status_filter = request.query_params.get('status', 'all')  # all, pending, completed
            
            if not po_numbers or po_numbers == ['']:
                # If no specific POs requested, get all POs
                pos = PurchasePO.objects.all()
            else:
                # Filter by specific PO numbers
                pos = PurchasePO.objects.filter(PoNo__in=po_numbers)
            
            all_grn_data = []
            
            for po in pos:
                # Reuse the logic from the single PO view
                try:
                    gate_entries = GeneralDetails.objects.filter(
                        # Add your condition here to link PO with Gate Entry
                    )
                    
                    po_items_serializer = ItemDetailSerializer(po.Item_Detail_Enter.all(), many=True)
                    po_items_data = po_items_serializer.data
                    
                    gate_entry_items = []
                    for gate_entry in gate_entries:
                        gate_items = ItemDetails.objects.filter(Work_Order_detail=gate_entry)
                        for gate_item in gate_items:
                            gate_entry_items.append({
                                'ItemNo': gate_item.ItemNo,
                                'Description': gate_item.Description,
                                'Qty_NOS': gate_item.Qty_NOS,
                                'QTY_KG': gate_item.QTY_KG,
                                'Unit_Code': gate_item.Unit_Code,
                                'GE_No': gate_entry.GE_No,
                                'GE_Date': gate_entry.GE_Date
                            })
                    
                    grn_items = []
                    for po_item in po_items_data:
                        po_item['PoNo'] = po.PoNo
                        po_item['PoDate'] = po.PoDate
                        
                        received_quantity = 0
                        for gate_item in gate_entry_items:
                            if (gate_item['ItemNo'] and po_item.get('ItemNo') and 
                                gate_item['ItemNo'].strip().lower() == po_item.get('ItemNo', '').strip().lower()):
                                try:
                                    if gate_item['Qty_NOS']:
                                        received_quantity += float(gate_item['Qty_NOS'])
                                except (ValueError, TypeError):
                                    pass
                        
                        po_quantity = float(po_item.get('Qty', 0) or 0)
                        grn_quantity = po_quantity - received_quantity
                        
                        grn_item = {
                            **po_item,
                            'ReceivedQuantity': received_quantity,
                            'GRNQuantity': grn_quantity,
                            'Status': 'Completed' if grn_quantity <= 0 else 'Pending'
                        }
                        
                        # Apply status filter
                        if status_filter == 'all' or \
                           (status_filter == 'pending' and grn_item['Status'] == 'Pending') or \
                           (status_filter == 'completed' and grn_item['Status'] == 'Completed'):
                            grn_items.append(grn_item)
                    
                    if grn_items:  # Only add PO if it has items matching the filter
                        po_data = {
                            "PoNo": po.PoNo,
                            "PoDate": po.PoDate,
                            "GRN_Items": grn_items
                        }
                        all_grn_data.append(po_data)
                        
                except Exception as e:
                    continue  # Skip this PO if there's an error
            
            return Response({
                "PurchaseOrders": all_grn_data,
                "TotalPOs": len(all_grn_data)
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import GrnGenralDetail, NewGrnList, GrnGst, GrnGstTDC



# from django.db.models import Sum
# from collections import defaultdict
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404

# @api_view(['GET'])
# def get_grn_data(request, grn_id=None):
#     try:
#         # Fetch GRN items and GST data
#         if grn_id:
#             grn_detail = get_object_or_404(GrnGenralDetail, id=grn_id)
#             grn_items = NewGrnList.objects.filter(New_MRN_Detail=grn_detail)
#             grn_gst = GrnGst.objects.filter(New_MRN_Detail=grn_detail)
#         else:
#             grn_items = NewGrnList.objects.all()
#             grn_gst = GrnGst.objects.all()

#         # Initialize grouped data
#         grouped_data = defaultdict(lambda: {
#             "sr_no": None,
#             "item_code": "",
#             "description": "",
#             "size": "",
#             "group_name": "",
#             "unit_code": "",
#             "item_type": "",
#             "po_rate_qty": "",
#             "rate": "",
#             "qc_stock": "",
#             "f4_stock": "",
#             "stock": 0,
#             "shop_floor": '',
#             "amount": 0,
#             "po_no": "",
#             "date": "",
#             "mfg_date": "",
#             "hsn": "",
#             "po_rate": "",
#             "discount_rate": "",
#             "cgst": "",
#             "sgst": "",
#             "igst": "",
#             "variants": []
#         })

#         for index, item in enumerate(grn_items, 1):
#             gst_data = grn_gst.filter(ItemCode=item.ItemNoCode).first() if grn_gst else None
#             item_master = ItemTable.objects.filter(Part_Code=item.ItemNoCode).first()

#             # Calculate amount
#             try:
#                 rate = float(item.Rate) if item.Rate else 0
#                 qty = float(item.GrnQty) if item.GrnQty else 0
#                 amount = rate * qty
#             except (ValueError, TypeError):
#                 amount = 0

#             # QC stock or normal stock
#             qc_stock_value, stock_value = "", 0
#             if item_master and item_master.QC_Application and item_master.QC_Application.lower() == "yes":
#                 qc_stock_value = item.GrnQty or ""
#             else:
#                 stock_value = float(item.GrnQty or 0)

#             # Shop floor value from MaterialChallanTable
#             shop_floor_value = ""
#             material_challan = MaterialChallan.objects.filter(Item=item.ItemNoCode).first()
#             if material_challan:
#                 challan_table = MaterialChallanTable.objects.filter(MaterialChallanDetail=material_challan).first()
#                 if challan_table:
#                     shop_floor_value = challan_table.Qty or ""

#             # Get group for current item
#             group = grouped_data[item.ItemNoCode]

#             # Initialize group if first occurrence
#             if not group["sr_no"]:
#                 group.update({
#                     "sr_no": index,
#                     "item_code": item.ItemNoCode or '',
#                     "description": item.Description or '',
#                     "unit_code": item.UnitCode or '',
#                     "po_rate_qty": item.PoQty or '',
#                     "rate": item.Rate or '',
#                     "qc_stock": qc_stock_value,
#                     "f4_stock": "",
#                     "stock": 0,
#                     "shop_floor": shop_floor_value,
#                     "amount": amount,
#                     "po_no": item.PoNo or '',
#                     "date": item.Date or '',
#                     "mfg_date": item.MfgDate or '',
#                     "hsn": gst_data.HSN if gst_data else '',
#                     "po_rate": gst_data.PoRate if gst_data else '',
#                     "discount_rate": gst_data.DiscRate if gst_data else '',
#                     "cgst": gst_data.CGST if gst_data else '',
#                     "sgst": gst_data.SGST if gst_data else '',
#                     "igst": gst_data.IGST if gst_data else '',
#                 })

#             # Update total stock
#             group["stock"] += stock_value

#             # ✅ Calculate f4_stock (sum of all onward challan quantities)
#             onward_total = OnwardChallanItem.objects.filter(
#                 item_code__icontains=item.ItemNoCode
#             ).aggregate(total_qty=Sum('qtyNo'))['total_qty'] or 0

#             group["f4_stock"] = format(float(onward_total or group["stock"]), '.2f')

#             # Append variant details
#             group["variants"].append({
#                 "heat_no": item.HeatNo or '',
#                 "stock": str(stock_value),
#                 "grn_qty": item.GrnQty or '',
#                 "challan_qty": item.ChalQty or '',
#                 "short_excess_qty": item.ShortExcessQty or '',
#             })

#         response_data = list(grouped_data.values())

#         return Response({
#             "success": True,
#             "message": "Data fetched successfully",
#             "data": response_data,
#             "total_records": len(response_data)
#         }, status=status.HTTP_200_OK)

#     except Exception as e:
#         return Response({
#             "success": False,
#             "message": f"Error fetching data: {str(e)}",
#             "data": []
#         }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




from collections import defaultdict
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import traceback

from collections import defaultdict
from django.db.models import Q, Sum
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import traceback

@api_view(['GET'])
def get_grn_data(request, grn_id=None):
    try:
        search_query = request.GET.get('q', '').strip()

        # Fetch GRN items and GST data
        if grn_id:
            grn_detail = get_object_or_404(GrnGenralDetail, id=grn_id)
            grn_items = NewGrnList.objects.filter(New_MRN_Detail=grn_detail)
            grn_gst = GrnGst.objects.filter(New_MRN_Detail=grn_detail)
        else:
            grn_items = NewGrnList.objects.all()
            grn_gst = GrnGst.objects.all()

        # Apply search filter
        if search_query:
            grn_items = grn_items.filter(
                Q(ItemNoCode__icontains=search_query) |
                Q(Description__icontains=search_query)
            )

        # Initialize grouped data
        grouped_data = defaultdict(lambda: {
            "sr_no": None,
            "item_code": "",
            "description": "",
            "size": "",
            "group_name": "",
            "unit_code": "",
            "item_type": "",
            "po_rate_qty": "",
            "rate": "",
            "qc_stock": "",
            "f4_stock": "",
            "stock": 0,
            "shop_floor": '',
            "amount": 0,
            "po_no": "",
            "date": "",
            "mfg_date": "",
            "hsn": "",
            "po_rate": "",
            "discount_rate": "",
            "cgst": "",
            "sgst": "",
            "igst": "",
            "variants": []
        })

        for index, item in enumerate(grn_items, 1):
            # Safe fetch of GST & Item data
            gst_data = grn_gst.filter(ItemCode=item.ItemNoCode).first() if grn_gst else None
            item_master = ItemTable.objects.filter(Part_Code=item.ItemNoCode).first()

            # Calculate amount
            try:
                rate = float(item.Rate) if item.Rate else 0
                qty = float(item.GrnQty) if item.GrnQty else 0
                amount = rate * qty
            except (ValueError, TypeError):
                amount = 0

            # QC stock or normal stock
            qc_stock_value, stock_value = "", 0
            if item_master and getattr(item_master, "QC_Application", "").lower() == "yes":
                qc_stock_value = item.GrnQty or ""
            else:
                stock_value = float(item.GrnQty or 0)

            # Shop floor value from MaterialChallanTable
            # shop_floor_value = ""
            # material_challan = MaterialChallan.objects.filter(Item=item.ItemNoCode).first()
            # if material_challan:
            #     challan_table = MaterialChallanTable.objects.filter(
            #         MaterialChallanDetail=material_challan
            #     ).first()
            #     if challan_table:
            #         shop_floor_value = challan_table.Qty or ""

             
            if item.ItemNoCode:
                shop_floor_value = (
                    MaterialChallanTable.objects.filter(
                    MaterialChallanDetail__Item__startswith=item.ItemNoCode
                         ).aggregate(total_qty=Sum('Qty'))['total_qty'] or 0
                    )
            else:
                 shop_floor_value = 0
            
            # Get group for current item
            group = grouped_data[item.ItemNoCode]

            # Initialize group if first occurrence
            if not group["sr_no"]:
                group.update({
                    "sr_no": index,
                    "item_code": item.ItemNoCode or '',
                    "description": item.Description or '',
                    "unit_code": item.UnitCode or '',
                    "po_rate_qty": item.PoQty or '',
                    "rate": item.Rate or '',
                    "qc_stock": qc_stock_value,
                    "f4_stock": "",
                    "stock": 0,
                    "shop_floor": shop_floor_value,
                    "amount": amount,
                    "po_no": item.PoNo or '',
                    "date": item.Date or '',
                    "mfg_date": item.MfgDate or '',
                    "hsn": getattr(gst_data, "HSN", ""),
                    "po_rate": getattr(gst_data, "PoRate", ""),
                    "discount_rate": getattr(gst_data, "DiscRate", ""),
                    "cgst": getattr(gst_data, "CGST", ""),
                    "sgst": getattr(gst_data, "SGST", ""),
                    "igst": getattr(gst_data, "IGST", ""),
                })

            # Update total stock
            group["stock"] += stock_value

            # ✅ F4 Stock Calculation
            onward_total = 0
            inward_total_kg = 0
            if item.ItemNoCode:
                # 1️⃣ Total qty from Onward Challan
                onward_total = (
                    OnwardChallanItem.objects
                    .filter(item_code__icontains=item.ItemNoCode)
                    .aggregate(total_qty=Sum('qtyNo'))['total_qty'] or 0
                )

                # 2️⃣ Total InQtyKg from Inward Challan
                inward_total_kg = (
                    InwardChallanTable.objects
                    .filter(ItemDescription__icontains=item.ItemNoCode)
                    .aggregate(total_in_qty_kg=Sum('InQtyKg'))['total_in_qty_kg'] or 0
                )

                # 3️⃣ Subtract inward qty from onward qty
                final_f4_stock = float(onward_total) - float(inward_total_kg)
            else:
                final_f4_stock = group["stock"]

            group["f4_stock"] = format(final_f4_stock, '.2f')

            # Append variant details
            group["variants"].append({
                "heat_no": item.HeatNo or '',
                "stock": str(stock_value),
                "grn_qty": item.GrnQty or '',
                "challan_qty": item.ChalQty or '',
                "short_excess_qty": item.ShortExcessQty or '',
            })

        # Prepare final list
        response_data = list(grouped_data.values())

        return Response({
            "success": True,
            "message": "Data fetched successfully",
            "data": response_data,
            "total_records": len(response_data)
        }, status=status.HTTP_200_OK)

    except Exception as e:
        print("❌ ERROR in get_grn_data:", e)
        traceback.print_exc()

        return Response({
            "success": False,
            "message": f"Error fetching data: {str(e)}",
            "data": []
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)








# @api_view(['GET'])
# def get_item_variants(request):
#     try:
#         item_code = request.query_params.get("item_code")

#         if not item_code:
#             return Response({
#                 "success": False,
#                 "message": "query param is required",
#                 "data": []
#             }, status=status.HTTP_400_BAD_REQUEST)

#         # Example: "RMRM1001 - 123456 - 18.05 Dai E1MA"
#         try:
#             parts = [p.strip() for p in item_code.split("-")]

#             item_code = parts[0]      #  RMRM1001
#             # heat_no = parts[1]      #  ignore heat filter
#             description = parts[2]    #  18.05 Dai E1MA
#         except Exception:
#             return Response({
#                 "success": False,
#                 "message": "Invalid query format",
#                 "data": []
#             }, status=status.HTTP_400_BAD_REQUEST)

#         # filter only by item_code + description (ignore heat_no)
#         grn_items = NewGrnList.objects.filter(
#             ItemNoCode=item_code,
#             Description=description
#         )

#         if not grn_items.exists():
#             return Response({
#                 "success": True,
#                 "message": "No items found with given filters",
#                 "data": []
#             }, status=status.HTTP_200_OK)

#         response_data = []
#         for item in grn_items:
#             qc_stock, stock = "", ""

#             #  check QC flag
#             item_master = ItemTable.objects.filter(Part_Code=item.ItemNoCode).first()
#             if item_master and item_master.QC_Application and item_master.QC_Application.lower() == "yes":
#                 qc_stock = item.GrnQty or ""
#             else:
#                 stock = item.GrnQty or ""

#             response_data.append({
#                 "heat_no": item.HeatNo or "",  
#                 "stock": stock,
#                 "qc_stock": qc_stock,
#             })

#         return Response({
#             "success": True,
#             "message": "Variants fetched successfully",
#             "data": response_data,
#             "total_records": len(response_data)
#         }, status=status.HTTP_200_OK)

#     except Exception as e:
#         return Response({
#             "success": False,
#             "message": f"Error fetching variants: {str(e)}",
#             "data": []
#         }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_item_variants(request):
    try:
        item_code = request.query_params.get("item_code")

        if not item_code:
            return Response({
                "success": False,
                "message": "query param is required",
                "data": []
            }, status=status.HTTP_400_BAD_REQUEST)

        # Clean and split safely
        parts = [p.strip() for p in item_code.split("-") if p.strip()]

        if len(parts) < 2:
            return Response({
                "success": False,
                "message": "Invalid query format. Expected at least item_code and description.",
                "data": []
            }, status=status.HTTP_400_BAD_REQUEST)

        # Handle both 2-part and 3-part inputs
        if len(parts) == 2:
            item_code = parts[0]           # RMRM1001
            description = parts[1]         # 18.05 Dai E1MA
        elif len(parts) >= 3:
            item_code = parts[0]           # RMRM1001
            description = parts[2]         # 18.05 Dai E1MA (ignore middle heat_no)

        # filter only by item_code + description (ignore heat_no)
        grn_items = NewGrnList.objects.filter(
            ItemNoCode=item_code,
            Description__icontains=description  # allow partial match
        )

        if not grn_items.exists():
            return Response({
                "success": True,
                "message": "No items found with given filters",
                "data": []
            }, status=status.HTTP_200_OK)

        response_data = []
        for item in grn_items:
            qc_stock, stock = "", ""

            # check QC flag
            item_master = ItemTable.objects.filter(Part_Code=item.ItemNoCode).first()
            if item_master and item_master.QC_Application and item_master.QC_Application.lower() == "yes":
                qc_stock = item.GrnQty or ""
            else:
                stock = item.GrnQty or ""

            response_data.append({
                "heat_no": item.HeatNo or "",
                "stock": stock,
                "qc_stock": qc_stock,
            })

        return Response({
            "success": True,
            "message": "Variants fetched successfully",
            "data": response_data,
            "total_records": len(response_data)
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "success": False,
            "message": f"Error fetching variants: {str(e)}",
            "data": []
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
def get_grn_summary(request, grn_id):
    """
    GET API to fetch GRN summary including tax details
    """
    try:
        grn_detail = get_object_or_404(GrnGenralDetail, id=grn_id)
        grn_tdc = GrnGstTDC.objects.filter(New_MRN_Detail=grn_detail).first()
        
        summary_data = {
            'grn_info': {
                'grn_no': grn_detail.GrnNo or '',
                'grn_date': grn_detail.GrnDate or '',
                'grn_time': grn_detail.GrnTime or '',
                'plant': grn_detail.Plant or '',
                'supplier': grn_detail.SelectSupplier or '',
                'po_number': grn_detail.SelectPO or '',
                'challan_no': grn_detail.ChallanNo or '',
                'challan_date': grn_detail.ChallanDate or '',
                'invoice_no': grn_detail.InvoiceNo or '',
                'invoice_date': grn_detail.InvoiceDate or '',
                'vehicle_no': grn_detail.VehicleNo or '',
                'transporter': grn_detail.Transporter or '',
            },
            'tax_details': {
                'assessable_value': float(grn_tdc.assessable_value) if grn_tdc else 0,
                'packing_charges': float(grn_tdc.packing_forwarding_charges) if grn_tdc and grn_tdc.packing_forwarding_charges else 0,
                'transport_charges': float(grn_tdc.transport_charges) if grn_tdc and grn_tdc.transport_charges else 0,
                'insurance': float(grn_tdc.insurance) if grn_tdc and grn_tdc.insurance else 0,
                'cgst': float(grn_tdc.cgst) if grn_tdc else 0,
                'sgst': float(grn_tdc.sgst) if grn_tdc else 0,
                'igst': float(grn_tdc.igst) if grn_tdc else 0,
                'vat': float(grn_tdc.vat) if grn_tdc else 0,
                'cess_amount': float(grn_tdc.cess_amount) if grn_tdc else 0,
                'tds': float(grn_tdc.Tds) if grn_tdc and grn_tdc.Tds else 0,
                'tcs_amount': float(grn_tdc.tcs_amount) if grn_tdc and grn_tdc.tcs_amount else 0,
                'grand_total': float(grn_tdc.grand_total) if grn_tdc else 0,
            } if grn_tdc else {}
        }
        
        return Response({
            'success': True,
            'message': 'GRN summary fetched successfully',
            'data': summary_data
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'success': False,
            'message': f'Error fetching GRN summary: {str(e)}',
            'data': {}
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

#wip stock report
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from collections import defaultdict
from datetime import datetime
import re
from All_Masters.models import ItemTable
import re
from datetime import datetime
from collections import defaultdict
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView




    
import re
from datetime import datetime
from collections import defaultdict
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from collections import defaultdict
from datetime import datetime
import re
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



# class WIPStockreport(APIView):
#     def get_inward_outward_balance(self, fg_part_code, bom_part_code, opno, extra_tokens=None):
#         """
#         Returns outward - inward quantity for the requested part/op pair.
#         Matches either the FG part code or the BOM part code inside challan descriptions.
#         """
#         import re

#         if not bom_part_code and not fg_part_code:
#             return 0.0

#         tokens = set()
#         if fg_part_code:
#             tokens.add(str(fg_part_code).strip().upper())
#         if bom_part_code:
#             tokens.add(str(bom_part_code).strip().upper())
#         if extra_tokens:
#             for token in extra_tokens:
#                 if token:
#                     tokens.add(str(token).strip().upper())

#         tokens.discard("")

#         if not tokens or not opno:
#             return 0.0

#         op_digits = re.search(r"(\d+)", str(opno))
#         target_op = f"OP {op_digits.group(1)}" if op_digits else None

#         def normalize_op(value):
#             if not value:
#                 return None
#             m = re.search(r"(\d+)", str(value))
#             return f"OP {m.group(1)}" if m else None

#         def extract_op(desc):
#             if not desc:
#                 return None
#             m = re.search(r"OP[\s:\-]*?(\d+)", str(desc), re.IGNORECASE)
#             return f"OP {m.group(1)}" if m else None

#         def contains_target(text):
#             if not text:
#                 return False
#             upper_text = str(text).upper()
#             return any(token and token in upper_text for token in tokens)

#         inward_qty = 0.0
#         outward_qty = 0.0

#         inward_qs = InwardChallan2.objects.all()
#         for inv in inward_qs:
#             for row in inv.InwardChallanTable.all():
#                 desc = row.ItemDescription
#                 in_op = extract_op(desc)
#                 if contains_target(desc) and in_op == target_op:
#                     inward_qty += float(row.InQtyNOS or 0)

#         outward_qs = onwardchallan.objects.all()
#         for out in outward_qs:
#             for item in out.items.all():
#                 out_op = (
#                     normalize_op(item.process)
#                     or extract_op(item.description)
#                     or extract_op(item.type)
#                 )

#                 text_matches = (
#                     contains_target(item.item_code)
#                     or contains_target(item.type)
#                     or contains_target(item.description)
#                 )

#                 if not text_matches:
#                     continue

#                 if out_op == target_op or out_op is None:
#                     outward_qty += float(item.qtyNo or 0)

#         balance = outward_qty - inward_qty
#         print("OUTWARD:", outward_qty)
#         print("INWARD:", inward_qty)
#         print("BALANCE:", balance)

#         return balance


    

    
#     def get(self, request):
#         query = request.query_params.get('q', '').strip()
#         if not query:
#             return Response({'error': 'Search query "q" is required'}, status=status.HTTP_400_BAD_REQUEST)

#         # Filter ItemTable using part_code, part_no, or name_description
#         items = ItemTable.objects.filter(
#             Q(Part_Code__icontains=query) |
#             Q(part_no__icontains=query) |
#             Q(Name_Description__icontains=query)
#         )
#         if not items.exists():
#             return Response({'error': 'No items found matching your query'}, status=status.HTTP_404_NOT_FOUND)

#         response_data = []

#         # Totals initialize (these will be recalculated after merge)
#         total_rework_qty = total_reject_qty = total_prod_qty = 0
#         total_pending_qc = total_subcon = total_total = 0

#         for item in items:
#             bom_items = BOMItem.objects.filter(item=item)

#             for bom in bom_items:
#                 if not bom.PartCode or not bom.OPNo:
#                     continue

#                 operation_number = bom.OPNo.strip()   # "20"

#                 production_entries = ProductionEntry.objects.filter(
#                     item__icontains=item.Part_Code,   
#                     operation__startswith=operation_number,                
                                 
#                 )

#                 # Get vendor balance using BOM PartCode (raw material)
    
    
#                 subcon_balance = float(
#                     self.get_inward_outward_balance(
#                         item.Part_Code,
#                         bom.PartCode,
#                         bom.OPNo,
#                         extra_tokens=[item.part_no, item.Name_Description],
#                     ) or 0
#                 )

#                 if not production_entries.exists():
#                     subcon_balance = float(subcon_balance or 0)
#                     wip_wt = float(bom.WipWt or 0)
#                     total = subcon_balance
#                     totalwt = total * wip_wt

#                     response_data.append({
#                         "part_code": item.Part_Code,
#                         "part_no": item.part_no,
#                         "Name_Description": item.Name_Description,
#                         "OPNo": bom.OPNo,
#                         "Operation": bom.Operation,
#                         "PartCode": bom.PartCode,
#                         "rework_qty": 0,
#                         "reject_qty": 0,
#                         "prod_qty": 0,
#                         "Total": total,
#                         "WipWt": wip_wt,
#                         "WipRate": float(bom.WipRate or 0),
#                         "pending_qc": 0,
#                         "subcon": subcon_balance,
#                         "totalwt": totalwt
#                     })
#                 else:
#                     subcon_added_to_total = False
#                     for prod in production_entries:
#                         pending_qc = 0 if getattr(bom, "QC", "").lower() in ["no", "n"] else float(prod.prod_qty or 0)
#                         rework = float(prod.rework_qty or 0)
#                         reject = float(prod.reject_qty or 0)
#                         prod_qty = float(prod.prod_qty or 0)
#                         subcon_balance = float(subcon_balance or 0)

#                         total = rework + reject + prod_qty + pending_qc + subcon_balance
#                         wip_wt = float(bom.WipWt or 0)
#                         totalwt = total * wip_wt

#                         response_data.append({
#                             "part_code": item.Part_Code,
#                             "part_no": item.part_no,
#                             "Name_Description": item.Name_Description,
#                             "OPNo": bom.OPNo,
#                             "Operation": bom.Operation,
#                             "PartCode": bom.PartCode,
#                             "rework_qty": rework,
#                             "reject_qty": reject,
#                             "prod_qty": prod_qty,
#                             "Total": total,
#                             "WipWt": wip_wt,
#                             "WipRate": float(bom.WipRate),
#                             "pending_qc": pending_qc,
#                             "subcon": subcon_balance,
#                             "totalwt": totalwt
#                         })

#                         # (original incremental totals kept but we'll recalc below to ensure correctness)
#                         total_rework_qty += rework
#                         total_reject_qty += reject
#                         total_prod_qty += prod_qty
#                         total_pending_qc += pending_qc
#                         total_total += total

#                         if not subcon_added_to_total:
#                             total_subcon += subcon_balance
#                             subcon_added_to_total = True

#         if not response_data:
#             return Response({'message': 'No matching BOM or production entries found'}, status=status.HTTP_404_NOT_FOUND)

#         # ==========================================
#         # 🔥 MERGE DUPLICATE OPNo ROWS
#         # ==========================================
#         merged = {}

       


#         for row in response_data:
            

#             key = (
#                 row["part_code"],
#                 row["part_no"],
#                 row["Name_Description"],
#                 row["OPNo"],
#                 row["PartCode"]
#             )

#             if key not in merged:
#                 # ensure numeric fields are numbers (not None)
#                 merged[key] = {
#                     **row,
#                     "rework_qty": float(row.get("rework_qty") or 0),
#                     "reject_qty": float(row.get("reject_qty") or 0),
#                     "prod_qty": float(row.get("prod_qty") or 0),
#                     "pending_qc": float(row.get("pending_qc") or 0),
#                     "subcon": float(row.get("subcon") or 0),
#                     "Total": float(row.get("Total") or 0),
#                     "WipWt": float(row.get("WipWt") or 0),
#                     "totalwt": float(row.get("totalwt") or 0),
#                 }
#             else:
#                 # Existing row → Add qty fields
#                 merged[key]["rework_qty"] = (merged[key]["rework_qty"] or 0) + (row.get("rework_qty") or 0)
#                 merged[key]["reject_qty"] = (merged[key]["reject_qty"] or 0) + (row.get("reject_qty") or 0)
#                 merged[key]["prod_qty"] = (merged[key]["prod_qty"] or 0) + (row.get("prod_qty") or 0)
#                 merged[key]["pending_qc"] = (merged[key]["pending_qc"] or 0) + (row.get("pending_qc") or 0)

#                 # subcon should remain the same (do not add again)
#                 # Recalculate Total
#                 merged[key]["Total"] = (
#                     (merged[key]["rework_qty"] or 0)
#                     + (merged[key]["reject_qty"] or 0)
#                     + (merged[key]["prod_qty"] or 0)
#                     + (merged[key]["pending_qc"] or 0)
#                     + (merged[key]["subcon"] or 0)
#                 )

#                 # Recalculate totalwt
#                 merged[key]["totalwt"] = merged[key]["Total"] * float(merged[key].get("WipWt") or 0)

#         # Replace response data with merged rows
#         response_data = list(merged.values())

                

#         # ================================================
#         # 🔥 RECALCULATE TOTAL SUMMARY AFTER MERGE
#         # ================================================
#         # reset totals and recompute from merged data to ensure correctness
#         total_rework_qty = total_reject_qty = total_prod_qty = 0
#         total_pending_qc = total_subcon = total_total = 0

#         for row in response_data:
#             total_rework_qty += row.get("rework_qty") or 0
#             total_reject_qty += row.get("reject_qty") or 0
#             total_prod_qty += row.get("prod_qty") or 0
#             total_pending_qc += row.get("pending_qc") or 0
#             total_total += row.get("Total") or 0

#             # subcon add once per merged OP row
#             total_subcon += row.get("subcon") or 0

#         # =====================================================
#         # 🔥 FINAL RESPONSE
#         # =====================================================
#         return Response({
#             "totals": {
#                 "total_rework": total_rework_qty,
#                 "total_reject": total_reject_qty,
#                 "total_prod": total_prod_qty,
#                 "total_pending_qc": total_pending_qc,
#                 "total_subcon": total_subcon,
#                 "total_total": total_total
#             },
#             "data": response_data
#         }, status=status.HTTP_200_OK)





class WIPStockreport(APIView):

    def get_vendor_balance_from_stock(self, part_code):
        try:
            combined_data = []
            inward_data = []

            def extract_number(value):
                match = re.search(r"[\d.]+", str(value))
                return float(match.group()) if match else 0

            # ================= Inward Challans =================
            inward_queryset = InwardChallan2.objects.all()

            for inward in inward_queryset:
                inward_items = []
                for inv_item in inward.InwardChallanTable.all():

                    item_dict = {
                        "ItemDescription": inv_item.ItemDescription,
                        "ChallanQty": float(extract_number(inv_item.ChallanQty)),
                        "InQtyNOS": float(extract_number(getattr(inv_item, "InQtyNOS", 0))),
                        "ItemCode": None
                    }
                   
                    # pull item code from related GST details
                    gst_detail = getattr(inv_item, "InwardChallanGSTDetails", None)
                    if gst_detail and getattr(gst_detail, "ItemCode", None):
                        item_dict["ItemCode"] = gst_detail.ItemCode

                    inward_items.append(item_dict)

                inward_record = {
                    "id": inward.id,
                    "SupplierName": inward.SupplierName,
                    "ChallanNo": inward.ChallanNo,
                    "ChallanDate": getattr(inward, "InwardDate", None),
                    "items": inward_items
                }
                inward_data.append(inward_record)

            # ================= Outward Challans =================
            outward_queryset = onwardchallan.objects.all().order_by("challan_date")

            # ================= Stock Calculation =================
            last_balance = defaultdict(float)
            grouped_by_date = defaultdict(lambda: defaultdict(lambda: {
                "opening_qty": 0,
                "inward_qty": 0,
                "inward_qty_kg": 0,
                "outward_qty": 0,
                "closing_qty": 0,
                "description": ""
            }))

            # ---- Process inward challans ----
            for inward in inward_data:
                challan_date = inward["ChallanDate"]

                if isinstance(challan_date, str):
                    try:
                        challan_date = datetime.strptime(challan_date, "%Y-%m-%d").date()
                    except Exception:
                        challan_date = None

                supplier_name = inward["SupplierName"]
                for item in inward["items"]:
                    code_key = item["ItemCode"] or item["ItemDescription"].strip().lower()
                    qty = item["ChallanQty"]
                    inqty_kg = item.get("InQtyKg", 0)

                    grouped_by_date[(challan_date, supplier_name)][code_key]["inward_qty"] += qty
                    grouped_by_date[(challan_date, supplier_name)][code_key]["inward_qty_kg"] += inqty_kg
                    grouped_by_date[(challan_date, supplier_name)][code_key]["description"] = item["ItemDescription"]

            # ---- Process outward challans ----
            for outward in outward_queryset:
                challan_date = outward.challan_date

                if isinstance(challan_date, str):
                    try:
                        challan_date = datetime.strptime(challan_date, "%Y-%m-%d").date()
                    except Exception:
                        challan_date = None

                supplier_name = outward.vender
                outward_items = list(
                    outward.items.all().values("description", "qtyNo", "qtyKg", "type", "item_code")
                )
                for item in outward_items:
                    code_key = item["item_code"] or item["description"].strip().lower()
                    qty_value = item.get("qtyKg")
                    if not qty_value:
                        qty_value = item.get("qtyNo", 0)
                    qty = extract_number(qty_value)
                    print("outwardqty==", qty)
                    grouped_by_date[(challan_date, supplier_name)][code_key]["outward_qty"] += qty
                    grouped_by_date[(challan_date, supplier_name)][code_key]["description"] = item["description"]

            # ================= Find balance for specific part_code =================
            part_balance = 0
            clean_part = str(part_code).strip().upper()

            for (date_val, supplier_name), items_dict in sorted(
                grouped_by_date.items(),
                key=lambda x: (x[0][0] or datetime.min.date())
            ):
                for code_key, qtys in items_dict.items():
                    code_key_str = str(code_key).upper()
                    description = str(qtys.get("description", "")).upper()

                    # Match by ItemCode or Description case-insensitively
                    if clean_part in code_key_str or clean_part in description:
                        op_qty = last_balance[code_key]
                        in_qty_kg = qtys["inward_qty_kg"]
                        out_qty = qtys["outward_qty"]
                       
                        # closing = opening + inward - outward
                        closing_qty = op_qty + in_qty_kg - out_qty

                        last_balance[code_key] = closing_qty
                        part_balance = closing_qty  # latest balance
                        
            return round(part_balance, 2)

        except Exception as e:
            print(f"Error getting vendor balance: {e}")
            return 0

    # ========================================================================
    def get(self, request):
        query = request.query_params.get('q', '').strip()
        if not query:
            return Response({'error': 'Search query "q" is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Filter ItemTable using part_code, part_no, or name_description
        items = ItemTable.objects.filter(
            Q(Part_Code__icontains=query) |
            Q(part_no__icontains=query) |
            Q(Name_Description__icontains=query)
        )
        if not items.exists():
            return Response({'error': 'No items found matching your query'}, status=status.HTTP_404_NOT_FOUND)

        response_data = []

        # Totals initialize (these will be recalculated after merge)
        total_rework_qty = total_reject_qty = total_prod_qty = total_pending_qc = total_subcon = total_total = 0

        for item in items:
            bom_items = BOMItem.objects.filter(item=item)

            for bom in bom_items:
                if not bom.PartCode or not bom.OPNo:
                    continue

                operation_number = bom.OPNo.strip()   # "20"

                production_entries = ProductionEntry.objects.filter(
                    item__icontains=item.Part_Code,   
                    operation__startswith=operation_number,                
                #    operation__icontains=bom.OPNo,                    
                )

                # Get vendor balance using BOM PartCode (raw material)
                subcon_balance = self.get_vendor_balance_from_stock(bom.PartCode)

                if not production_entries.exists():
                    subcon_balance = float(subcon_balance or 0)
                    wip_wt = float(bom.WipWt or 0)
                    total = subcon_balance
                    totalwt = total * wip_wt

                    response_data.append({
                        "part_code": item.Part_Code,
                        "part_no": item.part_no,
                        "Name_Description": item.Name_Description,
                        "OPNo": bom.OPNo,
                        "Operation": bom.Operation,
                        "PartCode": bom.PartCode,
                        "rework_qty": 0,
                        "reject_qty": 0,
                        "prod_qty": 0,
                        "Total": total,
                        "WipWt": wip_wt,
                        "WipRate": float(bom.WipRate or 0),
                        "pending_qc": 0,
                        "subcon": subcon_balance,
                        "totalwt": totalwt
                    })
                else:
                    subcon_added_to_total = False
                    for prod in production_entries:
                        pending_qc = 0 if getattr(bom, "QC", "").lower() in ["no", "n"] else float(prod.prod_qty or 0)
                        rework = float(prod.rework_qty or 0)
                        reject = float(prod.reject_qty or 0)
                        prod_qty = float(prod.prod_qty or 0)
                        subcon_balance = float(subcon_balance or 0)

                        total = rework + reject + prod_qty + pending_qc + subcon_balance
                        wip_wt = float(bom.WipWt or 0)
                        totalwt = total * wip_wt

                        response_data.append({
                            "part_code": item.Part_Code,
                            "part_no": item.part_no,
                            "Name_Description": item.Name_Description,
                            "OPNo": bom.OPNo,
                            "Operation": bom.Operation,
                            "PartCode": bom.PartCode,
                            "rework_qty": rework,
                            "reject_qty": reject,
                            "prod_qty": prod_qty,
                            "Total": total,
                            "WipWt": wip_wt,
                            "WipRate": float(bom.WipRate),
                            "pending_qc": pending_qc,
                            "subcon": abs(subcon_balance),
                            "totalwt": totalwt
                        })

                        # (original incremental totals kept but we'll recalc below to ensure correctness)
                        total_rework_qty += rework
                        total_reject_qty += reject
                        total_prod_qty += prod_qty
                        total_pending_qc += pending_qc
                        total_total += total

                        if not subcon_added_to_total:
                            total_subcon += subcon_balance
                            subcon_added_to_total = True

        if not response_data:
            return Response({'message': 'No matching BOM or production entries found'}, status=status.HTTP_404_NOT_FOUND)

        # ==========================================
        # 🔥 MERGE DUPLICATE OPNo ROWS
        # ==========================================
        merged = {}      


        for row in response_data:
            

            key = (
                row["part_code"],
                row["part_no"],
                row["Name_Description"],
                row["OPNo"],
                row["PartCode"]
            )

            if key not in merged:
                # ensure numeric fields are numbers (not None)
                merged[key] = {
                    **row,
                    "rework_qty": float(row.get("rework_qty") or 0),
                    "reject_qty": float(row.get("reject_qty") or 0),
                    "prod_qty": float(row.get("prod_qty") or 0),
                    "pending_qc": float(row.get("pending_qc") or 0),
                    "subcon": float(row.get("subcon") or 0),
                    "Total": float(row.get("Total") or 0),
                    "WipWt": float(row.get("WipWt") or 0),
                    "totalwt": float(row.get("totalwt") or 0),
                }
            else:
                # Existing row → Add qty fields
                merged[key]["rework_qty"] = (merged[key]["rework_qty"] or 0) + (row.get("rework_qty") or 0)
                merged[key]["reject_qty"] = (merged[key]["reject_qty"] or 0) + (row.get("reject_qty") or 0)
                merged[key]["prod_qty"] = (merged[key]["prod_qty"] or 0) + (row.get("prod_qty") or 0)
                merged[key]["pending_qc"] = (merged[key]["pending_qc"] or 0) + (row.get("pending_qc") or 0)

                # subcon should remain the same (do not add again)
                # Recalculate Total
                merged[key]["Total"] = (
                    (merged[key]["rework_qty"] or 0)
                    + (merged[key]["reject_qty"] or 0)
                    + (merged[key]["prod_qty"] or 0)
                    + (merged[key]["pending_qc"] or 0)
                    + (merged[key]["subcon"] or 0)
                )

                # Recalculate totalwt
                merged[key]["totalwt"] = merged[key]["Total"] * float(merged[key].get("WipWt") or 0)

        # Replace response data with merged rows
        response_data = list(merged.values())

                

        # ================================================
        # 🔥 RECALCULATE TOTAL SUMMARY AFTER MERGE
        # ================================================
        # reset totals and recompute from merged data to ensure correctness
        total_rework_qty = total_reject_qty = total_prod_qty = total_pending_qc = total_subcon = total_total = 0

        for row in response_data:
            total_rework_qty += row.get("rework_qty") or 0
            total_reject_qty += row.get("reject_qty") or 0
            total_prod_qty += row.get("prod_qty") or 0
            total_pending_qc += row.get("pending_qc") or 0
            total_total += row.get("Total") or 0

            # subcon add once per merged OP row
            total_subcon += row.get("subcon") or 0

        # =====================================================
        # 🔥 FINAL RESPONSE
        # =====================================================
        return Response({
            "totals": {
                "total_rework": total_rework_qty,
                "total_reject": total_reject_qty,
                "total_prod": total_prod_qty,
                "total_pending_qc": total_pending_qc,
                "total_subcon": total_subcon,
                "total_total": total_total
            },
            "data": response_data
        }, status=status.HTTP_200_OK)


"""
# this is final with out add opno
class WIPStockreport(APIView): 

    def get_vendor_balance_from_stock(self, part_code):
        try:
            combined_data = []
            inward_data = []

            def extract_number(value):
                match = re.search(r"[\d.]+", str(value))
                return float(match.group()) if match else 0

            # ================= Inward Challans =================
            inward_queryset = InwardChallan2.objects.all()

            for inward in inward_queryset:
                inward_items = []
                for inv_item in inward.InwardChallanTable.all():

                    item_dict = {
                        "ItemDescription": inv_item.ItemDescription,  
                        "ChallanQty": float(extract_number(inv_item.ChallanQty)),
                        "InQtyKg": float(extract_number(getattr(inv_item, "InQtyKg", 0))), 
                        "ItemCode": None
                    }

                    # pull item code from related GST details
                    gst_detail = getattr(inv_item, "InwardChallanGSTDetails", None)
                    if gst_detail and getattr(gst_detail, "ItemCode", None):
                        item_dict["ItemCode"] = gst_detail.ItemCode

                    inward_items.append(item_dict)

                inward_record = {
                    "id": inward.id,
                    "SupplierName": inward.SupplierName,
                    "ChallanNo": inward.ChallanNo,
                    "ChallanDate": getattr(inward, "InwardDate", None),
                    "items": inward_items
                }
                inward_data.append(inward_record)

            # ================= Outward Challans =================
            outward_queryset = onwardchallan.objects.all().order_by("challan_date")

            # ================= Stock Calculation =================
            last_balance = defaultdict(float)
            grouped_by_date = defaultdict(lambda: defaultdict(lambda: {
                "opening_qty": 0,
                "inward_qty": 0,
                "inward_qty_kg": 0,
                "outward_qty": 0,
                "closing_qty": 0,
                "description": ""
            }))

            # ---- Process inward challans ----
            for inward in inward_data:
                challan_date = inward["ChallanDate"]

                if isinstance(challan_date, str):
                    try:
                        challan_date = datetime.strptime(challan_date, "%Y-%m-%d").date()
                    except Exception:
                        challan_date = None

                supplier_name = inward["SupplierName"]
                for item in inward["items"]:
                    code_key = item["ItemCode"] or item["ItemDescription"].strip().lower()
                    qty = item["ChallanQty"]
                    inqty_kg = item.get("InQtyKg", 0)

                    grouped_by_date[(challan_date, supplier_name)][code_key]["inward_qty"] += qty
                    grouped_by_date[(challan_date, supplier_name)][code_key]["inward_qty_kg"] += inqty_kg
                    grouped_by_date[(challan_date, supplier_name)][code_key]["description"] = item["ItemDescription"]

            # ---- Process outward challans ----
            for outward in outward_queryset:
                challan_date = outward.challan_date

                if isinstance(challan_date, str):
                    try:
                        challan_date = datetime.strptime(challan_date, "%Y-%m-%d").date()
                    except Exception:
                        challan_date = None

                supplier_name = outward.vender
                outward_items = list(
                    outward.items.all().values("description", "qtyNo", "qtyKg", "type", "item_code")
                )
                for item in outward_items:
                    code_key = item["item_code"] or item["description"].strip().lower()
                    qty_value = item.get("qtyKg")
                    if not qty_value:
                        qty_value = item.get("qtyNo", 0)
                    qty = extract_number(qty_value)
                    grouped_by_date[(challan_date, supplier_name)][code_key]["outward_qty"] += qty
                    grouped_by_date[(challan_date, supplier_name)][code_key]["description"] = item["description"]

            # ================= Find balance for specific part_code =================
            part_balance = 0
            clean_part = str(part_code).strip().upper()

            for (date_val, supplier_name), items_dict in sorted(
                grouped_by_date.items(),
                key=lambda x: (x[0][0] or datetime.min.date())
            ):
                for code_key, qtys in items_dict.items():
                    code_key_str = str(code_key).upper()
                    description = str(qtys.get("description", "")).upper()

                    # ✅ Match by ItemCode or Description case-insensitively
                    if clean_part in code_key_str or clean_part in description:
                        op_qty = last_balance[code_key]
                        in_qty_kg = qtys["inward_qty_kg"]
                        out_qty = qtys["outward_qty"]
                        print(out_qty ,"out")
                        print("inward",in_qty_kg)
                        # ✅ Fixed logic: closing = opening + inward - outward
                        closing_qty = op_qty + in_qty_kg - out_qty

                        last_balance[code_key] = closing_qty
                        part_balance = closing_qty  # latest balance

            return round(part_balance, 2)

        except Exception as e:
            print(f"Error getting vendor balance: {e}")
            return 0

    # ========================================================================
    def get(self, request):
        query = request.query_params.get('q', '').strip()
        if not query:
            return Response({'error': 'Search query "q" is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Filter ItemTable using part_code, part_no, or name_description
        items = ItemTable.objects.filter(
            Q(Part_Code__icontains=query) |
            Q(part_no__icontains=query) |
            Q(Name_Description__icontains=query)
        )
        if not items.exists():
            return Response({'error': 'No items found matching your query'}, status=status.HTTP_404_NOT_FOUND)

        response_data = []

        # Totals initialize
        total_rework_qty = total_reject_qty = total_prod_qty = total_pending_qc = total_subcon = total_total = 0

        for item in items:
            bom_items = BOMItem.objects.filter(item=item)

            for bom in bom_items:
                if not bom.PartCode or not bom.OPNo:
                    continue

                production_entries = ProductionEntry.objects.filter(
                    item__icontains=item.Part_Code,
                    operation__icontains=bom.OPNo
                )

                # ✅ Get vendor balance using BOM PartCode (raw material)
                subcon_balance = self.get_vendor_balance_from_stock(bom.PartCode)

                if not production_entries.exists():
                    subcon_balance = float(subcon_balance or 0)
                    wip_wt = float(bom.WipWt or 0)
                    total = subcon_balance
                    totalwt = total * wip_wt

                    response_data.append({
                        "part_code": item.Part_Code,
                        "part_no": item.part_no,
                        "Name_Description": item.Name_Description,
                        "OPNo": bom.OPNo,
                        "Operation": bom.Operation,
                        "PartCode": bom.PartCode,
                        "rework_qty": None,
                        "reject_qty": None,
                        "prod_qty": None,
                        "Total": subcon_balance,
                        "WipWt": bom.WipWt,
                        "WipRate": bom.WipRate,
                        "pending_qc": 0,
                        "subcon": subcon_balance,
                        "totalwt": totalwt
                    })
                else:
                    subcon_added_to_total = False
                    for prod in production_entries:
                        pending_qc = 0 if getattr(bom, "QC", "").lower() in ["no", "n"] else float(prod.prod_qty or 0)
                        rework = float(prod.rework_qty or 0)
                        reject = float(prod.reject_qty or 0)
                        prod_qty = float(prod.prod_qty or 0)
                        subcon_balance = float(subcon_balance or 0)

                        total = rework + reject + prod_qty + pending_qc + subcon_balance
                        wip_wt = float(bom.WipWt or 0)
                        totalwt = total * wip_wt

                        response_data.append({
                            "part_code": item.Part_Code,
                            "part_no": item.part_no,
                            "Name_Description": item.Name_Description,
                            "OPNo": bom.OPNo,
                            "Operation": bom.Operation,
                            "PartCode": bom.PartCode,
                            "rework_qty": rework,
                            "reject_qty": reject,
                            "prod_qty": prod_qty,
                            "Total": total,
                            "WipWt": wip_wt,
                            "WipRate": float(bom.WipRate),
                            "pending_qc": pending_qc,
                            "subcon": subcon_balance,
                            "totalwt": totalwt
                        })

                        # Update totals
                        total_rework_qty += rework
                        total_reject_qty += reject
                        total_prod_qty += prod_qty
                        total_pending_qc += pending_qc
                        total_total += total

                        if not subcon_added_to_total:
                            total_subcon += subcon_balance
                            subcon_added_to_total = True

        if not response_data:
            return Response({'message': 'No matching BOM or production entries found'}, status=status.HTTP_404_NOT_FOUND)

        return Response({
            "totals": {
                "total_rework": total_rework_qty,
                "total_reject": total_reject_qty,
                "total_prod": total_prod_qty,
                "total_pending_qc": total_pending_qc,
                "total_subcon": total_subcon,
                "total_total": total_total
            },
            "data": response_data
        }, status=status.HTTP_200_OK)

"""



from Sales.models import onwardchallan


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# old h 
# class SubcornStock(APIView):
#     def get(self, request):
#         supplier = request.query_params.get("q")  # optional ?q=TATA
                
#         inward_queryset = InwardChallan2.objects.all()
#         if supplier:
#             inward_queryset = inward_queryset.filter(SupplierName=supplier)

#         combined_data = []
#         for inward in inward_queryset:
#          combined_data.append({
#         "type": "inward",
#         "id": inward.id,
#         "SupplierName": inward.SupplierName,
#         "ChallanNo": inward.ChallanNo,
#         "InwardChallanTable": inward.InwardChallanTable.all().values(
#             "ItemDescription", "ChallanQty"
#         ),
#     })
#         #  Outward Challans
#         outward_queryset = onwardchallan.objects.all()
#         if supplier:
#             outward_queryset = outward_queryset.filter(vender=supplier)

#         for outward in outward_queryset:
#             combined_data.append({
#                 "type": "outward",
#                 "challan_no": outward.challan_no,
#                 "vendor": outward.vender,
#                 "items": list(outward.items.all().values("item_code", "type", "description","qtyNo"))
#             })

#         return Response(combined_data, status=status.HTTP_200_OK)


from collections import defaultdict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import re

def normalize_description(desc):
    match = re.search(r'(\d+\.?\d*\s*Dia\s*[A-Z0-9]+)', desc)
    if match:
        return match.group(1).strip()
    return desc.strip()
#same item description se add ho rha h
class SubcornStock(APIView):
    def get(self, request):
        supplier = request.query_params.get("q")

        # ================= PASS 1 : TOTAL QTY =================
        material_qty = defaultdict(float)

        inward_qs = InwardChallan2.objects.all()
        outward_qs = onwardchallan.objects.all()

        if supplier:
            inward_qs = inward_qs.filter(SupplierName=supplier)
            outward_qs = outward_qs.filter(vender=supplier)

        for inward in inward_qs:
            for item in inward.InwardChallanTable.all():
                material = normalize_description(item.ItemDescription)
                material_qty[material] += float(item.ChallanQty)

        for outward in outward_qs:
            for item in outward.items.all():
                material = normalize_description(item.description)
                material_qty[material] += float(item.qtyNo)

        # ================= PASS 2 : BUILD RESPONSE =================
        combined_data = []
        shown_materials = set()

        # Inward (but only if LAST occurrence is inward)
        for inward in inward_qs:
            inward_items = []

            for item in inward.InwardChallanTable.all():
                material = normalize_description(item.ItemDescription)

                # if this material appears in outward later → skip
                if material in shown_materials:
                    continue

                inward_items.append({
                    "ItemDescription": item.ItemDescription,
                    "ChallanQty": material_qty[material]
                })

                shown_materials.add(material)

            if inward_items:
                combined_data.append({
                    "type": "inward",
                    "id": inward.id,
                    "SupplierName": inward.SupplierName,
                    "ChallanNo": inward.ChallanNo,
                    "InwardChallanTable": inward_items
                })

        # Outward (ALWAYS LAST → overwrite inward)
        for outward in outward_qs:
            items = []

            for item in outward.items.all():
                material = normalize_description(item.description)

                # remove inward entry if exists
                if material in shown_materials:
                    continue

                items.append({
                    "item_code": item.item_code,
                    "type": item.type,
                    "description": item.description,
                    "qtyNo": material_qty[material]
                })

                shown_materials.add(material)

            if items:
                combined_data.append({
                    "type": "outward",
                    "challan_no": outward.challan_no,
                    "vendor": outward.vender,
                    "items": items
                })

        return Response(combined_data, status=status.HTTP_200_OK)



from collections import defaultdict
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import InwardChallanGSTDetails,InwardChallanTable




#-----Matching Itemcode in inward or outward ----
# class VenderStock(APIView):
#     def get(self, request):
#         supplier = request.query_params.get("q")
#         start_date = request.query_params.get("start")
#         end_date = request.query_params.get("end")

#         # Parse dates
#         start_date_obj = end_date_obj = None
#         if start_date and end_date:
#             try:
#                 start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
#                 end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()
#             except ValueError:
#                 return Response(
#                     {"error": "Invalid date format. Use YYYY-MM-DD."},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )

#         combined_data = []
#         inward_data = []

#         # ================= Inward Challans =================
#         inward_queryset = InwardChallan2.objects.all()
#         if supplier:
#             inward_queryset = inward_queryset.filter(SupplierName=supplier)
#         if start_date_obj and end_date_obj:
#             inward_queryset = inward_queryset.filter(
#                 InwardDate__range=[start_date_obj, end_date_obj]
#             )

#         for inward in inward_queryset:
#             inward_items = []
#             for inv_item in inward.InwardChallanTable.all():

#                 def extract_number(value):
#                     match = re.search(r"[\d.]+", str(value))
#                     return float(match.group()) if match else 0

#                 # ================= Get GSTDetails ItemCode =================
#                 gst_details_qs = inward.InwardChallanGSTDetails.filter(
#                     InwardChallanDetail=inward
#                 )
#                 gst_item_code = None
#                 if gst_details_qs.exists():
#                     # For simplicity, pick first related GSTDetail
#                     gst_item_code = gst_details_qs.first().ItemCode

#                 item_dict = {
#                     "ItemDescription": inv_item.ItemDescription,
#                     "ChallanQty": int(extract_number(inv_item.ChallanQty)),
#                     "InQtyKg": float(extract_number(getattr(inv_item, "InQtyKg", 0))),
#                     "ItemCode": gst_item_code,  #  GSTDetails
#                 }

#                 inward_items.append(item_dict)

#             inward_data.append({
#                 "id": inward.id,
#                 "SupplierName": inward.SupplierName,
#                 "ChallanNo": inward.ChallanNo,
#                 "ChallanDate": getattr(inward, "InwardDate", None),
#                 "items": inward_items
#             })

#         # ================= Outward Challans =================
#         outward_queryset = onwardchallan.objects.all()
#         if supplier:
#             outward_queryset = outward_queryset.filter(vender=supplier)
#         if start_date_obj and end_date_obj:
#             outward_queryset = outward_queryset.filter(
#                 challan_date__range=[start_date_obj, end_date_obj]
#             )
#         outward_queryset = outward_queryset.order_by("challan_date")

#         # ================= Stock Calculation =================
#         last_balance = defaultdict(int)
#         grouped_by_date = defaultdict(
#             lambda: defaultdict(
#                 lambda: {
#                     "opening_qty": 0,
#                     "inward_qty": 0,
#                     "outward_qty": 0,
#                     "closing_qty": 0,
#                     "description": "",
#                 }
#             )
#         )

#         # ---- Process inward challans ----
#         for inward in inward_data:
#             challan_date = inward["ChallanDate"]
#             if isinstance(challan_date, str):
#                 try:
#                     challan_date = datetime.strptime(challan_date, "%Y-%m-%d").date()
#                 except Exception:
#                     challan_date = None
#             supplier_name = inward["SupplierName"]

#             for item in inward["items"]:
#                 code_key = (item["ItemCode"] or item["ItemDescription"]).strip().lower()
#                 qty = item["ChallanQty"]
#                 grouped_by_date[(challan_date, supplier_name)][code_key][
#                     "inward_qty"
#                 ] += qty
#                 grouped_by_date[(challan_date, supplier_name)][code_key][
#                     "description"
#                 ] = item["ItemDescription"]

#         # ---- Process outward challans ----
#         for outward in outward_queryset:
#             challan_date = outward.challan_date
#             if isinstance(challan_date, str):
#                 try:
#                     challan_date = datetime.strptime(challan_date, "%Y-%m-%d").date()
#                 except Exception:
#                     challan_date = None
#             supplier_name = outward.vender

#             outward_items = list(
#                 outward.items.all().values("description", "qtyNo", "type", "item_code")
#             )
#             for item in outward_items:
#                 raw_code = item.get("item_code")
#                 #  Use item_code if exists, fallback description
#                 if not raw_code or raw_code.strip() == "" or raw_code.lower() == "default_item":
#                     code_key = item.get("description", "").strip().lower()
#                 else:
#                     code_key = raw_code.strip().lower()

#                 qty = float(item.get("qtyNo") or 0)
#                 grouped_by_date[(challan_date, supplier_name)][code_key][
#                     "outward_qty"
#                 ] += qty
#                 grouped_by_date[(challan_date, supplier_name)][code_key][
#                     "description"
#                 ] = item.get("description", "")

#         # ================= Prepare final combined_data =================
#         for (date_val, supplier_name), items_dict in sorted(
#             grouped_by_date.items(), key=lambda x: (x[0][0] or datetime.min.date())
#         ):
#             day_items = []
#             for code_key, qtys in items_dict.items():
#                 op_qty = last_balance[code_key]
#                 in_qty = qtys["inward_qty"]
#                 out_qty = qtys["outward_qty"]
#                 closing_qty = op_qty - in_qty + out_qty  # Opening + Inward - Outward

#                 last_balance[code_key] = closing_qty

#                 day_items.append(
#                     {
#                         "ItemDescription": qtys.get("description", ""),
#                         "ItemCode": code_key,
#                         "op_qty": op_qty,
#                         "inward_qty": in_qty,
#                         "outward_qty": out_qty,
#                         "balance_qty": closing_qty,
#                     }
#                 )

#             combined_data.append(
#                 {
#                     "date": date_val.isoformat() if date_val else None,
#                     "supplier": supplier_name,
#                     "items": day_items,
#                 }
#             )

#         return Response(combined_data, status=status.HTTP_200_OK)




class VenderStock(APIView):
    def get(self, request):
        supplier = request.query_params.get("q")
        start_date = request.query_params.get("start")
        end_date = request.query_params.get("end")

        # Parse dates
        start_date_obj = end_date_obj = None
        if start_date and end_date:
            try:
                start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
                end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()
            except ValueError:
                return Response(
                    {"error": "Invalid date format. Use YYYY-MM-DD."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        combined_data = []
        inward_data = []

        # ================= Inward Challans =================
        inward_queryset = InwardChallan2.objects.all()
        if supplier:
            inward_queryset = inward_queryset.filter(SupplierName=supplier)
        if start_date_obj and end_date_obj:
            inward_queryset = inward_queryset.filter(
                InwardDate__range=[start_date_obj, end_date_obj]
            )

        for inward in inward_queryset:
            inward_items = []
            for inv_item in inward.InwardChallanTable.all():

                def extract_number(value):
                    match = re.search(r"[\d.]+", str(value))
                    return float(match.group()) if match else 0

                # ================= Get GSTDetails ItemCode =================
                gst_details_qs = inward.InwardChallanGSTDetails.filter(
                    InwardChallanDetail=inward
                )
                gst_item_code = None
                if gst_details_qs.exists():
                    gst_item_code = gst_details_qs.first().ItemCode

                # ✅ Include InQtyKg here
                item_dict = {
                    "ItemDescription": inv_item.ItemDescription,
                    "ChallanQty": int(extract_number(inv_item.ChallanQty)),
                    "InQtyKg": float(extract_number(getattr(inv_item, "InQtyKg", 0))),
                    "ItemCode": gst_item_code,
                }

                inward_items.append(item_dict)

            inward_data.append({
                "id": inward.id,
                "SupplierName": inward.SupplierName,
                "ChallanNo": inward.ChallanNo,
                "ChallanDate": getattr(inward, "InwardDate", None),
                "items": inward_items
            })

        # ================= Outward Challans =================
        outward_queryset = onwardchallan.objects.all()
        if supplier:
            outward_queryset = outward_queryset.filter(vender=supplier)
        if start_date_obj and end_date_obj:
            outward_queryset = outward_queryset.filter(
                challan_date__range=[start_date_obj, end_date_obj]
            )
        outward_queryset = outward_queryset.order_by("challan_date")

        # ================= Stock Calculation =================
        last_balance = defaultdict(int)
        grouped_by_date = defaultdict(
            lambda: defaultdict(
                lambda: {
                    "opening_qty": 0,
                    "inward_qty": 0,
                    "inward_qty_kg": 0,  # ✅ added
                    "outward_qty": 0,
                    "closing_qty": 0,
                    "description": "",
                }
            )
        )

        # ---- Process inward challans ----
        for inward in inward_data:
            challan_date = inward["ChallanDate"]
            if isinstance(challan_date, str):
                try:
                    challan_date = datetime.strptime(challan_date, "%Y-%m-%d").date()
                except Exception:
                    challan_date = None
            supplier_name = inward["SupplierName"]

            for item in inward["items"]:
                code_key = (item["ItemCode"] or item["ItemDescription"]).strip().lower()
                qty = item["ChallanQty"]
                inqty_kg = item.get("InQtyKg", 0)  # ✅ added
                grouped_by_date[(challan_date, supplier_name)][code_key][
                    "inward_qty"
                ] += qty
                grouped_by_date[(challan_date, supplier_name)][code_key][
                    "inward_qty_kg"
                ] += inqty_kg  # ✅ added
                grouped_by_date[(challan_date, supplier_name)][code_key][
                    "description"
                ] = item["ItemDescription"]

        # ---- Process outward challans ----
        for outward in outward_queryset:
            challan_date = outward.challan_date
            if isinstance(challan_date, str):
                try:
                    challan_date = datetime.strptime(challan_date, "%Y-%m-%d").date()
                except Exception:
                    challan_date = None
            supplier_name = outward.vender

            outward_items = list(
                outward.items.all().values("description", "qtyNo", "type", "item_code")
            )
            for item in outward_items:
                raw_code = item.get("item_code")
                if not raw_code or raw_code.strip() == "" or raw_code.lower() == "default_item":
                    code_key = item.get("description", "").strip().lower()
                else:
                    code_key = raw_code.strip().lower()

                qty = float(item.get("qtyNo") or 0)
                grouped_by_date[(challan_date, supplier_name)][code_key][
                    "outward_qty"
                ] += qty
                grouped_by_date[(challan_date, supplier_name)][code_key][
                    "description"
                ] = item.get("description", "")

        # ================= Prepare final combined_data =================
        for (date_val, supplier_name), items_dict in sorted(
            grouped_by_date.items(), key=lambda x: (x[0][0] or datetime.min.date())
        ):
            day_items = []
            for code_key, qtys in items_dict.items():
                op_qty = last_balance[code_key]
                in_qty = qtys["inward_qty"]
                in_qty_kg = qtys["inward_qty_kg"]  # ✅ added
                out_qty = qtys["outward_qty"]
                closing_qty = op_qty - in_qty_kg + out_qty  # Opening + Inward - Outward

                last_balance[code_key] = closing_qty

                # ✅ Include InQtyKg in output
                day_items.append(
                    {
                        "ItemDescription": qtys.get("description", ""),
                        "ItemCode": code_key,
                        "op_qty": op_qty,
                        "inward_qty": in_qty,
                        "InQtyKg": in_qty_kg,  # ✅ added
                        "outward_qty": out_qty,
                        "balance_qty": closing_qty,
                    }
                )

            combined_data.append(
                {
                    "date": date_val.isoformat() if date_val else None,
                    "supplier": supplier_name,
                    "items": day_items,
                }
            )

        return Response(combined_data, status=status.HTTP_200_OK)




from .utils import create_inwardNumber
class generate_unique_inward_number(APIView):
    def get(self, request):
        try:
            inward= create_inwardNumber()
            return Response({"Inward_no" : inward}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
 # You'll create this serializer

# class getbomnewjobwork(APIView):
#     def get(self, request):
#         search_query = request.GET.get('q', '').strip()

#         # Base queryset
#         queryset = NewJobWorkItemDetails.objects.all()

#         # Apply search filter if search_query is provided
#         if search_query:
#             queryset = queryset.filter(
#                 Q(ItemName__icontains=search_query) |
#                 Q(ItemDescription__icontains=search_query)
#             )

#         # Serialize the data
#         serializer = NewJobWorkItemDetailsSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

from django.db.models import Q
from Purchase.models import NewJobWorkItemDetails
from Purchase.serializers import NewJobWorkItemDetailsSerializer 
class getbomnewjobwork(APIView):
    def get(self, request):
        search_query = request.GET.get('q', '').strip()
        queryset = NewJobWorkItemDetails.objects.all()

        # Optional search by ItemName or ItemDescription
        if search_query:
            queryset = queryset.filter(
                Q(ItemName__icontains=search_query) |
                Q(ItemDescription__icontains=search_query)
            )

        result = []

        for item in queryset:
            out_part = str(item.OutAndInPart or "")

            # Extract OP number
            op_match = re.search(r'OP:(\d+)', out_part)
            op_no = op_match.group(1).strip() if op_match else None

            # Extract operation name (e.g., "BLACK PLATING")
            op_split = re.split(r'\|', out_part)
            operation = None
            if len(op_split) >= 3:
                operation = op_split[2].strip()

            # Extract last segment (usually PartCode)
            last_part = None
            if '|' in out_part:
                last_part = out_part.split('|')[-1].strip()
            elif '-' in out_part:
                last_part = out_part.split('-')[-1].strip()

            qtykg = None

            if op_no and operation and last_part:
                # Try matching by PartCode first (most accurate)
                bom_item = BOMItem.objects.filter(
                    OPNo=op_no,
                    Operation__iexact=operation,
                    PartCode__iexact=last_part
                ).first()

                # If not found, try BomPartCode as fallback
                if not bom_item:
                    bom_item = BOMItem.objects.filter(
                        OPNo=op_no,
                        Operation__iexact=operation,
                        BomPartCode__iexact=last_part
                    ).first()

                if bom_item:
                    qtykg = bom_item.QtyKg

            item_data = NewJobWorkItemDetailsSerializer(item).data
            item_data['BOM_QtyKg'] = qtykg
            result.append(item_data)

        return Response(result, status=status.HTTP_200_OK)




# Material_issue_challan_pdf
def generate_materialissue_challan_pdf(request, pk):    
    challan = get_object_or_404(MaterialChallan, pk=pk)    
    
    items = MaterialChallanTable.objects.filter(MaterialChallanDetail=challan)
   
    template = get_template('material_issue_challan.html')  
    html_content = template.render({
        'challan': challan,
        'items': items,
    })

    pdf_file = HTML(string=html_content).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="MaterialIssueChallan_{challan.ChallanNo or pk}.pdf"'
    return response

@api_view(['DELETE'])
def delete_material_challan(request, pk):   
    challan = get_object_or_404(MaterialChallan, pk=pk)
    challan.delete()  
    return Response({'message': f'Material Challan {pk} deleted successfully'}, status=status.HTTP_200_OK)


from .utils import create_inwardNumber
class generate_unique_inward_number(APIView):
    def get(self, request):
        try:
            inward= create_inwardNumber()
            return Response({"Inward_no" : inward}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


from .utils import create_challan_no
class GenerateUniqueChallanNumber(APIView):
    def get(self, request):
        try:
            challan_no = create_challan_no()
            return Response(
                {"challan_no": challan_no},
                status=status.HTTP_200_OK
            )
        except ValueError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": f"Unexpected error: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class GateEntryDeleteAPI(APIView):
    def delete(self,request,gate_id):
        try:
            entry=GeneralDetails.objects.get(id=gate_id)
        except GeneralDetails.DoesNotExist:
            return Response(
                {"error":"gate entry not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        entry.delete()
        return Response(
            {"message":'Gate entry delete successfuly'},
            status=status.HTTP_200_OK
        )



# class EditGrnGenralDetailAPI(APIView):
#     def put(self, request, id):
#         try:
#             grn = GrnGenralDetail.objects.get(id=id)
#         except GrnGenralDetail.DoesNotExist:
#             return Response({"error": "GRN not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = GrnGenralDetailSerializer(grn, data=request.data, partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 "message": "GRN updated successfully",
#                 "data": serializer.data
#             }, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditGrnGenralDetailAPI(APIView):

    # ---------- GET (Fetch data for edit) ----------
    def get(self, request, id):
        try:
            grn = GrnGenralDetail.objects.get(id=id)
        except GrnGenralDetail.DoesNotExist:
            return Response({"error": "GRN not found"}, status=status.HTTP_404_NOT_FOUND)

        # ------ Prepare Items ------
        grn_items = grn.NewGrnList.all()
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

        # ------ Prepare Main GRN Data ------
        data = {
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
            "Items": items_data
        }

        return Response(data, status=status.HTTP_200_OK)

    # ---------- PUT (Update data) ----------
    def put(self, request, id):
        try:
            grn = GrnGenralDetail.objects.get(id=id)
        except GrnGenralDetail.DoesNotExist:
            return Response({"error": "GRN not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = GrnGenralDetailSerializer(grn, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "GRN updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteGrnGenralDetailAPI(APIView):
    def delete(self, request, id):
        try:
            grn = GrnGenralDetail.objects.get(id=id)
        except GrnGenralDetail.DoesNotExist:
            return Response({"error": "GRN not found"}, status=status.HTTP_404_NOT_FOUND)

        grn.delete()
        return Response({"message": "GRN deleted successfully"}, status=status.HTTP_200_OK)
