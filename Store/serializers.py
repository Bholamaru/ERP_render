from rest_framework import serializers
from .models import *

# # Store Module:- Gate Inward Entry:- General Details
# class GeneralDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GeneralDetails
#         fields = [
#     'id', 'Plant', 'Series', 'Type', 'Supp_Cust', 'GE_No', 'GE_Date', 'GE_Time',
#     'ChallanNo', 'ChallanDate', 'Select', 'InVoiceNo','Invoicedate', 'EWayBillNo', 
#     'EWayBillDate', 'ContactPerson', 'VehicleNo', 'LrNo', 'Transporter', 'Remark']
        
# # Store Module:- Gate Inward Entry:- Item Details
# class ItemDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ItemDetails
#         fields = ['id', 'SelectItem', 'Qty_NOS', 'Qty_Kg', 'Remark']

class ItemDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDetails
        fields = ['ItemNo', 'Description', 'Qty_NOS', 'QTY_KG', 'Unit_Code', 'Remark']

class GeneralDetailsSerializer(serializers.ModelSerializer):
    ItemDetails = ItemDetailsSerializer(many=True)  # Related ItemDetails

    class Meta:
        model = GeneralDetails
        fields = '__all__'

    def create(self, validated_data):
        item_details_data = validated_data.pop('ItemDetails')  # Extract ItemDetails data
        general_detail = GeneralDetails.objects.create(**validated_data)

        for item_data in item_details_data:
            ItemDetails.objects.create(Work_Order_detail=general_detail, **item_data)

        return general_detail

    def update(self, instance, validated_data):
        item_details_data = validated_data.pop('ItemDetails', None)  # Handle item details

        # Update GeneralDetails fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update ItemDetails if provided
        if item_details_data:
            instance.ItemDetails.all().delete()  # Remove existing ItemDetails
            for item_data in item_details_data:
                ItemDetails.objects.create(Work_Order_detail=instance, **item_data)

        return instance

from rest_framework import serializers
from .models import GrnGenralDetail, NewGrnList, GrnGst, GrnGstTDC

class NewGrnListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewGrnList
        fields = '__all__'

class GrnGstSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrnGst
        fields = '__all__'

class GrnGstTDCSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrnGstTDC
        fields = '__all__'

class GrnGenralDetailSerializer(serializers.ModelSerializer):
    grn_items = NewGrnListSerializer(source='NewGrnList', many=True, read_only=True)
    grn_gst = GrnGstSerializer(source='GrnGst', many=True, read_only=True)
    grn_tdc = GrnGstTDCSerializer(source='GrnGstTDC', many=True, read_only=True)
    
    class Meta:
        model = GrnGenralDetail
        fields = '__all__'


# Store Module:- NEW MRN
class NewMrnTableSerilzer(serializers.ModelSerializer):
    class Meta:
        model = NewMRNTable
        fields = ['id', 'ItemCode', 'Description', 'QtyUnit', 'Qty_1', 'Type', 'Machine', 'Employee', 'Dept', 'Remark_1']

