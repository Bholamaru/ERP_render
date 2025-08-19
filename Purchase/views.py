from rest_framework import generics
from .models import ItemDetail,PoInfo
from All_Masters .models import Supplier_Customer
from All_Masters .models import ItemMaster
from .models import JwPoInfo
from .models import JwItemDetail
from .models import JwShipAdd
from .models import Quote_Comparison_Statement
from .serializers import ItemDetailSerializer,PO_Info_Serializer
from .serializers import Fetch_Supplier_Code_Serializer
from .serializers import Fetch_Item_fields_Serializer
from .serializers import JwPoInfo_Serializer
from .serializers import JwItemDetail_Serializer
from .serializers import JwShipAdd_Serializer
from .serializers import Quote_Comparison_Statement_Serializer
from .serializers import Fetch_PaymentTerm_Serializer
from All_Masters.models import Item

from rest_framework.filters import SearchFilter
from All_Masters.models import Item

# New Purchase Master:- Fetch supplier
class Fetch_Supplier_Code_ListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = Fetch_Supplier_Code_Serializer
    filter_backends = [SearchFilter]
    search_fields = ['Name', 'number']

from All_Masters.models import ItemTable
# New Purchase Master:- Fetch Item Master fields
class Fetch_Item_fields_ListCreate(generics.ListCreateAPIView):
    queryset = ItemTable.objects.all()
    serializer_class = Fetch_Item_fields_Serializer
    filter_backends = [SearchFilter]
    search_fields = ['part_no', 'Part_Code', 'Name_Description']



# New Purchase Master
class ItemDetailListCreate(generics.ListCreateAPIView):
    queryset = ItemDetail.objects.all()
    serializer_class = ItemDetailSerializer

class ItemDetailRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemDetail.objects.all()
    serializer_class = ItemDetailSerializer


# New Purchase Master:- PO Info
class PO_Info_ListCreate(generics.ListCreateAPIView):
    queryset = PoInfo.objects.all()
    serializer_class = PO_Info_Serializer

class PO_Info_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PoInfo.objects.all()
    serializer_class = PO_Info_Serializer

# New JobWork Purchase Order:- Po Info
class JwPoInfo_ListCreate(generics.ListCreateAPIView):
    queryset = JwPoInfo.objects.all()
    serializer_class = JwPoInfo_Serializer

class JwPoInfo_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = JwPoInfo.objects.all()
    serializer_class = JwPoInfo_Serializer


# New JobWork Purchase Order:- ItemDetail
class JwItem_ListCreate(generics.ListCreateAPIView):
    queryset = JwItemDetail.objects.all()
    serializer_class = JwItemDetail_Serializer

class JwItem_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = JwItemDetail.objects.all()
    serializer_class = JwItemDetail_Serializer

# New JobWork Purchase Order:- Ship To Add
class JwShipAdd_ListCreate(generics.ListCreateAPIView):
    queryset = JwShipAdd.objects.all()
    serializer_class = JwShipAdd_Serializer

class JwShipAdd_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = JwShipAdd.objects.all()
    serializer_class = JwShipAdd_Serializer


# New JobWork Purchase Order:- PoInfo Enter Supplier Name to Fetch Payment Term
# class Fetch_PaymentTerm_ListCreate(generics.ListCreateAPIView):
#     queryset = Supplier_Customer.objects.all()
#     serializer_class = Fetch_PaymentTerm_Serializer
#     filter_backends = [SearchFilter]
#     search_fields = ['Payment_Term', 'Name', 'Code_No']

class Fetch_PaymentTerm_ListCreate(generics.ListAPIView):
    queryset = Supplier_Customer.objects.all()
    serializer_class = Fetch_PaymentTerm_Serializer
    filter_backends = [SearchFilter]
    search_fields = ['Name', 'Code_No']

# Quote Comparison:- Quote Comparison Statement
class Quote_Comparison_Statement_ListCreate(generics.ListCreateAPIView):
    queryset = Quote_Comparison_Statement.objects.all()
    serializer_class = Quote_Comparison_Statement_Serializer

class Quote_Comparison_Statement_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote_Comparison_Statement.objects.all()
    serializer_class = Quote_Comparison_Statement_Serializer

##po number

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CodeGenerator
from .serializers import CodeGenerationResponseSerializer
from datetime import datetime

# class GenerateCodeView(APIView):
#     def post(self, request):
#         field = request.data.get('field')
#         user_year = request.data.get('year')

#         # Get the current year (if not provided, use the current year)
#         current_year = int(user_year or datetime.now().year)

#         # Check if field exists in the database
#         code_generator, created = CodeGenerator.objects.get_or_create(
#             field=field, year=current_year,
#             defaults={'last_code': 0}  # If new, start with last_code as 0
#         )

#         # Generate the new code
#         new_code = code_generator.generate_new_code()
#         code_generator.save()

#         response_data = {
#             'message': 'Code generated successfully',
#             'generated_code': new_code
#         }

#         return Response(response_data, status=status.HTTP_200_OK)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CodeGenerator
from .serializers import CodeGenerationResponseSerializer
from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CodeGenerator
from .serializers import CodeGenerationResponseSerializer
from datetime import datetime


class GenerateCodeView(APIView):
    def post(self, request):
        # Extract data from the request
        field = request.data.get('field')
        user_year = request.data.get('year')
        PoNo = request.data.get('PoNo')
        EnquiryNo = request.data.get('EnquiryNo')
        QuotNo = request.data.get('QuotNo')
        PaymentTerms = request.data.get('PaymentTerms')

        # New fields
        DeliveryDate = request.data.get('DeliveryDate')
        AMC_PO = request.data.get('AMC_PO')
        ModeOfShipment = request.data.get('ModeOfShipment')
        PreparedBy = request.data.get('PreparedBy')
        PoNote = request.data.get('PoNote')
        PoSpecification = request.data.get('PoSpecification')
        PoDate = request.data.get('PoDate')
        EnquiryDate = request.data.get('EnquiryDate')
        QuotDate = request.data.get('QuotDate')
        PaymentRemark = request.data.get('PaymentRemark')
        DeliveryType = request.data.get('DeliveryType')
        DeliveryNote = request.data.get('DeliveryNote')
        IndentNo = request.data.get('IndentNo')
        ApprovedBy = request.data.get('ApprovedBy')
        InspectionTerms = request.data.get('InspectionTerms')
        PF_Charges = request.data.get('PF_Charges')
        Time = request.data.get('Time')
        PoFor = request.data.get('PoFor')
        Freight = request.data.get('Freight')
        PoRateType = request.data.get('PoRateType')
        ContactPerson = request.data.get('ContactPerson')
        PoValidityDate = request.data.get('PoValidityDate')
        PoEffectiveDate = request.data.get('PoEffectiveDate')
        TransportName = request.data.get('TransportName')
        PoValidity_WarrantyTerm = request.data.get('PoValidity_WarrantyTerm')
        GstTaxes = request.data.get('GstTaxes')

        # If year is not provided, use the current year
        current_year = int(user_year or datetime.now().year)

        # Get or create the CodeGenerator object
        code_generator, created = CodeGenerator.objects.get_or_create(
            field=field, year=current_year,
            defaults={
                'last_code': 0, 'PoNo': PoNo, 'EnquiryNo': EnquiryNo, 'QuotNo': QuotNo, 'PaymentTerms': PaymentTerms,
                'DeliveryDate': DeliveryDate, 'AMC_PO': AMC_PO, 'ModeOfShipment': ModeOfShipment, 'PreparedBy': PreparedBy,
                'PoNote': PoNote, 'PoSpecification': PoSpecification, 'PoDate': PoDate, 'EnquiryDate': EnquiryDate,
                'QuotDate': QuotDate, 'PaymentRemark': PaymentRemark, 'DeliveryType': DeliveryType, 'DeliveryNote': DeliveryNote,
                'IndentNo': IndentNo, 'ApprovedBy': ApprovedBy, 'InspectionTerms': InspectionTerms, 'PF_Charges': PF_Charges,
                'Time': Time, 'PoFor': PoFor, 'Freight': Freight, 'PoRateType': PoRateType, 'ContactPerson': ContactPerson,
                'PoValidityDate': PoValidityDate, 'PoEffectiveDate': PoEffectiveDate, 'TransportName': TransportName,
                'PoValidity_WarrantyTerm': PoValidity_WarrantyTerm, 'GstTaxes': GstTaxes
            }
        )

        # If the object already exists, update the fields
        if not created:
            code_generator.PoNo = PoNo
            code_generator.EnquiryNo = EnquiryNo
            code_generator.QuotNo = QuotNo
            code_generator.PaymentTerms = PaymentTerms
            code_generator.DeliveryDate = DeliveryDate
            code_generator.AMC_PO = AMC_PO
            code_generator.ModeOfShipment = ModeOfShipment
            code_generator.PreparedBy = PreparedBy
            code_generator.PoNote = PoNote
            code_generator.PoSpecification = PoSpecification
            code_generator.PoDate = PoDate
            code_generator.EnquiryDate = EnquiryDate
            code_generator.QuotDate = QuotDate
            code_generator.PaymentRemark = PaymentRemark
            code_generator.DeliveryType = DeliveryType
            code_generator.DeliveryNote = DeliveryNote
            code_generator.IndentNo = IndentNo
            code_generator.ApprovedBy = ApprovedBy
            code_generator.InspectionTerms = InspectionTerms
            code_generator.PF_Charges = PF_Charges
            code_generator.Time = Time
            code_generator.PoFor = PoFor
            code_generator.Freight = Freight
            code_generator.PoRateType = PoRateType
            code_generator.ContactPerson = ContactPerson
            code_generator.PoValidityDate = PoValidityDate
            code_generator.PoEffectiveDate = PoEffectiveDate
            code_generator.TransportName = TransportName
            code_generator.PoValidity_WarrantyTerm = PoValidity_WarrantyTerm
            code_generator.GstTaxes = GstTaxes
            code_generator.save()

        # Generate the new code
        new_code = code_generator.generate_new_code()
        code_generator.save()

        # Prepare response data
        response_data = {
            'message': 'Code generated successfully',
            'generated_code': new_code
        }

        return Response(response_data, status=status.HTTP_200_OK)



# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CodeGenerator
from datetime import datetime

class GetNextCodeView(APIView):
    def get(self, request):
        # Request se field aur year nikaalna
        field = request.query_params.get('field')
        user_year = request.query_params.get('year')

        # Agar year nahi diya to current year ka use karenge
        current_year = int(user_year or datetime.now().year)

        # Field ko check karke CodeGenerator object ko retrieve karenge
        try:
            code_generator = CodeGenerator.objects.get(field=field, year=current_year)
        except CodeGenerator.DoesNotExist:
            # Agar field aur year ka code generator nahi milta to new create karenge
            code_generator = CodeGenerator.objects.create(field=field, year=current_year, last_code=0)

        # Next code generate karna
        next_code = code_generator.generate_new_code()

        response_data = {
            'message': 'Next code generated successfully',
            'next_code': next_code
        }

        return Response(response_data, status=status.HTTP_200_OK)

#RUD
from rest_framework import generics
from .models import CodeGenerator
from .serializers import RUDSerializer

# List all CodeGenerator records
class CodeGeneratorListView(generics.ListCreateAPIView):
    queryset = CodeGenerator.objects.all()
    serializer_class = RUDSerializer

# View the details of a single CodeGenerator
class CodeGeneratorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CodeGenerator.objects.all()
    serializer_class = RUDSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import NewJobWorkPoInfo
from .serializers import PurchaseOrderSerializer

@api_view(['GET'])
def get_next_job_work_number(request):
    year = request.query_params.get('Shortyear')
    if not year:
        return Response({'error': 'Year parameter is required'}, status=400)
    
    prefix = year
    latest_order = NewJobWorkPoInfo.objects.filter(PoNo__startswith=prefix).order_by('-PoNo').first()
    
    if latest_order:
        last_number = int(latest_order.PoNo[-3:])  # Extract the last 3 digits
        next_number = last_number + 1
    else:
        next_number = 1

    # Ensure the next number is always 6 digits long after the prefix (total length of 9)
    next_PoNo = f"{prefix}{next_number:05d}"
    return Response({'next_PoNo': next_PoNo})


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer

@api_view(['POST'])
def register_purchase_order(request):
    data = request.data
    serializer = PurchaseOrderSerializer(data=data)
    
    if serializer.is_valid():
        # Save the PurchaseOrder to the database
        serializer.save()
        return Response({'message': 'Purchase Order registered successfully!'}, status=201)
    
    return Response(serializer.errors, status=400)


from rest_framework import generics
from .serializers import PurchaseOrderSerializer

