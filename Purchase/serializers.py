from rest_framework import serializers
from .models import *
from .models import PoInfo
from All_Masters .models import Supplier_Customer
from All_Masters .models import ItemMaster
from .models import JwPoInfo
from .models import JwItemDetail
from .models import JwShipAdd
from .models import Quote_Comparison_Statement
from All_Masters.models import Item
from All_Masters.models import ItemTable

# New Purchase Master:- Fetch supplier
class Fetch_Supplier_Code_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'Name', 'number', "Payment_Term"]

# New Purchase Master:- Fetch Item Master fields
class Fetch_Item_fields_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTable
        fields = ['id', 'part_no', 'Part_Code', 'Name_Description', 'Rate', 'Item_Size', 'HSN_SAC_Code', 'Unit_Code']


# New Purchase Master
class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDetail
        fields = ['id', 'Item', 'ItemDescription', 'ItemSize', 'Rate', 'Disc', 'Qty', 'Unit', 'Particular', 
                  'Mill_Name', 'DeliveryDt']
        
# New Purchase Master:- Fetch Api
class ItemRateQtySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDetail
        fields = ['id', 'Rate', 'Qty']  # Only include 'Rate' and 'Qty'


# New Purchase Master:- PO Info
class PO_Info_Serializer(serializers.ModelSerializer):
    class Meta:
        model = PoInfo
        fields = [
    'PoNo', 'EnquiryNo', 'QuotNo', 'PaymentTerms', 'DeliveryDate', 
    'AMC_PO', 'ModeOfShipment', 'PreparedBy', 'PoNote', 'PoSpecification', 
    'PoDate', 'EnquiryDate', 'QuotDate', 'PaymentRemark', 'DeliveryType', 
    'DeliveryNote', 'IndentNo', 'ApprovedBy', 'InspectionTerms', 
    'PF_Charges', 'Time', 'PoFor', 'Freight', 'PoRateType', 
    'ContactPerson', 'PoValidityDate', 'PoEffectiveDate', 'TransportName', 
    'PoValidity_WarrantyTerm', 'GstTaxes'
]

# New JobWork Purchase Order:- Po Info
class JwPoInfo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = JwPoInfo
        fields = ['id', 'PoNo', 'PaymentTerm', 'QuotNo', 'Delivery', 'PoValidityDate', 'PoNote', 'GST', 'PoDate',
                   'PaymentRemark', 'QuotationDate', 'freight', 'ContactPersion', 'PF_Charges', 'PoRateType']


# New JobWork Purchase Order:- ItemDetail
class JwItemDetail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = JwItemDetail
        fields = ['id', 'SelectItem', 'ItemDescription', 'Out', 'In', 'Rate', 'RType', 'Disc', 'PoQty', 'Unit', 
                  'Particular_Process']
    
# New JobWork Purchase Order:- Ship To Add
class JwShipAdd_Serializer(serializers.ModelSerializer):
    class Meta:
        model = JwShipAdd
        fields = ['id', 'ShiptoAdd', 'ContactDetail', 'ProjectName', 'CRName', 'SoNo']


# New JobWork Purchase Order:- PoInfo Enter Supplier Name to Fetch Payment Term
class Fetch_PaymentTerm_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier_Customer
        fields = ['Payment_Term', 'Name', 'Code_No']

# Quote Comparison:- Quote Comparison Statement
class Quote_Comparison_Statement_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Quote_Comparison_Statement
        fields = ['id', 'SelectRFQ', 'Item', 'Make', 'MinPurchQty', 'OtherCharges', 'PaymentTerms', 'Date', 
                  'Supplier', 'UOM', 'TaxApplicable', 'RemarkDetails', 'SuppQuotNo', 'BasicRate', 
                  'DeliveryMode', 'QuoteDate', 'Discount', 'DeliveryTime']
        



# serializers.py
from rest_framework import serializers

class CountrySerializer(serializers.Serializer):
    name = serializers.CharField()


 
#PO Serial numbers
from rest_framework import serializers
from rest_framework import serializers
from .models import CodeGenerator

class CodeGeneratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeGenerator
        fields = [
            'field', 'year', 'last_code', 'PoNo', 'EnquiryNo', 'QuotNo', 'PaymentTerms',
            'DeliveryDate', 'AMC_PO', 'ModeOfShipment', 'PreparedBy', 'PoNote', 'PoSpecification',
            'PoDate', 'EnquiryDate', 'QuotDate', 'PaymentRemark', 'DeliveryType', 'DeliveryNote',
            'IndentNo', 'ApprovedBy', 'InspectionTerms', 'PF_Charges', 'Time', 'PoFor', 'Freight',
            'PoRateType', 'ContactPerson', 'PoValidityDate', 'PoEffectiveDate', 'TransportName',
            'PoValidity_WarrantyTerm', 'GstTaxes'
        ]


class CodeGenerationResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
    generated_code = serializers.CharField()


#RUD
from rest_framework import serializers
from .models import CodeGenerator

class RUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeGenerator
        fields = '__all__'  # Include all fields from the CodeGenerator model



from rest_framework import serializers
from .models import PurchaseOrder

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ["id", "POType", "Plant", "Series", "Supplier", "PoNo", "PaymentTerm", "QuotNo", "Delivery", "PoValidityDate", "PoNote",
                   "GST", "PoDate", "PaymentRemark", "QuotationDate", "freight", 
                   "ContactPersion", "PF_Charges", "PoRateType"]



from rest_framework import serializers
from .models import PurchaseNewIndent

class PurchaseNewIndentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseNewIndent
        fields = []



###########
# serializers.py

from rest_framework import serializers
from .models import PurchasePO, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item_code', 'description', 'quantity', 'unit_price', 'total_price']

# from rest_framework import serializers
# from .models import PurchasePO, PurchasePODetails

# class PurchasePODetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PurchasePODetails
#         fields = '__all__'

# class OOPurchaseSerializer(serializers.ModelSerializer):
#     # Serialize the related PurchasePODetails
#     purchase_po_details = PurchasePODetailsSerializer(many=True, required=False)

#     class Meta:
#         model = PurchasePO
#         fields = '__all__'

#     def create(self, validated_data):
#         # Handle nested purchase_po_details
#         purchase_po_details_data = validated_data.pop('purchase_po_details', [])
#         purchase = PurchasePO.objects.create(**validated_data)
        
#         # Create the related PurchasePODetails instances
#         for po_detail_data in purchase_po_details_data:
#             po_detail = PurchasePODetails.objects.create(**po_detail_data)
#             purchase.purchase_po_details.add(po_detail)

#         return purchase
from rest_framework import serializers
from .models import PurchasePO, GSTDetails, ItemDetailsOther, ScheduleLine, ShipToAdd, ItemDetail


class Item_Detail_EnterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDetail
        fields = '__all__'

class GSTDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GSTDetails
        fields = '__all__'

class ItemDetailsOtherSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDetailsOther
        fields = '__all__'

class ScheduleLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleLine
        fields = '__all__'

class ShipToAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipToAdd
        fields = '__all__'

class OOPurchaseSerializer(serializers.ModelSerializer):
    # Serialize the related PurchasePODetails and GSTDetails
    Item_Detail_Enter = Item_Detail_EnterSerializer(many=True, required=False, allow_null=True)
    Gst_Details = GSTDetailsSerializer(many=True, required=False, allow_null=True)
    Item_Details_Other = ItemDetailsOtherSerializer(many=True, required=False, allow_null=True)
    Schedule_Line = ScheduleLineSerializer(many=True, required=False, allow_null=True)
    Ship_To_Add = ShipToAddSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = PurchasePO
        fields = '__all__'

    def create(self, validated_data):
        # Handle nested purchase_po_details, Gst_Details, and Item_Details_Other
        Item_Detail_Enter_data = validated_data.pop('Item_Detail_Enter', [])
        gst_details_data = validated_data.pop('Gst_Details', [])
        Item_Details_Other_data = validated_data.pop('Item_Details_Other', [])
        Schedule_Line_data = validated_data.pop('Schedule_Line', [])
        Ship_To_Add_data = validated_data.pop('Ship_To_Add', [])
        
        # Create the PurchasePO instance
        purchase = PurchasePO.objects.create(**validated_data)
        
        
        for Item_Detail_Enter_data in Item_Detail_Enter_data:
            Item_Detail_Enter = ItemDetail.objects.create(**Item_Detail_Enter_data)
            purchase.Item_Detail_Enter.add(Item_Detail_Enter) 

        # Create the related GSTDetails instances and add them to the PurchasePO
        for gst_detail_data in gst_details_data:
            gst_detail = GSTDetails.objects.create(**gst_detail_data)
            purchase.Gst_Details.add(gst_detail)  # Assuming there's a related field in PurchasePO
        
        # Corrected: Use 'Item_Details_Other_data' instead of 'Item_Details_Other'
        for item_detail_data in Item_Details_Other_data:
            item_detail = ItemDetailsOther.objects.create(**item_detail_data)
            purchase.Item_Details_Other.add(item_detail)  # Assuming there's a related field in PurchasePO
        
        for Schedule_Line_data in Schedule_Line_data:
            Schedule_Line = ScheduleLine.objects.create(**Schedule_Line_data)
            purchase.Schedule_Line.add(Schedule_Line)
        
        for Ship_To_Add_data in Ship_To_Add_data:
            Ship_To_Add = ShipToAdd.objects.create(**Ship_To_Add_data)
            purchase.Ship_To_Add.add(Ship_To_Add)

        return purchase