class NewMrnSerializer(serializers.ModelSerializer):
    NewMRNTable = NewMrnTableSerilzer(many=True)

    class Meta:
        model = NewMrn
        fields = '__all__'
        

    def create(self, validated_data):
        New_MRN_Table_data = validated_data.pop('NewMRNTable')
        New_MRN_Entry_details = NewMrn.objects.create(**validated_data)

        for item_data in New_MRN_Table_data:
            NewMRNTable.objects.create(New_MRN_Detail=New_MRN_Entry_details, **item_data)

        return New_MRN_Entry_details

    def update(self, instance, validated_data):
        New_MRN_Table_data = validated_data.pop('NewMRNTable', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if New_MRN_Table_data:
            instance.NewMRNTable.all().delete()
            for item_data in New_MRN_Table_data:
                NewMRNTable.objects.create(New_MRN_Detail=instance, **item_data)

        return instance
    

# New MRN Item Search Serializer
from All_Masters.models import ItemTable as ItemSearch

class NewMRNItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSearch
        fields = ['part_no', 'Name_Description', 'Unit_Code']


# New MRN Employee Depatment
from All_Masters.models import Add_New_Operator_Model

class NewMRNEmployeeDeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Add_New_Operator_Model
        fields = ['Code', 'Name', 'Type', 'Department']


# Store Module:- Purchase GRN: General Details
class GrnGenralDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrnGenralDetail
        fields = fields = ['id', 'GrnNo', 'GrnDate', 'GrnTime', 'ChallanNo', 'ChallanDate', 'InvoiceNo', 
                           'InvoiceDate', 'EWayBillNo', 'EWayBillDate', 'VehicleNo', 'LrNo', 'Transporter',
                           'PreparedBy', 'CheckedBy', 'TcNo', 'TcDate', 'QcCheck', 'Delivery', 'Remark', 'PaymentTermDay']

# Store Module:- SubCon GRN: 57F4 Inward Challan
class InwardChallanSerializer(serializers.ModelSerializer):
    class Meta:
        model = InwardChallan
        fields = ['id', 'InwardF4No', 'InwardDate', 'InwardTime', 'ChallanNo', 'ChallanDate',
                             'GateEnrtyNo', 'InvoiceNo', 'InvoiceDate', 'EWayBillQty', 'EWayBillNo',
                               'VehicleNo', 'LrNo', 'Transporter', 'PreparedBy', 'CheckedBy', 'TcNo',
                                 'TcDate', 'Remark', 'DeliveryInTime', 'TotalItem',
                                   'TotalQtyNo', 'TotalQtyKg', 'Store']
        

# Store Module:- SubCon GRN: Job Work Inward Challan 
class Job_WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Work
        fields = ['id', 'InwardF4No', 'InwardDate', 'InwardTime', 'ChallanNo', 'ChallanDate', 'SubVendor', 
          'DcNo', 'DcDate', 'EWayBillQty', 'EWayBillNo', 'VehicleNo', 'LrNo', 'Transporter', 
          'PreparedBy', 'CheckedBy', 'VehicleTime', 'TcNo', 'TcDate', 'Remark', 'DeliveryInTime', 
          'ClearingStatus', 'VehicleOutTime']


# Store Module:- SubCon GRN: Vendor Scrap Inward
class VendorScrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorScrap
        fields = ['id', 'InWardNo', 'InWardDate', 'InWardTime', 'ChallanNo', 'ChallonDate', 'GIN_No', 'InvoiceNo',
                   'InvoiceDate', 'PreparedBy', 'CheckedBy', 'VehicleNo', 'LrNo', 'Transporter', 'Remark', 'DeliveryInTime']

# Store Module:- Material Issue Challan
class MaterialIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialIssue
        fields = ['id', 'Item', 'ItemDescription', 'AvailableStock', 'Machine', 'StoreName', 'Qty', 'Unit',
                   'Remark', 'MrnNo', 'Employee']
        
# Store Module:- Material Issue General
class Material_Issue_GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material_Issue_General
        fields = ['id', 'Item', 'ItemDescription', 'AvailableStock', 'StockStatus', 'Machine', 'StoreName', 
                  'Qty', 'Unit', 'Remark', 'MrnNo', 'Employee']

# Store Module:- DeliveryChallan
class DeliveryChallan_GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryChallan
        fields = ['id', 'SelectItem', 'Store', 'ItemCode', 'HSNCode', 'Description', 'Purpose', 'Unit',
                   'Rate', 'Qty']

# Store Module:- SecondDeliveryChallan
class SecondDeliveryChallan_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SecondDeliveryChallan
        fields = ['id', 'VehicleNo', 'Contractor', 'ChallanDate', 'Transport', 'EWayBillNo',
                            'PoNo', 'Ref_Person', 'LrNo', 'PoDate', 'Department', 'Remark', 
                            'AssessableValue', 'CGST', 'SGST', 'IGST', 'GrandTotal']

# Store Module:- DC_GRN
class DC_GRN_Serializer(serializers.ModelSerializer):
    class Meta:
        model = DC_GRN
        fields = fields = fields = [
    'id', 'GrnNo', 'GrnDate', 'GrnTime', 'ChallanNo', 'ChallanDate', 
    'InvoiceNo', 'InvoiceDate', 'VehicleNo', 'LrNo', 'Transporter', 
    'PreparedBy', 'CheckedBy', 'Remark', 'DeliveryInTime', 'QcCheck'
]


##testing 
class MainGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainGroup
        fields = ['id', 'name']

class ItemGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemGroup
        fields = ['id', 'name']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTable
        fields = ['id', 'main_group', 'item_group', 'name', 'age', 'part_no']
        read_only_fields = ['part_no']

# serializers.py
from rest_framework import serializers
from .models import ItemTable, MainGroup, ItemGroup

class ItemSerializer(serializers.ModelSerializer):
    main_group = serializers.CharField()  # Accepts main group as a string
    item_group = serializers.CharField()   # Accepts item group as a string

    class Meta:
        model = ItemTable
        fields = ['id', 'main_group', 'item_group', 'name', 'age', 'part_no']

    def create(self, validated_data):
        main_group_name = validated_data.pop('main_group')
        item_group_name = validated_data.pop('item_group')

        # Get or create the MainGroup instance
        main_group, _ = MainGroup.objects.get_or_create(name=main_group_name)
        # Get or create the ItemGroup instance
        item_group, _ = ItemGroup.objects.get_or_create(name=item_group_name)

        # Create the Item instance
        item = ItemTable.objects.create(main_group=main_group, item_group=item_group, **validated_data)
        return item

    def update(self, instance, validated_data):
        main_group_name = validated_data.pop('main_group', None)
        item_group_name = validated_data.pop('item_group', None)

        if main_group_name:
            main_group, _ = MainGroup.objects.get_or_create(name=main_group_name)
            instance.main_group = main_group
        
        if item_group_name:
            item_group, _ = ItemGroup.objects.get_or_create(name=item_group_name)
            instance.item_group = item_group

        # Only update name and age
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)

        # Do not change part_no if it's not in validated_data
        instance.save()
        return instance


