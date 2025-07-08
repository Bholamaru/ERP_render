from rest_framework import serializers
from .models import onwardchallan
from .models import transportdetails
from .models import vehicaldetails
from .models import outwardchallan, OnwardChallanItem
# from .views import generate_unique_challan_number

class OnwardChallanSerializer(serializers.ModelSerializer):
    class Meta:
        model = onwardchallan
        fields = '__all__'
class transportdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=transportdetails
        fields='__all__'
class vehicaldetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=vehicaldetails
        fields='__all__'
class outwardchallanSerializer(serializers.ModelSerializer):
    class Meta:
        model=outwardchallan
        fields='__all__'

class OnwardChallanItemSerializer(serializers.ModelSerializer):
    class Meta:
        model  = OnwardChallanItem
        fields = [
            "item_code", "type", "description",
            "store", "suppRefNo", "qtyNo", "qtyKg",
            "process", "pkg", "wRate", "wValue",
        ]

class OnwardChallanSerializer(serializers.ModelSerializer):
    items = OnwardChallanItemSerializer(many=True)

    class Meta:
        model  = onwardchallan
        fields = [
            "challan_no", "challan_date", "challan_time",
            "DC_no", "Transport_name", "vehical_no",
            "Estimated_value", "DC_date", "EWay_bill_no",
            "eway_bill_date", "rev_charges", "rec_ch_amt",
            "Eway_bill_Qty", "remarks", "plant", "series",
            "vender", "items",
        ]

    def create(self, validated_data):
        items_data = validated_data.pop("items", [])
        challan = onwardchallan.objects.create(**validated_data)
        OnwardChallanItem.objects.bulk_create([
            OnwardChallanItem(challan=challan, **item) for item in items_data
        ])
        return challan