# New JW-PO Perfect RUD (Read, Update & Delete)
class RUDpurchase_order(generics.ListAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class RUDpurchase_order_RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


#Purchase:- NewIndent

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PurchaseNewIndent
from .serializers import PurchaseNewIndentSerializer

@api_view(['GET'])
def get_next_PurchaseNewIndent_number(request):
    year = request.query_params.get('Shortyear')
    if not year:
        return Response({'error': 'Year parameter is required'}, status=400)
    
    prefix = year
    latest_order = PurchaseNewIndent.objects.filter(PoNo__startswith=prefix).order_by('-PoNo').first()
    
    if latest_order:
        last_number = int(latest_order.PoNo[-3:])  # Extract the last 3 digits
        next_number = last_number + 1
    else:
        next_number = 1

    # Ensure the next number is always 6 digits long after the prefix (total length of 9)
    next_PoNo = f"{prefix}{next_number:05d}"
    return Response({'next_PoNo': next_PoNo})


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PurchaseNewIndent
from .serializers import PurchaseNewIndentSerializer

@api_view(['POST'])
def register_PurchaseNewIndent(request):
    data = request.data
    serializer = PurchaseNewIndentSerializer(data=data)
    
    if serializer.is_valid():
        # Save the PurchaseOrder to the database
        serializer.save()
        return Response({'message': 'Purchase Order registered successfully!'}, status=201)
    
    return Response(serializer.errors, status=400)


from rest_framework import generics
from .serializers import PurchaseNewIndentSerializer

# New JW-PO Perfect RUD (Read, Update & Delete)
class PurchaseNewIndent_RUD(generics.ListAPIView):
    queryset = PurchaseNewIndent.objects.all()
    serializer_class = PurchaseNewIndentSerializer

class PurchaseNewIndent_RUDeveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseNewIndent.objects.all()
    serializer_class = PurchaseNewIndentSerializer


# views.py

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PurchasePO
from .serializers import OOPurchaseSerializer
from django.db.models import Max
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class RegisterPO(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        data = request.data

        field = data.get('field')
        PoNo = data.get('PoNo')
        EnquiryNo = data.get('EnquiryNo')

        # Validate that required fields are provided
        if not field or not PoNo or not EnquiryNo:
            return Response({'error': 'Field, PoNo, and EnquiryNo are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Extract the year from PoNo (assuming it's the first 4 digits)
        year = PoNo[:4]

        # Get the latest code for the specified field and year
        latest_purchase = PurchasePO.objects.filter(field=field, PoNo__startswith=year).aggregate(Max('PoNo'))
        latest_code = latest_purchase['PoNo__max']

        # Generate next code based on the PoNo format
        if latest_code:
            latest_number = int(latest_code[4:])
            next_code_number = latest_number + 1
        else:
            next_code_number = 1

        next_code = f'{year}{str(next_code_number).zfill(3)}'
        data['PoNo'] = next_code  # Update the PoNo with the generated code

        # Serialize the data and create the PurchasePO
        serializer = OOPurchaseSerializer(data=data)
        if serializer.is_valid():
            purchase = serializer.save(created_by=request.user)  # This will also save the associated purchase_po_details
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # GET method to retrieve all PurchasePO records along with related PurchasePODetails
        po_info = PurchasePO.objects.all()
        serializer = OOPurchaseSerializer(po_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    

########## post delete chaneg hfhhfhfhf
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PurchasePO, GSTDetails, ItemDetailsOther, ScheduleLine, ShipToAdd, ItemDetail
from .serializers import OOPurchaseSerializer
from rest_framework.exceptions import NotFound
from rest_framework.parsers import JSONParser

class PurchasePOView(APIView):
    parser_classes = [JSONParser]

    def get(self, request, pk=None):
        # GET method to retrieve a single or all PurchasePO records
        if pk is not None:
            try:
                po_info = PurchasePO.objects.get(pk=pk)
                serializer = OOPurchaseSerializer(po_info)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except PurchasePO.DoesNotExist:
                raise NotFound(detail="PurchasePO not found with the provided ID")
        
        po_info = PurchasePO.objects.all()
        serializer = OOPurchaseSerializer(po_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        # DELETE method to delete a PurchasePO record by ID (pk)
        try:
            po = PurchasePO.objects.get(pk=pk)
            po.delete()
            return Response({"message": "PurchasePO deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except PurchasePO.DoesNotExist:
            raise NotFound(detail="PurchasePO not found with the provided ID")

    def put(self, request, pk=None):
        # PUT method to update PurchasePO and related tables
        if pk is None:
            return Response({'error': 'ID is required for updating'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            purchase_po = PurchasePO.objects.get(pk=pk)
        except PurchasePO.DoesNotExist:
            raise NotFound("PurchasePO not found with the provided ID")

        # Extract related data from request
        related_fields_data = {
            'Item_Detail_Enter': request.data.pop('Item_Detail_Enter', []),
            'Gst_Details': request.data.pop('Gst_Details', []),
            'Item_Details_Other': request.data.pop('Item_Details_Other', []),
            'Schedule_Line': request.data.pop('Schedule_Line', []),
            'Ship_To_Add': request.data.pop('Ship_To_Add', []),
        }

        # Update main PurchasePO data
        serializer = OOPurchaseSerializer(purchase_po, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Helper function to update or create related objects
        def update_related_objects(m2m_field, model_class, items_data):
            related_manager = getattr(purchase_po, m2m_field)
            related_manager.clear()

            for item_data in items_data:
                if 'id' in item_data:
                    try:
                        obj = model_class.objects.get(id=item_data['id'])
                        for field, value in item_data.items():
                            setattr(obj, field, value)
                        obj.save()
                    except model_class.DoesNotExist:
                        obj = model_class.objects.create(**item_data)
                else:
                    obj = model_class.objects.create(**item_data)

                related_manager.add(obj)

        # Update all related many-to-many fields
        update_related_objects('Item_Detail_Enter', ItemDetail, related_fields_data['Item_Detail_Enter'])
        update_related_objects('Gst_Details', GSTDetails, related_fields_data['Gst_Details'])
        update_related_objects('Item_Details_Other', ItemDetailsOther, related_fields_data['Item_Details_Other'])
        update_related_objects('Schedule_Line', ScheduleLine, related_fields_data['Schedule_Line'])
        update_related_objects('Ship_To_Add', ShipToAdd, related_fields_data['Ship_To_Add'])

        return Response({'message': 'PurchasePO and related data updated successfully'}, status=status.HTTP_200_OK)


class PONextCode(APIView):
    def get(self, request, *args, **kwargs):
        field = request.query_params.get('field')
        year = request.query_params.get('year')

        if not field or not year:
            return Response({'error': 'Field and year are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Get the latest code for the specified field and year
        latest_purchase = PurchasePO.objects.filter(field=field, PoNo__startswith=year).aggregate(Max('PoNo'))
        latest_code = latest_purchase['PoNo__max']

        # Generate next code based on the PoNo format
        if latest_code:
            # Get the numeric part of the latest code and increment it
            latest_number = int(latest_code[4:])
            next_code_number = latest_number + 1
        else:
            next_code_number = 1

        # Format the new code to always be 9 characters
        next_code = f'{year}{str(next_code_number).zfill(5)}'

        return Response({'next_code': next_code}, status=status.HTTP_200_OK)


# Purchase Order list and Pdf

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from num2words import num2words
from .models import PurchasePO
from All_Masters.models import Item as Item2

def generate_item_pdf(request, pk):
    po = get_object_or_404(PurchasePO, pk=pk)

    item = Item2.objects.filter(number=po.CodeNo).first()

    item_details = list(po.Item_Detail_Enter.all())
    gst_details = list(po.Gst_Details.all())
    combined_details = list(zip(item_details, gst_details))

    # ✅ Calculate total GST sum instead of using po.GR_Total
    total_gst_sum = sum([gst.Total for gst in gst_details if gst.Total is not None])

    # ✅ Convert GST sum to words
    integer_part = int(total_gst_sum)
    words = num2words(integer_part, lang='en_IN').title()
    gr_total_in_words = f"Rs. {words} Only"

    template = get_template('Purchase-order.html')
    context = {
        'po': po,
        'item': item,
        'item_details': item_details,
        'gst_details': gst_details,
        'combined_details': combined_details,
        'other_details': po.Item_Details_Other.all(),
        'schedule_lines': po.Schedule_Line.all(),
        'ship_to_addresses': po.Ship_To_Add.all(),
        'gr_total_in_words': gr_total_in_words,
        'total_gst_sum': total_gst_sum,  # ✅ new context variable
    }

    html_content = template.render(context)
    pdf_file = HTML(string=html_content).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="purchase_po_{pk}.pdf"'
    return response






from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ItemDetail
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class ItemDetailAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        queryset = PurchasePO.objects.all()

        # Optionally, filter or search based on parameters
        item_search = request.GET.get("ItemSearch", "")
        if item_search:
            queryset = queryset.filter(Item__icontains=item_search)

        # Build response data
        data = []
        for item in queryset:
            data.append({
                "id": item.id,
                "Plant": item.Plant,
                "PoNo": item.PoNo,
                "PoDate": item.PoDate,
                "Type": item.Type,
                "CodeNo": item.CodeNo,
                "Supplier": item.Supplier,
                "User": item.created_by.username if item.created_by else None,
                "View": f"/Purchase/PoOrder/pdf/{item.id}/",   # PDF view link
                "Edit": f"/Purchase/RegisterPO_All_Series/{item.id}/",  # API edit link
            })

        return Response(data)


#############testing
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from All_Masters.models import Item, TaxDetails
from .models import MYDetail
from django.core.exceptions import ObjectDoesNotExist

class AddItemDetail(APIView):
    def post(self, request):
        try:
            # Extract data from request body
            item_data = request.data

            # Fetch supplier's GST_Tax_Code and HSN/SAC Code from related tables
            supplier = Item.objects.get(number=item_data['number'])
            gst_tax_code = supplier.GST_Tax_Code
            tax_details = TaxDetails.objects.get(HSN_SAC_Code=item_data['HSN_SAC_Code'])

            # Construct Item field dynamically based on GST_Tax_Code
            if gst_tax_code == "CGST+SGST":
                item = f"{item_data['Item']} HSN {item_data['HSN_SAC_Code']} CGST : {tax_details.CGST} SGST : {tax_details.SGST}"
            elif gst_tax_code == "IGST":
                item = f"{item_data['Item']} HSN {item_data['HSN_SAC_Code']} IGST : {tax_details.IGST}"
            elif gst_tax_code == "UTGST":
                item = f"{item_data['Item']} HSN {item_data['HSN_SAC_Code']} UTGST : {tax_details.UTGST}"
            else:
                item = f"{item_data['Item']} HSN {item_data['HSN_SAC_Code']} Tax Code: {gst_tax_code}"

            # Validate and convert input values
            original_rate = float(item_data['Rate']) if item_data.get('Rate') else 0.0
            discount = float(item_data['Disc']) if item_data.get('Disc') else 0.0
            qty = int(item_data['Qty']) if item_data.get('Qty') else 0

            # Calculate necessary values
            subtotal = original_rate * qty
            disc_rate = original_rate * (1 - (discount / 100)) if discount > 0 else original_rate
            
            # Determine GST rates based on the constructed item
            if "IGST" in item:
                cgst_rate = 0
                sgst_rate = 0
                igst_rate = tax_details.IGST
            else:
                cgst_rate = tax_details.CGST
                sgst_rate = tax_details.SGST
                igst_rate = 0

            # Ensure that CGST, SGST, IGST rates are treated as floats
            cgst_rate = float(cgst_rate)
            sgst_rate = float(sgst_rate)
            igst_rate = float(igst_rate)

            # Calculate GST amounts
            cgst_amt = disc_rate * (cgst_rate / 100)
            sgst_amt = disc_rate * (sgst_rate / 100)
            igst_amt = disc_rate * (igst_rate / 100)
            total_amount = disc_rate + cgst_amt + sgst_amt + igst_amt

            # Save the item details to the database
            item_detail = MYDetail(
                Item=item,
                ItemDescription=item_data['ItemDescription'],
                ItemSize=item_data['ItemSize'],
                Rate=original_rate,  # Save the original rate
                Disc=item_data['Disc'],
                Qty=qty,
                Unit=item_data['Unit'],
                Particular=item_data['Particular'],
                Mill_Name=item_data['Mill_Name'],
                DeliveryDt=item_data['DeliveryDt']
            )
            item_detail.save()

            # Build response data including Schedule_Line
            response_data = {
                'id': item_detail.id,
                'Item': item_detail.Item,
                'ItemDescription': item_detail.ItemDescription,
                'ItemSize': item_detail.ItemSize,
                'Rate': str(original_rate),
                'Disc': str(discount),
                'Qty': str(qty),
                'Unit': item_detail.Unit,
                'Particular': item_detail.Particular,
                'Mill_Name': item_detail.Mill_Name,
                'DeliveryDt': item_detail.DeliveryDt,
                'Schedule_Line': [
                    {
                        'Item': item_data['Item'],
                        'ItemDescription': item_data['ItemDescription'],
                        'Qty': str(qty)
                    }
                ],
                'GST_Details': {
                    'Item': item_data['Item'],
                    'HSN': item_data['HSN_SAC_Code'],
                    'Rate': str(original_rate),
                    'Qty': str(qty),
                    'SubTotal': f"{subtotal:.1f}",
                    'Disc': str(discount),
                    'Packing': "",
                    'Transport': "",
                    'TotalAmount': f"{total_amount:.2f}",
                    'DiscRate': f"{disc_rate:.2f}",
                    'CGST': {
                        'Rate': str(cgst_rate),
                        'Amt': f"{cgst_amt:.2f}"
                    },
                    'SGST': {
                        'Rate': str(sgst_rate),
                        'Amt': f"{sgst_amt:.2f}"
                    },
                    'IGST': {
                        'Rate': str(igst_rate),
                        'Amt': f"{igst_amt:.2f}"
                    },
                    'Vat': {
                        'Rate': "",
                        'Amt': ""
                    },
                    'Cess': {
                        'Rate': "",
                        'Amt': ""
                    },
                    'Total': f"{total_amount:.2f}"
                }
            }

            return Response({'message': 'Data saved successfully', 'data': response_data}, status=status.HTTP_201_CREATED)

        except ObjectDoesNotExist:
            return Response({'message': 'Supplier or HSN not found'}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as ve:
            return Response({'message': str(ve)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# class GetItemDetails(APIView):
#     def get(self, request):
#         try:
#             item_details = MYDetail.objects.all()
#             response_data = []

#             for item in item_details:
#                 # Extract values
#                 original_rate = float(item.Rate) if item.Rate else 0.0
#                 discount = float(item.Disc) if item.Disc else 0.0
#                 qty = int(item.Qty) if item.Qty else 0

#                 # Calculate necessary values
#                 subtotal = original_rate * qty
#                 disc_rate = original_rate * (1 - (discount / 100)) if discount > 0 else original_rate
                
#                 # Determine GST rates based on the constructed item
#                 if "IGST" in item.Item:
#                     cgst_rate = 0
#                     sgst_rate = 0
#                     igst_rate = 18  # Assuming IGST is 18% for example
#                 else:
#                     cgst_rate = 9  # Assuming CGST is 9%
#                     sgst_rate = 9  # Assuming SGST is 9%
#                     igst_rate = 0

#                 # Ensure that CGST, SGST, IGST rates are treated as floats
#                 cgst_rate = float(cgst_rate)
#                 sgst_rate = float(sgst_rate)
#                 igst_rate = float(igst_rate)

#                 # Calculate GST amounts
#                 cgst_amt = disc_rate * (cgst_rate / 100)
#                 sgst_amt = disc_rate * (sgst_rate / 100)
#                 igst_amt = disc_rate * (igst_rate / 100)
#                 total_amount = disc_rate + cgst_amt + sgst_amt + igst_amt

#                 # Prepare GST details
#                 gst_details = {
#                     "Item": item.Item.split(" ")[0],
#                     "HSN": item.Item.split(" ")[2],
#                     "Rate": str(original_rate),
#                     "Qty": str(qty),
#                     "SubTotal": f"{subtotal:.1f}",
#                     "Disc": str(discount),
#                     "Packing": "",
#                     "Transport": "",
#                     "TotalAmount": f"{total_amount:.2f}",
#                     "DiscRate": f"{disc_rate:.2f}",
#                     "CGST": {
#                         "Rate": str(cgst_rate),
#                         "Amt": f"{cgst_amt:.2f}"
#                     },
#                     "SGST ": {
#                         "Rate": str(sgst_rate),
#                         "Amt": f"{sgst_amt:.2f}"
#                     },
#                     "IGST": {
#                         "Rate": str(igst_rate),
#                         "Amt": f"{igst_amt:.2f}"
#                     },
#                     "Vat": {
#                         "Rate": "",
#                         "Amt": ""
#                     },
#                     "Cess": {
#                         "Rate": "",
#                         "Amt": ""
#                     },
#                     "Total": f"{total_amount:.2f}"
#                 }

#                 # Prepare the schedule line
#                 schedule_line = [
#                     {
#                         'Item': item.Item.split(" ")[0],
#                         'ItemDescription': item.ItemDescription,
#                         'Qty': str(qty)
#                     }
#                 ]

#                 # Append formatted data
#                 formatted_item = {
#                     'id': item.id,
#                     'Item': item.Item,
#                     'ItemDescription': item.ItemDescription,
#                     'ItemSize': item.ItemSize,
#                     'Rate': str(original_rate),
#                     'Disc': str(discount),
#                     'Qty': str(qty),
#                     'Unit': item.Unit,
#                     'Particular': item.Particular,
#                     'Mill_Name': item.Mill_Name,
#                     'DeliveryDt': item.DeliveryDt,
#                     'Schedule_Line': schedule_line,
#                     'GST_Details': gst_details
#                 }
#                 response_data.append(formatted_item)

#             return Response({'message': 'Data retrieved successfully', 'ItemDetails': response_data}, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# class GetItemDetails(APIView):
#     def get(self, request, id):
#         try:
#             # Fetch the item detail by ID
#             item_detail = MYDetail.objects.get(id=id)

#             # Prepare the response data similar to the GET method you already implemented
#             original_rate = float(item_detail.Rate) if item_detail.Rate else 0.0
#             discount = float(item_detail.Disc) if item_detail.Disc else 0.0
#             qty = int(item_detail.Qty) if item_detail.Qty else 0

#             subtotal = original_rate * qty
#             disc_rate = original_rate * (1 - (discount / 100)) if discount > 0 else original_rate
            
#             if "IGST" in item_detail.Item:
#                 cgst_rate = 0
#                 sgst_rate = 0
#                 igst_rate = 18
#             else:
#                 cgst_rate = 9
#                 sgst_rate = 9
#                 igst_rate = 0

#             cgst_amt = disc_rate * (cgst_rate / 100)
#             sgst_amt = disc_rate * (sgst_rate / 100)
#             igst_amt = disc_rate * (igst_rate / 100)
#             total_amount = disc_rate + cgst_amt + sgst_amt + igst_amt

#             response_data = {
#                 'id': item_detail.id,
#                 'Item': item_detail.Item,
#                 'ItemDescription': item_detail.ItemDescription,
#                 'ItemSize': item_detail.ItemSize,
#                 'Rate': str(original_rate),
#                 'Disc': str(discount),
#                 'Qty': str(qty),
#                 'Unit': item_detail.Unit,
#                 'Particular': item_detail.Particular,
#                 'Mill_Name': item_detail.Mill_Name,
#                 'DeliveryDt': item_detail.DeliveryDt,
#                 'GST_Details': {
#                     'Item': item_detail.Item.split(" ")[0],
#                     'HSN': item_detail.Item.split(" ")[2],
#                     'Rate': str(original_rate),
#                     'Qty': str(qty),
#                     'SubTotal': f"{subtotal:.1f}",
#                     'Disc': str(discount),
#                     'TotalAmount': f"{total_amount:.2f}",
#                     'DiscRate': f"{disc_rate:.2f}",
#                     'CGST': {'Rate': str(cgst_rate), 'Amt': f"{cgst_amt:.2f}"},
#                     'SGST': {'Rate': str(sgst_rate), 'Amt': f"{sgst_amt:.2f}"},
#                     'IGST': {'Rate': str(igst_rate), 'Amt': f"{igst_amt:.2f}"},
#                     'Total': f"{total_amount:.2f}"
#                 }
#             }
#             return Response({'message': 'Data retrieved successfully', 'data': response_data}, status=status.HTTP_200_OK)
        
#         except MYDetail.DoesNotExist:
#             return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, id):
#         try:
#             # Fetch the existing item detail by ID
#             item_detail = MYDetail.objects.get(id=id)

#             # Get the updated data from the request
#             updated_data = request.data

#             # Update fields dynamically
#             item_detail.ItemDescription = updated_data.get('ItemDescription', item_detail.ItemDescription)
#             item_detail.ItemSize = updated_data.get('ItemSize', item_detail.ItemSize)
#             item_detail.Rate = float(updated_data.get('Rate', item_detail.Rate))
#             item_detail.Disc = float(updated_data.get('Disc', item_detail.Disc))
#             item_detail.Qty = int(updated_data.get('Qty', item_detail.Qty))
#             item_detail.Unit = updated_data.get('Unit', item_detail.Unit)
#             item_detail.Particular = updated_data.get('Particular', item_detail.Particular)
#             item_detail.Mill_Name = updated_data.get('Mill_Name', item_detail.Mill_Name)
#             item_detail.DeliveryDt = updated_data.get('DeliveryDt', item_detail.DeliveryDt)

#             # Save the updated item details
#             item_detail.save()

#             return Response({'message': 'Data updated successfully', 'data': item_detail.id}, status=status.HTTP_200_OK)
#         except MYDetail.DoesNotExist:
#             return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         try:
#             # Fetch the item detail by ID
#             item_detail = MYDetail.objects.get(id=id)

#             # Delete the item detail
#             item_detail.delete()

#             return Response({'message': 'Data deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
#         except MYDetail.DoesNotExist:
#             return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetItemDetails(APIView):
    def get(self, request, id=None):
        try:
            if id:  # If an id is provided, fetch the specific item
                item_detail = MYDetail.objects.get(id=id)

                # Prepare the response data similar to your previous GET method
                original_rate = float(item_detail.Rate) if item_detail.Rate else 0.0
                discount = float(item_detail.Disc) if item_detail.Disc else 0.0
                qty = int(item_detail.Qty) if item_detail.Qty else 0

                subtotal = original_rate * qty
                disc_rate = original_rate * (1 - (discount / 100)) if discount > 0 else original_rate
                
                if "IGST" in item_detail.Item:
                    cgst_rate = 0
                    sgst_rate = 0
                    igst_rate = 18
                else:
                    cgst_rate = 9
                    sgst_rate = 9
                    igst_rate = 0

                cgst_amt = disc_rate * (cgst_rate / 100)
                sgst_amt = disc_rate * (sgst_rate / 100)
                igst_amt = disc_rate * (igst_rate / 100)
                total_amount = disc_rate + cgst_amt + sgst_amt + igst_amt

                response_data = {
                    'id': item_detail.id,
                    'Item': item_detail.Item,
                    'ItemDescription': item_detail.ItemDescription,
                    'ItemSize': item_detail.ItemSize,
                    'Rate': str(original_rate),
                    'Disc': str(discount),
                    'Qty': str(qty),
                    'Unit': item_detail.Unit,
                    'Particular': item_detail.Particular,
                    'Mill_Name': item_detail.Mill_Name,
                    'DeliveryDt': item_detail.DeliveryDt,
                    'GST_Details': {
                        'Item': item_detail.Item.split(" ")[0],
                        'HSN': item_detail.Item.split(" ")[2],
                        'Rate': str(original_rate),
                        'Qty': str(qty),
                        'SubTotal': f"{subtotal:.1f}",
                        'Disc': str(discount),
                        'TotalAmount': f"{total_amount:.2f}",
                        'DiscRate': f"{disc_rate:.2f}",
                        'CGST': {'Rate': str(cgst_rate), 'Amt': f"{cgst_amt:.2f}"},
                        'SGST': {'Rate': str(sgst_rate), 'Amt': f"{sgst_amt:.2f}"},
                        'IGST': {'Rate': str(igst_rate), 'Amt': f"{igst_amt:.2f}"},
                        'Total': f"{total_amount:.2f}"
                    }
                }
                return Response({'message': 'Data retrieved successfully', 'data': response_data}, status=status.HTTP_200_OK)

            # If no id is provided, fetch all items
            item_details = MYDetail.objects.all()
            response_data = []

            for item in item_details:
                # Prepare the response data for each item
                original_rate = float(item.Rate) if item.Rate else 0.0
                discount = float(item.Disc) if item.Disc else 0.0
                qty = int(item.Qty) if item.Qty else 0

                subtotal = original_rate * qty
                disc_rate = original_rate * (1 - (discount / 100)) if discount > 0 else original_rate
                
                if "IGST" in item.Item:
                    cgst_rate = 0
                    sgst_rate = 0
                    igst_rate = 18
                else:
                    cgst_rate = 9
                    sgst_rate = 9
                    igst_rate = 0

                cgst_amt = disc_rate * (cgst_rate / 100)
                sgst_amt = disc_rate * (sgst_rate / 100)
                igst_amt = disc_rate * (igst_rate / 100)
                total_amount = disc_rate + cgst_amt + sgst_amt + igst_amt

                response_data.append({
                    'id': item.id,
                    'Item': item.Item,
                    'ItemDescription': item.ItemDescription,
                    'ItemSize': item.ItemSize,
                    'Rate': str(original_rate),
                    'Disc': str(discount),
                    'Qty': str(qty),
                    'Unit': item.Unit,
                    'Particular': item.Particular,
                    'Mill_Name': item.Mill_Name,
                    'DeliveryDt': item.DeliveryDt,
                    'GST_Details': {
                        'Item': item.Item.split(" ")[0],
                        'HSN': item.Item.split(" ")[2],
                        'Rate': str(original_rate),
                        'Qty': str(qty),
                        'SubTotal': f"{subtotal:.1f}",
                        'Disc': str(discount),
                        'TotalAmount': f"{total_amount:.2f}",
                        'DiscRate': f"{disc_rate:.2f}",
                        'CGST': {'Rate': str(cgst_rate), 'Amt': f"{cgst_amt:.2f}"},
                        'SGST': {'Rate': str(sgst_rate), 'Amt': f"{sgst_amt:.2f}"},
                        'IGST': {'Rate': str(igst_rate), 'Amt': f"{igst_amt:.2f}"},
                        'Total': f"{total_amount:.2f}"
                    }
                })

            return Response({'message': 'Data retrieved successfully', 'ItemDetails': response_data}, status=status.HTTP_200_OK)
        
        except MYDetail.DoesNotExist:
            return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            # Fetch the existing item detail by ID
            item_detail = MYDetail.objects.get(id=id)

            # Get the updated data from the request
            updated_data = request.data

            # Update fields dynamically
            item_detail.ItemDescription = updated_data.get('ItemDescription', item_detail.ItemDescription)
            item_detail.ItemSize = updated_data.get('ItemSize', item_detail.ItemSize)
            item_detail.Rate = float(updated_data.get('Rate', item_detail.Rate))
            item_detail.Disc = float(updated_data.get('Disc', item_detail.Disc))
            item_detail.Qty = int(updated_data.get('Qty', item_detail.Qty))
            item_detail.Unit = updated_data.get('Unit', item_detail.Unit)
            item_detail.Particular = updated_data.get('Particular', item_detail.Particular)
            item_detail.Mill_Name = updated_data.get('Mill_Name', item_detail.Mill_Name)
            item_detail.DeliveryDt = updated_data.get('DeliveryDt', item_detail.DeliveryDt)

            # Save the updated item details
            item_detail.save()

            return Response({'message': 'Data updated successfully', 'data': item_detail.id}, status=status.HTTP_200_OK)
        except MYDetail.DoesNotExist:
            return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            # Fetch the item detail by ID
            item_detail = MYDetail.objects.get(id=id)

            # Delete the item detail
            item_detail.delete()

            return Response({'message': 'Data deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except MYDetail.DoesNotExist:
            return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

# New Indent
from rest_framework import viewsets
from .models import Indent
from .serializers import IndentSerializer

class IndentViewSet(viewsets.ModelViewSet):
    queryset = Indent.objects.all()
    serializer_class = IndentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max
from .models import Indent

class GetNextIndentNo(APIView):
    def get(self, request, *args, **kwargs):
        year = request.GET.get('year', None)

        if not year:
            return Response({"error": "Year is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            year = int(year)
        except ValueError:
            return Response({"error": "Invalid year format"}, status=status.HTTP_400_BAD_REQUEST)

        prefix = f"{year}"
        latest_indent = Indent.objects.filter(IndentNo__startswith=f"IND {prefix}").aggregate(Max('IndentNo'))

        if latest_indent['IndentNo__max']:
            last_code = latest_indent['IndentNo__max']
            number_part = int(last_code[len(f"IND {prefix}"):])  # Extract trailing number
            next_code_number = number_part + 1
        else:
            next_code_number = 1

        next_code_number_str = f"{next_code_number:05d}"
        next_indent_no = f"IND {prefix}{next_code_number_str}"

        return Response({"next_IndentNo": next_indent_no}, status=status.HTTP_200_OK)

from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from .models import Indent
from .serializers import IndentSerializer

class IndentDetailAPIView(generics.ListAPIView):
    queryset = Indent.objects.all()
    serializer_class = IndentSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []
        for indent in queryset:
            print(indent)
            indent_items = indent.New_Indent.all()  # Related items
            items_data = [
                {
                    "ItemNoCpcCode": item.ItemNoCpcCode,
                    "Description": item.Description,
                    "Unit": item.Unit,
                    "Qty": item.Qty,
                    "Type": item.Type,
                    "SchDate": item.SchDate,
                    "Remark": item.Remark
                }
                for item in indent_items
            ]
            data.append({
                "id": indent.id,
                "Plant": indent.Plant,
                "IndentNo": indent.IndentNo,
                "Date": indent.Date,
                "Time": indent.Time,
                "Category": indent.Category,
                "CPCCode": indent.CPCCode,
                "WorkOrder": indent.WorkOrder,
                "Remark": indent.Remark,
                "PDF_Link": f"/store/indent/pdf/{indent.id}/",
                "Items": items_data
            })
        return Response(data)

def generate_indent_pdf(request, id):
    indent = get_object_or_404(Indent, id=id)
    indent_items = indent.New_Indent.all()

    template = get_template('ViewIndent.html')  # Update this with your actual template name
    html_content = template.render({'indent': indent, 'indent_items': indent_items})

    pdf_file = HTML(string=html_content).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="indent_{id}.pdf"'
    return response


from rest_framework.generics import ListAPIView
from .models import Indent
from .serializers import IndentSerializer

class FilteredIndentListAPIView(ListAPIView):
    serializer_class = IndentSerializer

    def get_queryset(self):
        return Indent.objects.exclude(Auth='Rejected')


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Indent

class ApproveRejectIndentAPIView(APIView):
    def post(self, request, *args, **kwargs):
        indent_id = request.data.get("id")
        action = request.data.get("action")  # 'Approved' or 'Rejected'

        if not indent_id or action not in ['Approved', 'Rejected']:
            return Response({"error": "Invalid data"}, status=400)

        try:
            indent = Indent.objects.get(id=indent_id)
            indent.Auth = action
            indent.save()
            return Response({"success": f"Indent {action}"})
        except Indent.DoesNotExist:
            return Response({"error": "Indent not found"}, status=404)

class ApprovedIndentDropdownAPIView(ListAPIView):
    serializer_class = IndentSerializer

    def get_queryset(self):
        return Indent.objects.filter(Auth='Approved')

# PO GST CALUCLATION

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from All_Masters.models import Item as Item5
from All_Masters.models import Item as Item5
from .models import ItemTransaction2

class ItemTransactionCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        try:
            supplier = Item5.objects.get(id=data['supplier_id'])
        except Item5.DoesNotExist:
            return Response({"error": "Supplier not found"}, status=404)

        txn = ItemTransaction2.objects.create(
            supplier=supplier,
            part_no=data.get('part_no'),
            ItemDescription=data.get('ItemDescription'),
            PartCode=data.get('PartCode'),
            Out=data.get('Out', 0),
            Inn=data.get('Inn', 0),
            Rate=data.get('Rate', 0),
            RType=data.get('RType'),
            Disc=data.get('Disc', 0),
            PoQty=data.get('PoQty', 0),
            Unit=data.get('Unit'),
            ParticularProcess=data.get('ParticularProcess')
        )

        return Response({"message": "Item transaction created", "id": txn.id}, status=201)


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ItemTransaction2

class ItemTransactionDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            txn = ItemTransaction2.objects.get(id=pk)
        except ItemTransaction2.DoesNotExist:
            return Response({"error": "Transaction not found"}, status=404)

        item_info = ItemTable.objects.filter(part_no=txn.part_no).first()
        tax_info = TaxDetails.objects.filter(SAC_Code=item_info.SAC_Code).first() if item_info else None

        supplier = txn.supplier
        gst_code = supplier.GST_Tax_Code.strip().upper() if supplier and supplier.GST_Tax_Code else ""

        rate = float(txn.Rate or 0)
        qty = float(txn.PoQty or 0)
        subtotal = rate * qty
        discount = float(txn.Disc or 0)
        discount_amt = round(subtotal * discount / 100, 2)
        ass_value = round(subtotal - discount_amt, 2)

        cgst = float(tax_info.CGST or 0) if "CGST" in gst_code else 0
        sgst = float(tax_info.SGST or 0) if "SGST" in gst_code else 0
        igst = float(tax_info.IGST or 0) if "IGST" in gst_code else 0
        cess = float(tax_info.Cess or 0) if "CESS" in gst_code else 0

        cgst_amt = round((ass_value * cgst) / 100, 2) if cgst else ""
        sgst_amt = round((ass_value * sgst) / 100, 2) if sgst else ""
        igst_amt = round((ass_value * igst) / 100, 2) if igst else ""
        cess_amt = round((ass_value * cess) / 100, 2) if cess else ""

        total = ass_value + (cgst_amt or 0) + (sgst_amt or 0) + (igst_amt or 0) + (cess_amt or 0)

        return Response({
            "id": txn.id,
            "part_no": txn.part_no,
            "PartCode": txn.PartCode,
            "ItemDescription": txn.ItemDescription,
            "SAC_Code": item_info.SAC_Code if item_info else "",
            "Rate": rate,
            "Disc": discount,
            "PoQty": qty,
            "Unit": txn.Unit,
            "ParticularProcess": txn.ParticularProcess,
            "GST_Details": {
                "AssValue": ass_value,
                "CGST": cgst, "CGSTAmt": cgst_amt,
                "SGST": sgst, "SGSTAmt": sgst_amt,
                "IGST": igst, "IGSTAmt": igst_amt,
                "Cess": cess, "CessAmt": cess_amt,
                "Total": total
            }
        })



# New JobWork Purchase Order
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import NewJobWorkPoInfo
from .serializers import NewJobWorkPoInfoSerializer

class NewJobWorkPoInfoViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = NewJobWorkPoInfo.objects.all()
    serializer_class = NewJobWorkPoInfoSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    


def generate_po_pdf(request, pk):
    po = get_object_or_404(NewJobWorkPoInfo, pk=pk)
    item_details = list(po.Item_Detail_Enter.all())
    gst_details = list(po.Gst_Details.all())
    schedule_lines = po.Schedule_Line.all()
    ship_to_addresses = po.Ship_To_Add.all()

    # Safely zip the item and gst details
    combined_details = zip(item_details, gst_details)

    template = get_template('new_job_work_po_pdf.html')

    html = template.render({
        'po': po,
        'item_details': item_details,
        'gst_details': gst_details,
        'schedule_lines': schedule_lines,
        'ship_to_addresses': ship_to_addresses,
        'combined_details': combined_details,  # <-- Added this line
    })

    pdf_file = HTML(string=html).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="purchase_order_{pk}.pdf"'
    return response



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import NewJobWorkPoInfo
from datetime import datetime

from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import NewJobWorkPoInfo

class NewJobWorkPoInfoAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = NewJobWorkPoInfo.objects.all()

        # Filters from GET params
        filters = {
            "PoNo__icontains": request.GET.get("po_no"),
            "Supplier__icontains": request.GET.get("supplier"),
            "Plant__icontains": request.GET.get("plant"),
            "PoType__icontains": request.GET.get("po_type"),
            "Series__icontains": request.GET.get("series"),
            "PaymentTerm__icontains": request.GET.get("payment_term"),
        }

        # Apply string filters
        for key, value in filters.items():
            if value:
                queryset = queryset.filter(**{key: value})

        # Date filters
        po_date_from = request.GET.get("po_date_from")
        po_date_to = request.GET.get("po_date_to")

        if po_date_from:
            try:
                po_date_from_parsed = datetime.strptime(po_date_from, "%Y-%m-%d")
                queryset = queryset.filter(PoDate__gte=po_date_from_parsed)
            except ValueError:
                return Response({"error": "Invalid po_date_from format. Use YYYY-MM-DD."}, status=400)

        if po_date_to:
            try:
                po_date_to_parsed = datetime.strptime(po_date_to, "%Y-%m-%d")
                queryset = queryset.filter(PoDate__lte=po_date_to_parsed)
            except ValueError:
                return Response({"error": "Invalid po_date_to format. Use YYYY-MM-DD."}, status=400)

        # Serialize results
        data = []
        for po in queryset:
            # Handle Supplier split: "Name - Number"
            supplier_name = ""
            supplier_number = ""
            if po.Supplier:
                parts = po.Supplier.split(" - ")
                if len(parts) == 2:
                    supplier_name = parts[0].strip()
                    supplier_number = parts[1].strip()
                else:
                    supplier_name = po.Supplier

            data.append({
                "id": po.id,
                "Plant": po.Plant,
                "PoNo": po.PoNo,
                "PoDate": po.PoDate,
                "PoType": po.PoType,
                "Name": supplier_name,
                "number": supplier_number,
                "User": po.created_by.username if po.created_by else None,
                "View": f"/Purchase/purchase-order/pdf/{po.id}/",
                "Edit": f"/Purchase/api/NewJobWorkPO/{po.id}/",
            })

        return Response(data)

# views.py
from rest_framework import generics, filters
from All_Masters.models import Item as SupplierItem
from .serializers import JobWorkItemSerializer

class JobWorkItemSearchView(generics.ListAPIView):
    serializer_class = JobWorkItemSerializer
    queryset = SupplierItem.objects.filter(type='Job Work')
    filter_backends = [filters.SearchFilter]
    search_fields = ['Name', 'number']



# get route to fetch the unverified PO's
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import PurchasePO
from .serializers import PurchasePOSerializer


@api_view(['GET'])
def get_purchase_orders(request):
    """
    Simple API endpoint to get unverified purchase orders with item details
    """
    try:
        unverified_pos = PurchasePO.objects.all()
        
        po_data = []
        for po in unverified_pos:
            # Get item details for this purchase order
            item_details = []
            for item in po.Item_Detail_Enter.all():
                item_details.append({
                    'id': item.id,
                    'Item': item.Item,
                    'ItemDescription': item.ItemDescription,
                    'ItemSize': item.ItemSize,
                    'Rate': item.Rate,
                    'Disc': item.Disc,
                    'Qty': item.Qty,
                    'Unit': item.Unit,
                    'Particular': item.Particular,
                    'Mill_Name': item.Mill_Name,
                    'DeliveryDt': item.DeliveryDt.strftime('%Y-%m-%d') if item.DeliveryDt else None
                })
            
            # Get GST details for this purchase order
            gst_details = []
            for gst in po.Gst_Details.all():
                gst_details.append({
                    'id': gst.id,
                    'ItemCode': gst.ItemCode,
                    'HSN': gst.HSN,
                    'Rate': float(gst.Rate) if gst.Rate else None,
                    'Qty': gst.Qty,
                    'SubTotal': float(gst.SubTotal) if gst.SubTotal else None,
                    'Discount': float(gst.Discount) if gst.Discount else None,
                    'Packing': float(gst.Packing) if gst.Packing else None,
                    'Transport': float(gst.Transport) if gst.Transport else None,
                    'ToolAmort': float(gst.ToolAmort) if gst.ToolAmort else None,
                    'AssValue': float(gst.AssValue) if gst.AssValue else None,
                    'CGST': float(gst.CGST) if gst.CGST else None,
                    'SGST': float(gst.SGST) if gst.SGST else None,
                    'IGST': float(gst.IGST) if gst.IGST else None,
                    'Vat': float(gst.Vat) if gst.Vat else None,
                    'Cess': float(gst.Cess) if gst.Cess else None,
                    'Total': float(gst.Total) if gst.Total else None
                })
            
            # Build purchase order data with item details
            po_data.append({
                'id': po.id,
                'field': po.field,
                'PoNo': po.PoNo,
                'EnquiryNo': po.EnquiryNo,
                'Type': po.Type,
                'Plant': po.Plant,
                'Series': po.Series,
                'Supplier': po.Supplier,
                'CodeNo': po.CodeNo,
                'QuotNo': po.QuotNo,
                'PaymentTerms': po.PaymentTerms,
                'DeliveryDate': po.DeliveryDate.strftime('%Y-%m-%d') if po.DeliveryDate else None,
                'PoDate': po.PoDate.strftime('%Y-%m-%d') if po.PoDate else None,
                'PreparedBy': po.PreparedBy,
                'Approved_status' : po.Approved_Status,
                'ApprovedBy': po.ApprovedBy,
                'GR_Total': float(po.GR_Total) if po.GR_Total else None,
                'is_verified': po.is_verified,
                'created_by_username': po.created_by.username if po.created_by else None,
                'ContactPerson': po.ContactPerson,
                'PoNote': po.PoNote,
                'Freight': po.Freight,
                'PoRateType': po.PoRateType,
                'GstTaxes': po.GstTaxes,
                # Item details
                'item_details': item_details,
                'item_count': len(item_details),
                # GST details
                'gst_details': gst_details,
                'gst_count': len(gst_details)
            })
        
        return JsonResponse({
            'success': True,
            'message': f'Found {len(po_data)} unverified purchase orders with item details',
            'count': len(po_data),
            'data': po_data
        }, status=200)
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error fetching unverified purchase orders: {str(e)}',
            'data': []
        }, status=500)



@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Remove this if authentication is not required
def get_unverified_purchase_orders(request):
    """
    API endpoint to get all purchase orders that are not verified (is_verified=False)
    """
    try:
        # Filter purchase orders where is_verified is False
        unverified_pos = PurchasePO.objects.filter(is_verified=False)
        
        # Serialize the data
        serializer = PurchasePOSerializer(unverified_pos, many=True)
        
        return Response({
            'success': True,
            'message': f'Found {unverified_pos.count()} unverified purchase orders',
            'count': unverified_pos.count(),
            'data': serializer.data
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'success': False,
            'message': f'Error fetching unverified purchase orders: {str(e)}',
            'data': []
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Alternative simpler version without DRF serializers
@api_view(['GET'])
def get_unverified_purchase_orders_simple(request):
    """
    Simple API endpoint to get unverified purchase orders with item details
    """
    try:
        unverified_pos = PurchasePO.objects.filter(Approved_Status__in=['pending', 'Pending']).select_related('created_by').prefetch_related('Item_Detail_Enter', 'Gst_Details')
        
        po_data = []
        for po in unverified_pos:
            # Get item details for this purchase order
            item_details = []
            for item in po.Item_Detail_Enter.all():
                item_details.append({
                    'id': item.id,
                    'Item': item.Item,
                    'ItemDescription': item.ItemDescription,
                    'ItemSize': item.ItemSize,
                    'Rate': item.Rate,
                    'Disc': item.Disc,
                    'Qty': item.Qty,
                    'Unit': item.Unit,
                    'Particular': item.Particular,
                    'Mill_Name': item.Mill_Name,
                    'DeliveryDt': item.DeliveryDt.strftime('%Y-%m-%d') if item.DeliveryDt else None
                })
            
            # Get GST details for this purchase order
            gst_details = []
            for gst in po.Gst_Details.all():
                gst_details.append({
                    'id': gst.id,
                    'ItemCode': gst.ItemCode,
                    'HSN': gst.HSN,
                    'Rate': float(gst.Rate) if gst.Rate else None,
                    'Qty': gst.Qty,
                    'SubTotal': float(gst.SubTotal) if gst.SubTotal else None,
                    'Discount': float(gst.Discount) if gst.Discount else None,
                    'Packing': float(gst.Packing) if gst.Packing else None,
                    'Transport': float(gst.Transport) if gst.Transport else None,
                    'ToolAmort': float(gst.ToolAmort) if gst.ToolAmort else None,
                    'AssValue': float(gst.AssValue) if gst.AssValue else None,
                    'CGST': float(gst.CGST) if gst.CGST else None,
                    'SGST': float(gst.SGST) if gst.SGST else None,
                    'IGST': float(gst.IGST) if gst.IGST else None,
                    'Vat': float(gst.Vat) if gst.Vat else None,
                    'Cess': float(gst.Cess) if gst.Cess else None,
                    'Total': float(gst.Total) if gst.Total else None
                })
            
            # Build purchase order data with item details
            po_data.append({
                'id': po.id,
                'field': po.field,
                'PoNo': po.PoNo,
                'EnquiryNo': po.EnquiryNo,
                'Type': po.Type,
                'Plant': po.Plant,
                'Series': po.Series,
                'Supplier': po.Supplier,
                'CodeNo': po.CodeNo,
                'QuotNo': po.QuotNo,
                'PaymentTerms': po.PaymentTerms,
                'DeliveryDate': po.DeliveryDate.strftime('%Y-%m-%d') if po.DeliveryDate else None,
                'PoDate': po.PoDate.strftime('%Y-%m-%d') if po.PoDate else None,
                'PreparedBy': po.PreparedBy,
                'ApprovedBy': po.ApprovedBy,
                'GR_Total': float(po.GR_Total) if po.GR_Total else None,
                'is_verified': po.is_verified,
                'created_by_username': po.created_by.username if po.created_by else None,
                'ContactPerson': po.ContactPerson,
                'PoNote': po.PoNote,
                'Freight': po.Freight,
                'PoRateType': po.PoRateType,
                'GstTaxes': po.GstTaxes,
                # Item details
                'item_details': item_details,
                'item_count': len(item_details),
                # GST details
                'gst_details': gst_details,
                'gst_count': len(gst_details)
            })
        
        return JsonResponse({
            'success': True,
            'message': f'Found {len(po_data)} unverified purchase orders with item details',
            'count': len(po_data),
            'data': po_data
        }, status=200)
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error fetching unverified purchase orders: {str(e)}',
            'data': []
        }, status=500)



from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import PurchasePO

@csrf_exempt
@require_http_methods(["POST"])
# @login_required
def update_approved_status(request, po_id):
    """
    Function-based view to update approved status
    """
    try:
        # Get the PurchasePO object
        purchase_po = get_object_or_404(PurchasePO, id=po_id)
        
        # Parse JSON data from request body
        data = json.loads(request.body)
        new_status = data.get('approved_status')
        
        # Validate the new status
        valid_statuses = ['Approved', 'Pending', 'Rejected']
        if new_status not in valid_statuses:
            return JsonResponse({
                'success': False,
                'message': f'Invalid status. Must be one of: {valid_statuses}'
            }, status=400)
        
        # Update the approved status
        old_status = purchase_po.Approved_Status
        purchase_po.Approved_Status = new_status
        purchase_po.save()
        
        return JsonResponse({
            'success': True,
            'message': 'Approved status updated successfully',
            'data': {
                'po_id': purchase_po.id,
                'po_no': purchase_po.PoNo,
                'old_status': old_status,
                'new_status': purchase_po.Approved_Status,
                'updated_by': request.user.username
            }
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid JSON data'
        }, status=400)
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'An error occurred: {str(e)}'
        }, status=500)



from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Indent, New_Indent
import json

# Function-based view

@require_http_methods(["GET"])
def get_indents(request):
    """
    GET route to fetch all indents with Auth status 'Pending' or 'pending'
    """
    try:
        # Filter indents with Auth status 'Pending' (case-insensitive)
        pending_indents = Indent.objects.all()
        
        # Convert queryset to list of dictionaries
        indents_data = []
        for indent in pending_indents:
            indent_dict = {
                'id': indent.id,
                'Plant': indent.Plant,
                'Series': indent.Series,
                'IndentNo': indent.IndentNo,
                'Date': indent.Date,
                'Time': indent.Time,
                'Category': indent.Category,
                'CPCCode': indent.CPCCode,
                'WorkOrder': indent.WorkOrder,
                'Remark': indent.Remark,
                'Auth': indent.Auth,
                # Include related New_Indent items if needed
                'indent_details': []
            }
            
            # Get related New_Indent records
            new_indent_details = New_Indent.objects.filter(New_Indent_Detail=indent)
            for detail in new_indent_details:
                detail_dict = {
                    'id': detail.id,
                    'ItemNoCpcCode': detail.ItemNoCpcCode,
                    'Description': detail.Description,
                    'Unit': detail.Unit,
                    'MachineAndDepartment': detail.MachineAndDepartment,
                    'Qty': detail.Qty,
                    'Type': detail.Type,
                    'Remark': detail.Remark,
                    'UseFor': detail.UseFor,
                    'MoRef': detail.MoRef,
                    'SchDate': detail.SchDate,
                }
                indent_dict['indent_details'].append(detail_dict)
            
            indents_data.append(indent_dict)
        
        return JsonResponse({
            'success': True,
            'count': len(indents_data),
            'data': indents_data
        }, status=200)
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)



@require_http_methods(["GET"])
def get_pending_indents(request):
    """
    GET route to fetch all indents with Auth status 'Pending' or 'pending'
    """
    try:
        # Filter indents with Auth status 'Pending' (case-insensitive)
        pending_indents = Indent.objects.filter(Auth__iexact='pending')
        
        # Convert queryset to list of dictionaries
        indents_data = []
        for indent in pending_indents:
            indent_dict = {
                'id': indent.id,
                'Plant': indent.Plant,
                'Series': indent.Series,
                'IndentNo': indent.IndentNo,
                'Date': indent.Date,
                'Time': indent.Time,
                'Category': indent.Category,
                'CPCCode': indent.CPCCode,
                'WorkOrder': indent.WorkOrder,
                'Remark': indent.Remark,
                'Auth': indent.Auth,
                # Include related New_Indent items if needed
                'indent_details': []
            }
            
            # Get related New_Indent records
            new_indent_details = New_Indent.objects.filter(New_Indent_Detail=indent)
            for detail in new_indent_details:
                detail_dict = {
                    'id': detail.id,
                    'ItemNoCpcCode': detail.ItemNoCpcCode,
                    'Description': detail.Description,
                    'Unit': detail.Unit,
                    'MachineAndDepartment': detail.MachineAndDepartment,
                    'Qty': detail.Qty,
                    'Type': detail.Type,
                    'Remark': detail.Remark,
                    'UseFor': detail.UseFor,
                    'MoRef': detail.MoRef,
                    'SchDate': detail.SchDate,
                }
                indent_dict['indent_details'].append(detail_dict)
            
            indents_data.append(indent_dict)
        
        return JsonResponse({
            'success': True,
            'count': len(indents_data),
            'data': indents_data
        }, status=200)
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)



@csrf_exempt
@require_http_methods(["POST"])
def update_indent_auth_status(request):
    """
    POST route to update Auth status of an indent
    Expected JSON payload:
    {
        "indent_id": 1,
        "auth_status": "Approved" or "Rejected" or "Pending"
    }
    """
    try:
        # Parse JSON data from request body
        data = json.loads(request.body)
        
        # Get required fields
        indent_id = data.get('indent_id')
        auth_status = data.get('auth_status')
        
        # Validate required fields
        if not indent_id:
            return JsonResponse({
                'success': False,
                'error': 'indent_id is required'
            }, status=400)
        
        if not auth_status:
            return JsonResponse({
                'success': False,
                'error': 'auth_status is required'
            }, status=400)
        
        # Validate auth_status against allowed choices
        valid_statuses = ['Pending', 'Approved', 'Rejected']
        if auth_status not in valid_statuses:
            return JsonResponse({
                'success': False,
                'error': f'auth_status must be one of: {", ".join(valid_statuses)}'
            }, status=400)
        
        # Get the indent object
        try:
            indent = Indent.objects.get(id=indent_id)
        except Indent.DoesNotExist:
            return JsonResponse({
                'success': False,
                'error': f'Indent with id {indent_id} not found'
            }, status=404)
        
        # Store old status for response
        old_status = indent.Auth
        
        # Update the Auth status
        indent.Auth = auth_status
        indent.save()
        
        return JsonResponse({
            'success': True,
            'message': f'Indent auth status updated successfully',
            'data': {
                'indent_id': indent.id,
                'indent_no': indent.IndentNo,
                'old_status': old_status,
                'new_status': indent.Auth,
                'plant': indent.Plant,
                'series': indent.Series
            }
        }, status=200)
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON in request body'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)
    

from rest_framework import viewsets
from .models import QuotationComparison
from .models import RFQ
from .serializers import QuotationComparisonSerializer
from .serializers import RFQSerializer
class QuotationComparisonViewSet(viewsets.ModelViewSet):
    queryset = QuotationComparison.objects.all()
    serializer_class = QuotationComparisonSerializer 
class RFQViewSet(viewsets.ModelViewSet):
    queryset=RFQ.objects.all()
    serializer_class=RFQSerializer

class DeleteQuotationComparison(APIView):
    def delete(self, request, pk):
        try:
            quotation = QuotationComparison.objects.get(pk=pk)
            quotation.delete()
            return Response(
                {'message': f'QuotationComparison with id {pk} deleted successfully'},
                status=status.HTTP_204_NO_CONTENT
            )
        except QuotationComparison.DoesNotExist:
            return Response(
                {'error': 'QuotationComparison not found'},
                status=status.HTTP_404_NOT_FOUND
            )



class EditQuotationComparison(APIView):
    def put(self, request, pk):
        try:
            quotation = QuotationComparison.objects.get(pk=pk)
        except QuotationComparison.DoesNotExist:
            return Response(
                {'error': 'QuotationComparison not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = QuotationComparisonSerializer(quotation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


from .utils import Create_RFQ_No

class generate_unique_rfq_no(APIView):
    def get(self, request):
        try:
            rfq_no = Create_RFQ_No()  
            return Response({"rfq_no" : rfq_no}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
from All_Masters.models import ItemTable
from All_Masters.models import BOMItem
from .serializers import BOMItemWithnewjobwork
from django.db.models import Q

class newjobworkitemdata(APIView):
    def get(self, request):
        query = request.query_params.get('q', '').strip()
        if not query:
            return Response({'error': 'Search query "q" is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Filter ItemTable with any match of part_code, part_no or name_description
        items = ItemTable.objects.filter(
            Q(Part_Code__icontains=query) |
            Q(part_no__icontains=query) |
            Q(Name_Description__icontains=query)
        )

        if not items.exists():
            return Response({'error': 'No items found matching your query'}, status=status.HTTP_404_NOT_FOUND)

        bom_items = BOMItem.objects.filter(item__in=items)
        serializer = BOMItemWithnewjobwork(bom_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
        