#################
from rest_framework import serializers
from .models import GrnGenralDetail, NewGrnList, GrnGst, GrnGstTDC, RefTC

class NewGrnListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewGrnList
        fields = ["PoNo", "Date", "ItemNoCode", "Description", "Rate", "PoQty", "BalQty", "ChalQty", "GrnQty", "ShortExcessQty", "UnitCode", "Total", "HeatNo", "MfgDate"]

class GrnGstSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrnGst
        fields = ["ItemCode", "HSN", "PoRate", "DiscRate", "Qty", "Discount", "PackAmt", "TransAmt", "AssValue", "CGST", "SGST", "IGST", "VAT", "CESS"]

class GrnGstTDCSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrnGstTDC
        fields = ["assessable_value", "packing_forwarding_charges", "transport_charges", "insurance", "installation_charges", "other_charges", "Tds", "cgst", "sgst", "igst", "vat", "cess_amount", "tcs_amount", "grand_total"]

class RefTCSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefTC
        fields = ["ItemCode", "ItemDesc", "MillTcName", "MillTcNo", "MillTcDate", "Location"]

class GrnGenralDetailSerializer(serializers.ModelSerializer):
    # Make these fields optional
    NewGrnList = NewGrnListSerializer(many=True, required=False)
    GrnGst = GrnGstSerializer(many=True, required=False)
    GrnGstTDC = GrnGstTDCSerializer(many=True, required=False)
    RefTC = RefTCSerializer(many=True, required=False)

    class Meta:
        model = GrnGenralDetail
        fields = '__all__'

    def create(self, validated_data):
        # Pop data from validated_data and provide empty list as default if not provided
        grn_newgrnlist_data = validated_data.pop('NewGrnList', [])
        grn_gst_data = validated_data.pop('GrnGst', [])
        grn_gst_tdc_data = validated_data.pop('GrnGstTDC', [])
        ref_tc_data = validated_data.pop('RefTC', [])

        # Create the GrnGenralDetail instance
        grn_general = GrnGenralDetail.objects.create(**validated_data)

        # Create related instances if data exists
        for newgrnlist_data in grn_newgrnlist_data:
            NewGrnList.objects.create(New_MRN_Detail=grn_general, **newgrnlist_data)

        for gst_data in grn_gst_data:
            GrnGst.objects.create(New_MRN_Detail=grn_general, **gst_data)

        for tdc_data in grn_gst_tdc_data:
            GrnGstTDC.objects.create(New_MRN_Detail=grn_general, **tdc_data)

        for ref_data in ref_tc_data:
            RefTC.objects.create(New_MRN_Detail=grn_general, **ref_data)

        return grn_general

    def update(self, instance, validated_data):
        # Pop data from validated_data and handle if it's missing (None by default)
        grn_newgrnlist_data = validated_data.pop('NewGrnList', None)
        grn_gst_data = validated_data.pop('GrnGst', None)
        grn_gst_tdc_data = validated_data.pop('GrnGstTDC', None)
        ref_tc_data = validated_data.pop('RefTC', None)

        # Update GrnGenralDetail fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Handle related fields if they exist in the request data
        if grn_newgrnlist_data is not None:
            instance.NewGrnList.all().delete()
            for newgrnlist_data in grn_newgrnlist_data:
                NewGrnList.objects.create(New_MRN_Detail=instance, **newgrnlist_data)

        if grn_gst_data is not None:
            instance.GrnGst.all().delete()
            for gst_data in grn_gst_data:
                GrnGst.objects.create(New_MRN_Detail=instance, **gst_data)

        if grn_gst_tdc_data is not None:
            instance.GrnGstTDC.all().delete()
            for tdc_data in grn_gst_tdc_data:
                GrnGstTDC.objects.create(New_MRN_Detail=instance, **tdc_data)

        if ref_tc_data is not None:
            instance.RefTC.all().delete()
            for ref_data in ref_tc_data:
                RefTC.objects.create(New_MRN_Detail=instance, **ref_data)

        return instance


