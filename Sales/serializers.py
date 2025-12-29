from rest_framework import serializers
from .models import onwardchallan
from .models import transportdetails
from .models import vehicaldetails
from .models import outwardchallan, OnwardChallanItem
from Store.serializers import GrnGenralDetailSerializer
from Store.models import GrnGenralDetail
from .models import *
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




from .models import Store
class OnwardChallanItemSerializer(serializers.ModelSerializer):
    grndetails=GrnGenralDetailSerializer(source='items',many=True, read_only=True)
    
    class Meta:
        model  = OnwardChallanItem
        fields = [
            "item_code", "type", "description",
            "store", "suppRefNo", "qtyNo", "qtyKg",
            "process", "pkg", "wRate", "wValue",
            "grndetails","stock",
        ]
        extra_kwargs = {
            "stock": {"write_only": True}  
        }
    

    def validate(self, attrs):
        qtyNo = attrs.get("qtyNo")
        stock = attrs.get("stock")

        try:
            qtyNo = float(qtyNo)
            stock = float(stock)
        except (TypeError, ValueError):
            raise serializers.ValidationError({"stock": "Invalid stock or quantity value."})

        if qtyNo > stock:
            raise serializers.ValidationError({
                "qtyNo": f"Quantity ({qtyNo}) cannot be greater than available stock ({stock})."
            })

        return attrs

    def create(self, validated_data):
        validated_data.pop("stock", None)  
        return OnwardChallanItem.objects.create(**validated_data)

from Store.models import NewGrnList
from decimal import Decimal
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
            "vender", "items","id"
        ]

    
    def create(self, validated_data):
        items_data = validated_data.pop("items", [])
        challan = onwardchallan.objects.create(**validated_data)

        for item_data in items_data:
            item = OnwardChallanItem.objects.create(challan=challan, **item_data)
            # Subtract qtyNo from GRNQty
            store = item.store.strip()
            qty = Decimal(item.qtyNo or 0)
            grn_items = NewGrnList.objects.filter(HeatNo__iexact=store)
            for grn_item in grn_items:
                current_qty = Decimal(grn_item.GrnQty or 0)
                grn_item.GrnQty = max(current_qty - qty, Decimal(0))
                grn_item.save(update_fields=["GrnQty"])
                print(f"✅ GRN {grn_item.id} updated: {current_qty} → {grn_item.GrnQty}")

        return challan

    def update(self, instance, validated_data):
        items_data = validated_data.pop("items", [])
        # Update challan fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Delete old items and restore their qty to GRN
        old_items = OnwardChallanItem.objects.filter(challan=instance)
        for old_item in old_items:
            store = old_item.store.strip()
            qty = Decimal(old_item.qtyNo or 0)
            grn_items = NewGrnList.objects.filter(HeatNo__iexact=store)
            for grn_item in grn_items:
                grn_item.GrnQty = Decimal(grn_item.GrnQty or 0) + qty
                grn_item.save(update_fields=["GrnQty"])
                print(f"♻️ GRN {grn_item.id} restored: +{qty}")
        old_items.delete()

        # Create new items and subtract qtyNo
        for item_data in items_data:
            item = OnwardChallanItem.objects.create(challan=instance, **item_data)
            store = item.store.strip()
            qty = Decimal(item.qtyNo or 0)
            grn_items = NewGrnList.objects.filter(HeatNo__iexact=store)
            for grn_item in grn_items:
                current_qty = Decimal(grn_item.GrnQty or 0)
                grn_item.GrnQty = max(current_qty - qty, Decimal(0))
                grn_item.save(update_fields=["GrnQty"])
                print(f"✅ GRN {grn_item.id} updated: {current_qty} → {grn_item.GrnQty}")

        return instance


    # def create(self, validated_data):
    #     items_data = validated_data.pop("items", [])
    #     challan = onwardchallan.objects.create(**validated_data)
    #     OnwardChallanItem.objects.bulk_create([
    #         OnwardChallanItem(challan=challan, **item) for item in items_data
    #     ])
    #     return challan





from rest_framework import serializers
from .models import Invoice, InvoiceItemdetails

class InvoiceItemdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItemdetails
        fields = '__all__'
        extra_kwargs = {
            'invoice': {'required': False}  
        }


class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemdetailsSerializer(many=True)  # nested items

    class Meta:
        model = Invoice
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])

        # Create main Invoice
        invoice = Invoice.objects.create(**validated_data)

        # Create related items
        for item in items_data:
            InvoiceItemdetails.objects.create(invoice=invoice, **item)

        return invoice



class NewSalesItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewSalesItemdetails
        # fields = '__all__'
        exclude = ["newsaleoreder"]


class NewSalesOrderSerializer(serializers.ModelSerializer):
    item = NewSalesItemSerializer(many=True,required=False)

    class Meta:
        model = NewSalesOrder
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('item', [])
        order = NewSalesOrder.objects.create(**validated_data)

        for item in items_data:
            NewSalesItemdetails.objects.create(
                newsaleoreder=order,
                **item
            )
        return order


# class NewSalesOrderSerializer(serializers.ModelSerializer):
#     item = NewSalesItemSerializer(many=True, read_only=True)
#     class Meta:
#         model = NewSalesOrder
#         fields = '__all__'
    
#     def create(self, validated_data):
#         items_data = validated_data.pop('item', [])
#         order = NewSalesOrder.objects.create(**validated_data)

#         for item in items_data:
#             NewSalesItemdetails.objects.create(
#                 newsaleoreder=order,
#                 **item
#             )
#         return order

from All_Masters.models import Item       
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"