##testign 
from rest_framework import serializers
from .models import ItemDetail

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDetail
        fields = '__all__'

# Indent No
from rest_framework import serializers
from .models import Indent, New_Indent

class NewIndentSerializer(serializers.ModelSerializer):
    class Meta:
        model = New_Indent
        fields = [
            'ItemNoCpcCode', 'Description', 'Unit', 'MachineAndDepartment',
            'Qty', 'Type', 'Remark', 'UseFor', 'MoRef', 'SchDate'
        ]

class IndentSerializer(serializers.ModelSerializer):
    New_Indent = NewIndentSerializer(many=True, required=False)

    class Meta:
        model = Indent
        fields = '__all__'

    def create(self, validated_data):
        indent_items_data = validated_data.pop('New_Indent', [])
        indent = Indent.objects.create(**validated_data)

        for item_data in indent_items_data:
            New_Indent.objects.create(New_Indent_Detail=indent, **item_data)

        return indent

    def update(self, instance, validated_data):
        indent_items_data = validated_data.pop('New_Indent', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if indent_items_data is not None:
            instance.New_Indent.all().delete()
            for item_data in indent_items_data:
                New_Indent.objects.create(New_Indent_Detail=instance, **item_data)

        return instance
    
# New JobWork Purchase Order
class NewJobWorkItemDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewJobWorkItemDetails
        fields = '__all__'

class NewJobWorkGstDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewJobWorkGstDetails
        fields = '__all__'

class NewJobWorkScheduleLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewJobWorkScheduleLine
        fields = '__all__'

class NewJobWorkShipToAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewJobWorkShipToAdd
        fields = '__all__'

from rest_framework import serializers
from django.db import transaction

class NewJobWorkPoInfoSerializer(serializers.ModelSerializer):
    Item_Detail_Enter = NewJobWorkItemDetailsSerializer(many=True, required=False)
    Gst_Details = NewJobWorkGstDetailsSerializer(many=True, required=False)
    Schedule_Line = NewJobWorkScheduleLineSerializer(many=True, required=False)
    Ship_To_Add = NewJobWorkShipToAddSerializer(many=True, required=False)

    class Meta:
        model = NewJobWorkPoInfo
        fields = '__all__'

    def create(self, validated_data):
        items = validated_data.pop('Item_Detail_Enter', [])
        gst = validated_data.pop('Gst_Details', [])
        schedule = validated_data.pop('Schedule_Line', [])
        ship = validated_data.pop('Ship_To_Add', [])

        po = NewJobWorkPoInfo.objects.create(**validated_data)

        for item in items:
            obj = NewJobWorkItemDetails.objects.create(**item)
            po.Item_Detail_Enter.add(obj)

        for gst_item in gst:
            obj = NewJobWorkGstDetails.objects.create(**gst_item)
            po.Gst_Details.add(obj)

        for schedule_item in schedule:
            obj = NewJobWorkScheduleLine.objects.create(**schedule_item)
            po.Schedule_Line.add(obj)

        for ship_item in ship:
            obj = NewJobWorkShipToAdd.objects.create(**ship_item)
            po.Ship_To_Add.add(obj)

        return po

    def update(self, instance, validated_data):
        items = validated_data.pop('Item_Detail_Enter', [])
        gst = validated_data.pop('Gst_Details', [])
        schedule = validated_data.pop('Schedule_Line', [])
        ship = validated_data.pop('Ship_To_Add', [])

        with transaction.atomic():
            # Update base fields
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()

            # Clear and recreate related objects
            instance.Item_Detail_Enter.clear()
            NewJobWorkItemDetails.objects.filter(id__in=[obj.id for obj in instance.Item_Detail_Enter.all()]).delete()
            for item in items:
                obj = NewJobWorkItemDetails.objects.create(**item)
                instance.Item_Detail_Enter.add(obj)

            instance.Gst_Details.clear()
            NewJobWorkGstDetails.objects.filter(id__in=[obj.id for obj in instance.Gst_Details.all()]).delete()
            for gst_item in gst:
                obj = NewJobWorkGstDetails.objects.create(**gst_item)
                instance.Gst_Details.add(obj)

            instance.Schedule_Line.clear()
            NewJobWorkScheduleLine.objects.filter(id__in=[obj.id for obj in instance.Schedule_Line.all()]).delete()
            for schedule_item in schedule:
                obj = NewJobWorkScheduleLine.objects.create(**schedule_item)
                instance.Schedule_Line.add(obj)

            instance.Ship_To_Add.clear()
            NewJobWorkShipToAdd.objects.filter(id__in=[obj.id for obj in instance.Ship_To_Add.all()]).delete()
            for ship_item in ship:
                obj = NewJobWorkShipToAdd.objects.create(**ship_item)
                instance.Ship_To_Add.add(obj)

        return instance



from rest_framework import serializers
from All_Masters.models import Item as SupplierItem

class JobWorkItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierItem
        fields = ['id', 'Name', 'number']


from rest_framework import serializers
from .models import PurchasePO, ItemDetail, GSTDetails

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDetail
        fields = '__all__'

class GSTDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GSTDetails
        fields = '__all__'

class PurchasePOSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    item_details = ItemDetailSerializer(source='Item_Detail_Enter', many=True, read_only=True)
    gst_details = GSTDetailsSerializer(source='Gst_Details', many=True, read_only=True)
    
    class Meta:
        model = PurchasePO
        fields = [
            'id', 'field', 'PoNo', 'EnquiryNo', 'Type', 'Plant', 'Series',
            'Supplier', 'CodeNo', 'QuotNo', 'PaymentTerms', 'DeliveryDate',
            'AMC_PO', 'ModeOfShipment', 'PreparedBy', 'PoNote', 'PoSpecification',
            'PoDate', 'EnquiryDate', 'QuotDate', 'PaymentRemark', 'DeliveryType',
            'DeliveryNote', 'IndentNo', 'ApprovedBy', 'InspectionTerms',
            'PF_Charges', 'Time', 'PoFor', 'Freight', 'PoRateType',
            'ContactPerson', 'PoValidityDate', 'PoEffectiveDate', 'TransportName',
            'PoValidity_WarrantyTerm', 'GstTaxes', 'TOC_AssableValue',
            'TOC_PackCharges', 'TOC_TransportCost', 'TOC_Insurance',
            'TOC_InstallationCharges', 'TOC_CGST', 'TOC_SGST', 'TOC_IGST',
            'TOC_VAT', 'TOC_CESS', 'TOC_TDS', 'GR_Total', 'created_by_username',
            'is_verified', 'item_details', 'gst_details'
        ]


class QuotationComparisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationComparison
        fields = '_all_'

class RFQSerializer(serializers.ModelSerializer):
    rfq_type = serializers.ChoiceField(choices=RFQ.RFQ_TYPE_CHOICES)
    item = serializers.ChoiceField(choices=RFQ.ITEM_TYPE_CHOICES)
    unit = serializers.ChoiceField(choices=RFQ.UNIT_CHOICES)
    class Meta:
        model = RFQ
        fields = [
            'id',
            'rfq_type',
            'rfq_no',
            'item',
            'item_no',
            'quantity',
            'delivery_location',
            'payment_term',
            'delivery_schedule',
            'to_date',
            'indent_no',
            'unit',
            'quality_terms',
            'remark_details',
            'expected_date',
            'project_name'
        ]

#new job work oreder iteam deta in out
from rest_framework import serializers
from All_Masters.models import BOMItem

class BOMItemWithnewjobwork(serializers.ModelSerializer):
    part_code = serializers.CharField(source='item.Part_Code', read_only=True)
    part_no = serializers.CharField(source='item.part_no', read_only=True)
    Name_Description = serializers.CharField(source='item.Name_Description', read_only=True)

    class Meta:
        model = BOMItem
        fields = [
            'id',      
            'part_code',
            'part_no',
            'Name_Description',
             'OPNo', 'Operation', 'PartCode','BOMPartType',
        ]