# Fetch Code for PurchaseGRN
from rest_framework import serializers
from .models import GeneralDetails

class GeneralDetailsLimitedSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralDetails
        fields = ['id', 'GE_No', 'Supp_Cust', 'Select', 'ChallanNo', 'InVoiceNo', 'EWayBillNo', 'VehicleNo', 'Transporter']


# Fetch PO Item
from rest_framework import serializers
from Purchase.models import PurchasePO, ItemDetail, GSTDetails

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDetail
        fields = '__all__'

class GSTDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GSTDetails
        fields = '__all__'

class PurchasePOSerializer(serializers.ModelSerializer):
    Item_Detail_Enter = ItemDetailSerializer(many=True)
    Gst_Details = GSTDetailSerializer(many=True)

    class Meta:
        model = PurchasePO
        fields = ['PoNo', 'PoDate', 'Item_Detail_Enter', 'Gst_Details']




# New Material Issue Serializer
from .models import MaterialChallan
from .models import MaterialChallanTable

class MaterialChallanTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialChallanTable
        fields = ['ItemDescription', 'Stock', 'Qty', 'Machine', 'NatureOfWork', 'MrnNo', 'CoilNo', 'Employee', 'Dept']

class MaterialChallanSerializer(serializers.ModelSerializer):
    MaterialChallanTable = MaterialChallanTableSerializer(many=True)

    class Meta:
        model = MaterialChallan
        fields = '__all__'
        

    def create(self, validated_data):
        Material_Table_data = validated_data.pop('MaterialChallanTable')
        Material_Issue_details = MaterialChallan.objects.create(**validated_data)

        for item_data in Material_Table_data:
            MaterialChallanTable.objects.create(MaterialChallanDetail=Material_Issue_details, **item_data)

        return Material_Issue_details

    def update(self, instance, validated_data):
        Material_Table_data = validated_data.pop('MaterialChallanTable', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if Material_Table_data:
            instance.MaterialChallanTable.all().delete()
            for item_data in Material_Table_data:
                MaterialChallanTable.objects.create(MaterialChallanDetail=instance, **item_data)

        return instance
    


# New Gate Entry:- Fetch Supplier with PDF
from rest_framework import serializers
from All_Masters.models import Item as Item2
from Purchase.models import PurchasePO

class PurchasePOSerializer2(serializers.ModelSerializer):
    class Meta:
        model = PurchasePO
        fields = ['PoNo', 'Type', 'CodeNo']

class ItemSearchResultSerializer(serializers.Serializer):
    Name = serializers.CharField()
    number = serializers.CharField()
    Type = serializers.CharField()
    PoNo = serializers.CharField()
    pdf_link = serializers.SerializerMethodField()

    def get_pdf_link(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/Purchase/PoOrder/pdf/{obj["po_id"]}/')



# New DC GRN Serilaizer
from .models import NewDCgrn, NewDCgrnTable

class NewDCgrnTableSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = NewDCgrnTable
        fields = ['DCno', 'Date', 'ItemCode', 'Description', 'Rate', 'DCqty', 'Balqty', 'Chalqty', 'GRNqty', 'ShortExcessqty', 'UnitCode', 'Total', 'HeatCode', 'Remark']

class NewDcgrnSerilaizer(serializers.ModelSerializer):
    NewDCgrnTable = NewDCgrnTableSerilaizer(many=True)
    class Meta:
        model = NewDCgrn
        fields = '__all__'

    def create(self, validated_data):
        NewDC_grn_Table_data = validated_data.pop('NewDCgrnTable')
        NewDC_grn_details = NewDCgrn.objects.create(**validated_data)

        for item_data in NewDC_grn_Table_data:
            NewDCgrnTable.objects.create(NewDCgrnDetail=NewDC_grn_details, **item_data)

        return NewDC_grn_details

    def update(self, instance, validated_data):
        NewDC_grn_Table_data = validated_data.pop('NewDCgrnTable', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if NewDC_grn_Table_data:
            instance.NewDCgrnTable.all().delete()
            for item_data in NewDC_grn_Table_data:
                NewDCgrnTable.objects.create(NewDCgrnDetail=instance, **item_data)

        return instance


# 57-F4 GRN(Inward Challan)
from .models import InwardChallan2, InwardChallanTable, InwardChallanGSTDetails
class InwardChallanTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = InwardChallanTable
        fields = ['OutNo', 'OutDate', 'ItemDescription', 'OutIn', 'Unit', 'OutQty', 'BalQty', 'ChallanQty', 'InQtyNOS', 'InQtyKg', 'JwRate']

class InwardChallanGSTDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InwardChallanGSTDetails
        fields = ['ItemCode', 'SACCode', 'PORate', 'RateType', 'Qty', 'Discount', 'PackAmt', 'TransAmt', 'AssValue', 'CGST', 'SGST', 'IGST']

class InwardChallanSerializer(serializers.ModelSerializer):
    InwardChallanTable = InwardChallanTableSerializer(many=True)
    InwardChallanGSTDetails = InwardChallanGSTDetailsSerializer(many=True)

    class Meta:
        model = InwardChallan2
        fields = '__all__'

    def create(self, validated_data):
        Inward_Challan_Table_data = validated_data.pop('InwardChallanTable')
        Inward_Challan_GST_Detail_data = validated_data.pop('InwardChallanGSTDetails')
        Inward_Challan_details = InwardChallan2.objects.create(**validated_data)

        for item_data in Inward_Challan_Table_data:
            InwardChallanTable.objects.create(InwardChallanDetail=Inward_Challan_details, **item_data)

        for item_data in Inward_Challan_GST_Detail_data:
            InwardChallanGSTDetails.objects.create(InwardChallanDetail=Inward_Challan_details, **item_data)

        return Inward_Challan_details

    def update(self, instance, validated_data):
        Inward_Challan_Table_data = validated_data.pop('InwardChallanTable', None)
        Inward_Challan_GST_Detail_data = validated_data.pop('InwardChallanGSTDetails', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if Inward_Challan_Table_data:
            instance.InwardChallanTable.all().delete()
            for item_data in Inward_Challan_Table_data:
                InwardChallanTable.objects.create(InwardChallanDetail=instance, **item_data)

        if Inward_Challan_GST_Detail_data:
            instance.InwardChallanGSTDetails.all().delete()
            for item_data in Inward_Challan_GST_Detail_data:
                InwardChallanGSTDetails.objects.create(InwardChallanGSTDetail=instance, **item_data)

        return instance
    


# Subcon GRN:- JobWork Inward-Challan
from .models import JobworkInwardChallan, JobworkInwardChallanTable
class JobworkInwardChallanTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobworkInwardChallanTable
        fields = ['ItemCode', 'Operation', 'ChallanQty', 'GRNQty', 'MaterialRate', 'HeatNo', 'CustHeatNo', 'ParticularNatureOfProcess']

class JobworkInwardChallanSerializer(serializers.ModelSerializer):
    JobworkInwardChallanTable = JobworkInwardChallanTableSerializer(many=True)

    class Meta:
        model = JobworkInwardChallan
        fields = '__all__'

    def create(self, validated_data):
        Job_Inward_Challan_Table_data = validated_data.pop('JobworkInwardChallanTable')
        Job_Inward_Challan_details = JobworkInwardChallan.objects.create(**validated_data)

        for item_data in Job_Inward_Challan_Table_data:
            JobworkInwardChallanTable.objects.create(JobworkInwardChallanDetail=Job_Inward_Challan_details, **item_data)

        return Job_Inward_Challan_details

    def update(self, instance, validated_data):
        Job_Inward_Challan_Table_data = validated_data.pop('JobworkInwardChallanTable', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if Job_Inward_Challan_Table_data:
            instance.JobworkInwardChallanTable.all().delete()
            for item_data in Job_Inward_Challan_Table_data:
                JobworkInwardChallanTable.objects.create(JobworkInwardChallanDetail=instance, **item_data)

        return instance
    

from rest_framework import serializers
from .models import FGMovement

class FGMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = FGMovement
        fields = [
            'id', 'trn_no', 'date', 'fg_item_code', 'fg_item_name', 
            'fg_item_description', 'operation', 'ok_qty', 'rework_qty', 
            'reject_qty', 'heat_code', 'stock_view', 'remark',
            'created_by', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'trn_no', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        # Set the created_by field to the current user
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)


from All_Masters.models import BOMItem
from Production.models import ProductionEntry

# class WipSerializer(serializers.ModelSerializer):
#     # item_part_code = serializers.CharField(source='item.Part_Code', read_only=True)
#     part_code=serializers.CharField(source='item.Part_Code', read_only=True)
#     Name_Description = serializers.CharField(source='item.Name_Description', read_only=True)
#     part_no=serializers.CharField(source='item.part_no',read_only=True)
#     rework_qty = serializers.SerializerMethodField()
#     reject_qty = serializers.SerializerMethodField()

#     class Meta:
#         model= BOMItem
#         fields=['part_code','part_no','Name_Description','OPNo','Operation','PartCode','rework_qty',
#             'reject_qty','WipWt','WipRate']
        
#     def get_rework_qty(self, obj):
#         # Match based on item.Part_Code and Operation
#         part_code = obj.item.Part_Code
#         operation = obj.Operation
#         entries = ProductionEntry.objects.filter(item=part_code, operation=operation)

#         total = sum(int(e.rework_qty or 0) for e in entries)
#         return total

#     def get_reject_qty(self, obj):
#         part_code = obj.item.Part_Code
#         operation = obj.Operation
#         entries = ProductionEntry.objects.filter(item=part_code, operation=operation)

#         total = sum(int(e.reject_qty or 0) for e in entries)
#         return total

class WipSerializer(serializers.ModelSerializer):
    part_code = serializers.CharField(source='item.Part_Code', read_only=True)
    Name_Description = serializers.CharField(source='item.Name_Description', read_only=True)
    part_no = serializers.CharField(source='item.part_no', read_only=True)
    rework_qty = serializers.SerializerMethodField()
    reject_qty = serializers.SerializerMethodField()
    total_rework_qty = serializers.SerializerMethodField()  # ✅ new field
    total_reject_qty = serializers.SerializerMethodField()  # ✅ optional

    class Meta:
        model = BOMItem
        fields = [
            'part_code', 'part_no', 'Name_Description',
            'OPNo', 'Operation', 'PartCode',
            'rework_qty', 'reject_qty',
            'total_rework_qty', 'total_reject_qty',
            'WipWt', 'WipRate'
        ]

    def get_rework_qty(self, obj):
        part_code = obj.item.Part_Code
        operation = obj.Operation
        entries = ProductionEntry.objects.filter(item=part_code, operation=operation)

        return sum(int(e.rework_qty or 0) for e in entries)

    def get_reject_qty(self, obj):
        part_code = obj.item.Part_Code
        operation = obj.Operation
        entries = ProductionEntry.objects.filter(item=part_code, operation=operation)

        return sum(int(e.reject_qty or 0) for e in entries)

    def get_total_rework_qty(self, obj):
        part_code = obj.item.Part_Code
        entries = ProductionEntry.objects.filter(item=part_code)

        return sum(int(e.rework_qty or 0) for e in entries)

    def get_total_reject_qty(self, obj):
        part_code = obj.item.Part_Code
        entries = ProductionEntry.objects.filter(item=part_code)
        return sum(int(e.reject_qty or 0) for e in entries)
