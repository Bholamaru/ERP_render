
from rest_framework import serializers
from .models import ScrapRejection


class ScrapRejectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapRejection
        fields = '__all__'  # This will include all fields of the ScrapRejection model



# Production Entry
from rest_framework import serializers
from .models import ProductionEntry, MachineIdleTime

class MachineIdleTime_Detail_EnterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineIdleTime
        fields = '__all__'

class ProductionEntrySerializer(serializers.ModelSerializer):
    MachineIdleTime_Detail_Enter = MachineIdleTime_Detail_EnterSerializer(many=True, read_only=True)

    class Meta:
        model = ProductionEntry
        fields = '__all__'

class OOPurchaseSerializer(serializers.ModelSerializer):
    MachineIdleTime_Detail_Enter = MachineIdleTime_Detail_EnterSerializer(many=True)

    class Meta:
        model = ProductionEntry
        fields = '__all__'

    def create(self, validated_data):
        MachineIdleTime_Detail_Enter_data = validated_data.pop('MachineIdleTime_Detail_Enter', [])
        production_entry = ProductionEntry.objects.create(**validated_data)
        
        for MachineIdleTime_data in MachineIdleTime_Detail_Enter_data:
            MachineIdleTime_Detail = MachineIdleTime.objects.create(**MachineIdleTime_data)
            production_entry.MachineIdleTime_Detail_Enter.add(MachineIdleTime_Detail)

        return production_entry
    

# Production Entry Shift Time Serailizer :-Fetch
from All_Masters.models import Shift_Master_Model
class ProductionEntryShift(serializers.ModelSerializer):
    class Meta:
        model = Shift_Master_Model
        fields = '__all__'

# Production Entry Contractor:- Fetch
from All_Masters.models import Contractor_Master_Model
class ProductionEntryContractor(serializers.ModelSerializer):
    class Meta:
        model = Contractor_Master_Model
        fields = ['ContractorName']


# Production Entry Operator:- Fetch
from All_Masters.models import Add_New_Operator_Model
class ProductionOperatorSupervisor(serializers.ModelSerializer):
    class Meta:
        model = Add_New_Operator_Model
        fields = ['Name', 'Code', 'Type'] 


# Production Entry Fetch Unit Machine from Work Center Master
from All_Masters.models import Work_Center_Model
class ProductionEntryUnitMachine(serializers.ModelSerializer):
    class Meta: 
        model = Work_Center_Model
        fields = ['WorkCenterCode', 'WorkCenterName']




# Rework Production Entry 2
from rest_framework import serializers
from .models import ProductionEntry2, MachineIdleTime2

class MachineIdleTime_Detail_EnterSerializer2(serializers.ModelSerializer):
    class Meta:
        model = MachineIdleTime2
        fields = '__all__'

class ProductionEntrySerializer2(serializers.ModelSerializer):
    MachineIdleTime_Detail_Enter = MachineIdleTime_Detail_EnterSerializer2(many=True, read_only=True)

    class Meta:
        model = ProductionEntry2
        fields = '__all__'

class OOPurchaseSerializer2(serializers.ModelSerializer):
    MachineIdleTime_Detail_Enter = MachineIdleTime_Detail_EnterSerializer2(many=True)

    class Meta:
        model = ProductionEntry2
        fields = '__all__'

    def create(self, validated_data):
        MachineIdleTime_Detail_Enter_data = validated_data.pop('MachineIdleTime_Detail_Enter', [])
        production_entry = ProductionEntry2.objects.create(**validated_data)
        
        for MachineIdleTime_data in MachineIdleTime_Detail_Enter_data:
            MachineIdleTime_Detail = MachineIdleTime2.objects.create(**MachineIdleTime_data)
            production_entry.MachineIdleTime_Detail_Enter.add(MachineIdleTime_Detail)

        return production_entry
    


# Rework Production: Rework production Entry

from rest_framework import serializers
from .models import ProductDetail2, Item2, ConsumptionDetails

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item2
        fields = ['id', 'item_desc', 'heat_code', 'rework_to_ok_qty', 'reject_to_ok_qty', 'rework_to_reject_qty']

class ConsumptionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumptionDetails
        fields = ['id', 'item_desc', 'heat_code', 'qty']

class ProductDetailSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    consumption_details = ConsumptionDetailsSerializer(many=True)
    user = serializers.StringRelatedField(read_only=True)  # Show the username in response

    class Meta:
        model = ProductDetail2
        fields = ['id', 'series', 'rework_no', 'rework_date', 'rework_time', 'machine', 'work_order', 'item_code',
                  'part_code', 'heat_code', 'rework_to_ok_qty', 'reject_to_ok_qty', 'change_fg', 'part_code2',
                  'heat_code2', 'reason_for_rework', 'quality_remark', 'operator', 'items', 'consumption_details', 'user']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None

        # Bulk create support
        if isinstance(validated_data, list):
            instances = []
            for entry in validated_data:
                items_data = entry.pop('items')
                consumption_data = entry.pop('consumption_details')
                product_detail = ProductDetail2.objects.create(user=user, **entry)

                for item in items_data:
                    Item2.objects.create(product_detail=product_detail, **item)
                for cons in consumption_data:
                    ConsumptionDetails.objects.create(product_detail=product_detail, **cons)

                instances.append(product_detail)
            return instances

        # Single create
        items_data = validated_data.pop('items')
        consumption_data = validated_data.pop('consumption_details')
        product_detail = ProductDetail2.objects.create(user=user, **validated_data)

        for item in items_data:
            Item2.objects.create(product_detail=product_detail, **item)
        for cons in consumption_data:
            ConsumptionDetails.objects.create(product_detail=product_detail, **cons)

        return product_detail

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', None)
        consumption_details_data = validated_data.pop('consumption_details', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if items_data is not None:
            instance.items.all().delete()
            for item_data in items_data:
                Item2.objects.create(product_detail=instance, **item_data)

        if consumption_details_data is not None:
            instance.consumption_details.all().delete()
            for cons_data in consumption_details_data:
                ConsumptionDetails.objects.create(product_detail=instance, **cons_data)

        return instance

    


# Production Entry Assembly:-

from rest_framework import serializers
from .models import AssemblyProductionDetails, MachineIdleTimeAss, ItemStockDetails

class MachineIdleTimeAssSerializer(serializers.ModelSerializer):  # Renamed ItemSerializer
    class Meta:
        model = MachineIdleTimeAss
        fields = ["idle_reason", "from_time", "to_time", "total_time", "supervisor_operator", "setting_part", "remark"]
        

class ItemStockDetailsSerializer(serializers.ModelSerializer):  # Renamed ConsumptionDetailsSerializer
    class Meta:
        model = ItemStockDetails
        fields = ["Item_Group", "Alt_Item", "Item_No", "Item_Code", "Desc", "Bom_Qty", "Reg_Qty", "Stock"]

from .models import ReworkReason,RejectReason

class ReworkReasonSerializer(serializers.ModelSerializer):  # Renamed ConsumptionDetailsSerializer
    class Meta:
        model = ReworkReason
        fields = ["Description", "Qty"]
    

class RejectReasonSerializer(serializers.ModelSerializer):  # Renamed ConsumptionDetailsSerializer
    class Meta:
        model = RejectReason
        fields = ["Description", "Qty"]

class AssemblyProductionDetailsSerializer(serializers.ModelSerializer):
    MachineIdleTimeAss = MachineIdleTimeAssSerializer(many=True)  # Renamed items to MachineIdleTimeAss
    ItemStockDetails = ItemStockDetailsSerializer(many=True)  # Renamed consumption_details to ItemStockDetails
    ReworkReason = ReworkReasonSerializer(many=True) 
    RejectReason = RejectReasonSerializer(many=True) 

    class Meta:
        model = AssemblyProductionDetails
        fields = '__all__'

    def create(self, validated_data):
        machine_idle_time_ass_data = validated_data.pop('MachineIdleTimeAss')
        item_stock_details_data = validated_data.pop('ItemStockDetails')
        ReworkReason_details_data = validated_data.pop('ReworkReason')
        RejectReason_details_data = validated_data.pop('RejectReason')
        assembly_production_details = AssemblyProductionDetails.objects.create(**validated_data)

        for item_data in machine_idle_time_ass_data:
            MachineIdleTimeAss.objects.create(product_detail=assembly_production_details, **item_data)

        for consumption_data in item_stock_details_data:
            ItemStockDetails.objects.create(product_detail=assembly_production_details, **consumption_data)

        for  ReworkReason_data in ReworkReason_details_data:
            ReworkReason.objects.create(product_detail=assembly_production_details, ** ReworkReason_data)
        
        for RejectReason_data in RejectReason_details_data:
            RejectReason.objects.create(product_detail=assembly_production_details, **RejectReason_data)

        return assembly_production_details

    def update(self, instance, validated_data):
        machine_idle_time_ass_data = validated_data.pop('MachineIdleTimeAss', None)
        item_stock_details_data = validated_data.pop('ItemStockDetails', None)
        ReworkReason_details_data = validated_data.pop('ReworkReason', None)
        RejectReason_details_data = validated_data.pop('RejectReason', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if machine_idle_time_ass_data:
            instance.MachineIdleTimeAss.all().delete()
            for item_data in machine_idle_time_ass_data:
                MachineIdleTimeAss.objects.create(product_detail=instance, **item_data)

        if item_stock_details_data:
            instance.ItemStockDetails.all().delete()
            for consumption_data in item_stock_details_data:
                ItemStockDetails.objects.create(product_detail=instance, **consumption_data)
        
        if ReworkReason_details_data:
            instance.ReworkReason.all().delete()
            for ReworkReason_data in ReworkReason_details_data:
                ReworkReason.objects.create(product_detail=instance, **ReworkReason_data)

        if RejectReason_details_data:
            instance.RejectReason.all().delete()
            for RejectReason_data in RejectReason_details_data:
                RejectReason.objects.create(product_detail=instance, **RejectReason_data)

        return instance

from .models import ReworkReason2,RejectReason2

class ReworkReason2Serializer(serializers.ModelSerializer):
    class Meta:
        model = ReworkReason2
        fields = '__all__'

class RejectReason2Serializer(serializers.ModelSerializer):
    class Meta:
        model = RejectReason2
        fields = '__all__'
    

# Contractor Production Entry

from rest_framework import serializers
from .models import ProductionRecord

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionRecord
        fields = "__all__"



# FG Scrap Rejection Note
from rest_framework import serializers
from .models import FGScrapDetails, FGScrapItem

class FGScrapItemSerializer(serializers.ModelSerializer):  
    class Meta:
        model = FGScrapItem
        fields = ["ItemDescription", "HeatCode", "ReworkQty", "Reason", "RejectQty", "Reason2", "ScrapWt"]

class FGScrapDetailsSerializer(serializers.ModelSerializer):
    scrap_items = FGScrapItemSerializer(many=True)  # Matches related_name in the model
    
    class Meta:
        model = FGScrapDetails
        fields = '__all__'

    def create(self, validated_data):
        scrap_items_data = validated_data.pop('scrap_items')
        scrap_detail = FGScrapDetails.objects.create(**validated_data)

        for item_data in scrap_items_data:
            FGScrapItem.objects.create(ItemDesc=scrap_detail, **item_data)

        return scrap_detail

    def update(self, instance, validated_data):
        scrap_items_data = validated_data.pop('scrap_items', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if scrap_items_data:
            instance.scrap_items.all().delete()
            for item_data in scrap_items_data:
                FGScrapItem.objects.create(ItemDesc=instance, **item_data)

        return instance


# Scrap Line Rejection Note
from rest_framework import serializers
from .models import ScrapLineRejectionNote, ScrapLineRejectionNoteDetails

class ScrapRejectSerializer(serializers.ModelSerializer):  
    class Meta:
        model = ScrapLineRejectionNoteDetails
        fields = ["ItemNo", "ScrapRejectionQty", "ReasonNote", "RejectReason", "ScrapRejectionItem","ScrapQty"]

class ScrapRejectDetailsSerializer(serializers.ModelSerializer):
    scrap_items = ScrapRejectSerializer(many=True)  # Matches related_name in the model
    
    class Meta:
        model = ScrapLineRejectionNote
        fields = '__all__'

    def create(self, validated_data):
        scrap_items_data = validated_data.pop('scrap_items')
        scrap_detail = ScrapLineRejectionNote.objects.create(**validated_data)

        for item_data in scrap_items_data:
            ScrapLineRejectionNoteDetails.objects.create(ItemDesc=scrap_detail, **item_data)

        return scrap_detail

    def update(self, instance, validated_data):
        scrap_items_data = validated_data.pop('scrap_items', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if scrap_items_data:
            instance.scrap_items.all().delete()
            for item_data in scrap_items_data:
                ScrapLineRejectionNoteDetails.objects.create(ItemDesc=instance, **item_data)

        return instance
    
# New Work Order 
from rest_framework import serializers
from .models import WorkOrderEntry

# Work Order Customer_supplier Search
from All_Masters.models import Item
class WO_Customer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'Name', 'number']

# New Work Order 
from .models import NewWorkOrderItem
class New_Work_Oder_Item_Serializer(serializers.ModelSerializer):   # Renamed items to MachineIdleTimeAss
    class Meta:
        model = NewWorkOrderItem
        fields = ["Purchase_order_detail", "item", "Description", "SO_Sch_Qty", "Bal_Qty", "Work_Order_Qty", "Remark", "Machine", "Shift", "Process", "Raw_Material"]


class WorkOrderSerializer(serializers.ModelSerializer):
    NewWorkOrderItem = New_Work_Oder_Item_Serializer(many=True)

    class Meta:
        model = WorkOrderEntry
        fields = '__all__'

    def create(self, validated_data):
        Work_Order_detail_data = validated_data.pop('NewWorkOrderItem')
        Work_Order_entry_details = WorkOrderEntry.objects.create(**validated_data)

        for item_data in Work_Order_detail_data:
            NewWorkOrderItem.objects.create(Work_Order_detail=Work_Order_entry_details, **item_data)

        return Work_Order_entry_details

    def update(self, instance, validated_data):
        Work_Order_detail_data = validated_data.pop('NewWorkOrderItem', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if Work_Order_detail_data:
            instance.NewWorkOrderItem.all().delete()
            for item_data in Work_Order_detail_data:
                NewWorkOrderItem.objects.create(Work_Order_detail=instance, **item_data)

        return instance
    

##
from rest_framework import serializers
from .models import ProductDetail2, Item2, ConsumptionDetails

class ProductDetailGetSerializer(serializers.ModelSerializer):
    part_no = serializers.SerializerMethodField()
    Part_Code = serializers.SerializerMethodField()
    Name_Description = serializers.SerializerMethodField()

    OPNo = serializers.SerializerMethodField()
    PartCode = serializers.SerializerMethodField()

    change_fg_part_no = serializers.SerializerMethodField()
    change_fg_Part_Code = serializers.SerializerMethodField()
    change_fg_Name_Description = serializers.SerializerMethodField()

    OPNo2 = serializers.SerializerMethodField()
    PartCode2 = serializers.SerializerMethodField()

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProductDetail2
        fields = [
            'Plant', 'rework_no', 'rework_date',
            'part_no', 'Part_Code', 'Name_Description',
            'OPNo', 'PartCode',
            'change_fg_part_no', 'change_fg_Part_Code', 'change_fg_Name_Description',
            'OPNo2', 'PartCode2',
            'rework_to_ok_qty', 'reject_to_ok_qty',
            'reason_for_rework', 'quality_remark', 'user'
        ]

    # Helpers
    def split_item_code(self, value, expected_parts=3):
        if value:
            parts = [x.strip() for x in value.split('|')]
            while len(parts) < expected_parts:
                parts.append("")
            return parts
        return [""] * expected_parts

    def split_part_code(self, value, expected_parts=2):
        if value:
            parts = [x.strip() for x in value.split('|')]
            while len(parts) < expected_parts:
                parts.append("")
            return parts
        return [""] * expected_parts

    # item_code
    def get_part_no(self, obj):
        return self.split_item_code(obj.item_code)[0]

    def get_Part_Code(self, obj):
        return self.split_item_code(obj.item_code)[1]

    def get_Name_Description(self, obj):
        return self.split_item_code(obj.item_code)[2]

    # part_code
    def get_OPNo(self, obj):
        return self.split_part_code(obj.part_code)[0]

    def get_PartCode(self, obj):
        return self.split_part_code(obj.part_code)[1]

    # change_fg
    def get_change_fg_part_no(self, obj):
        return self.split_item_code(obj.change_fg)[0]

    def get_change_fg_Part_Code(self, obj):
        return self.split_item_code(obj.change_fg)[1]

    def get_change_fg_Name_Description(self, obj):
        return self.split_item_code(obj.change_fg)[2]

    # part_code2
    def get_OPNo2(self, obj):
        return self.split_part_code(obj.part_code2)[0]

    def get_PartCode2(self, obj):
        return self.split_part_code(obj.part_code2)[1]


from All_Masters.models import *
class ItemdropdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTable
        fields= ['Part_Code','part_no' , 'Name_Description']

class BOMItemdropSerializer(serializers.ModelSerializer):
    item_part_code = serializers.CharField(source='item.Part_Code', read_only=True)
    class Meta:
        model = BOMItem
        fields = ['item_part_code','OPNo', 'PartCode']

