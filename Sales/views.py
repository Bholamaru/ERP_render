from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from .models import onwardchallan
from .models import transportdetails
from .models import vehicaldetails
from .models import outwardchallan
from .serializers import OnwardChallanSerializer
from .serializers import transportdetailsSerializer
from .serializers import vehicaldetailsSerializer
from .serializers import outwardchallanSerializer
from .utils import create_challanNumber
from All_Masters.models import Item as Item2
from Purchase.serializers import ItemSerializer, ItemDetailSerializer
from Purchase.models import PurchasePO
from django.db.models import Q


class OnwardChallanViewSet(viewsets.ModelViewSet):
    queryset = onwardchallan.objects.all()
    serializer_class = OnwardChallanSerializer
class transportdetailsview(viewsets.ModelViewSet):
    queryset=transportdetails.objects.all()
    serializer_class=transportdetailsSerializer

class vehicaldetailsview(viewsets.ModelViewSet):
    queryset=vehicaldetails.objects.all()
    serializer_class=vehicaldetailsSerializer
class outwardchallanview(viewsets.ModelViewSet):
    queryset=outwardchallan.objects.all()
    serializer_class=outwardchallanSerializer


class OnwardChallanViewSet(viewsets.ModelViewSet):
    queryset         = onwardchallan.objects.all()
    serializer_class = OnwardChallanSerializer





class deletechallan(APIView):
    def delete(self, request,id):
        # challan_no = request.data.get('challan_no')
        # if not challan_no:
        #     return Response({'error': 'challan_no is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            challan = onwardchallan.objects.get(challan_no=id)
            challan.delete()
            return Response({'message': f'Challan {id} deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except onwardchallan.DoesNotExist:
            return Response({'error': 'Challan not found'}, status=status.HTTP_404_NOT_FOUND)


class generate_unique_challan_number(APIView):
    def get(self, request):
        try:
            challan_no = create_challanNumber()
            return Response({"Challan_no" : challan_no}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class deletetransportdetails(APIView):
    def delete(self,request,name):
        try:
            transport_name=transportdetails.objects.get(transport_name=name)
            transport_name.delete()
            return Response({'message': f'transport_name {name} deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except transportdetails.DoesNotExist:
            return Response({'error': 'transport_name not found'}, status=status.HTTP_404_NOT_FOUND)


        
class edittransportdetails(APIView):
    def put(self, request, name):
        try:
            # Find the transportdetails by transport_name
            transport_obj = transportdetails.objects.get(transport_name=name)
        except transportdetails.DoesNotExist:
            return Response({'error': 'transport_name not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Get new EWAY_bill_no from request body
        new_eway_bill_no = request.data.get('EWAY_bill_no')
        if not new_eway_bill_no:
            return Response({'error': 'EWAY_bill_no is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Update
        transport_obj.EWAY_bill_no = new_eway_bill_no
        transport_obj.save()

        return Response({
            'message': f'transport_name {name} updated successfully',
            'transport_name': transport_obj.transport_name,
            'EWAY_bill_no': transport_obj.EWAY_bill_no,
            'serial_no': transport_obj.serial_no,
        }, status=status.HTTP_200_OK)

class editvehicaldetails(APIView):
    def put(self, request, vehical_no):
        try:
            vehicle = vehicaldetails.objects.get(vehical_no=vehical_no)
        except vehicaldetails.DoesNotExist:
            return Response({'error': 'Vehicle not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = vehicaldetailsSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class deletevehicaldetails(APIView):
    def delete(self,request,name):
        try:
            vehical_no=vehicaldetails.objects.get(vehical_no=name)
            vehical_no.delete()
            return Response({'message':f'vehical_no {name} deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except transportdetails.DoesNotExist:
            return Response({'error':'vehical_no not found'}, status=status.HTTP_404_NOT_FOUND)


class purchaseview(APIView):
    def post(self, request):
        
        purchase_order = request.data.get('purchase_order')
        item_code = request.data.get('item_code')
        description = request.data.get('description')
        quantity = request.data.get('quantity')
        unit_price = request.data.get('unit_price')
        total_price = request.data.get('total_price')

    
        if not purchase_order or not item_code:
            return Response(
                {"error": "purchase_order and item_code are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        queryset = Item2.objects.all()
        queryset = queryset.filter(purchase_order=purchase_order, item_code=item_code)

        if description:
            queryset = queryset.filter(description__icontains=description)
        if quantity:
            queryset = queryset.filter(quantity=quantity)
        if unit_price:
            queryset = queryset.filter(unit_price=unit_price)
        if total_price:
            queryset = queryset.filter(total_price=total_price)

        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class challanview(APIView):
    def get(self, request):
        challan_no = request.query_params.get('challan_no')
        if not challan_no:
            return Response({"error": "challan_no parameter is required."}, status=400)

        try:
            challan = onwardchallan.objects.get(challan_no=challan_no)
        except onwardchallan.DoesNotExist:
            return Response({"error": "Challan not found."}, status=404)

        serializer = OnwardChallanSerializer(challan)
        return Response(serializer.data)
    
from Purchase.models import NewJobWorkItemDetails
from Purchase.serializers import NewJobWorkItemDetailsSerializer

# class inwardchallanview(APIView):
#     def get(self, request):
#         supplier = request.query_params.get('supplier')
#         if not supplier:
#             return Response({"error": "supplier parameter is required."}, status=400)

#         supplier = supplier.strip()
#         purchase_orders = PurchasePO.objects.filter(
#             Q(Supplier__icontains=supplier) |
#             Q(Supplier__iexact=supplier)
#         )
#         if not purchase_orders.exists():
#             return Response(
#                 {"error": f"No PurchasePO found for supplier '{supplier}'"},
#                 status=404
#             )

#         results = []
#         all_details = []

#         for po in purchase_orders:
#             # 1) Items on this PO
#             items_qs = po.items.all()
#             items_data = ItemSerializer(items_qs, many=True).data

#             # 2) Details on this PO
#             detail_qs = po.Item_Detail_Enter.all()  # or use the related_name you set
#             details_data = NewJobWorkItemDetailsSerializer(detail_qs, many=True).data

#             # collect into the per‑PO results
#             results.append({
#                 "purchase_order_no": po.PoNo,
#                 "items": items_data,
#                 "item_details": details_data,      # <-- this is already an array
#             })

#             # also flatten into a single array if you need that
#             all_details.extend(details_data)
#             all_details.extend(items_data)

#         return Response({
#             "supplier": supplier,
#             "results": results,                  # list of per‑PO dicts
#             "all_item_details": all_details,     # flat list of every detail
#         }, status=status.HTTP_200_OK)
    

class supplierview(APIView):
    def get(self, request):
        supplier = request.query_params.get('supplier')
        if not supplier:
            return Response({"error": "supplier parameter is required."}, status=400)

        # Filter onwardchallan by vendor name
        challans = onwardchallan.objects.filter(vender__iexact=supplier)

        if not challans.exists():
            return Response({"error": f"No challans found for supplier '{supplier}'"}, status=404)

        serializer = OnwardChallanSerializer(challans, many=True)
        return Response({
            "supplier": supplier,
            "challans": serializer.data
        }, status=status.HTTP_200_OK)


from django.template.loader import get_template
from django.shortcuts import render,get_object_or_404,HttpResponse
from weasyprint import HTML
def generate_onwardchallan_pdf(request, pk):
    challan = get_object_or_404(onwardchallan, pk=pk)
    items = challan.items.all()

    total=0
    for item in items:
        item.value = (item.qtyNo or 1) * (item.wRate or 1)
        total=total+item.value
    challan.Amount=total

    context = {
        'challan': challan,
        'items': items,
    }

    template = get_template('Sales/onwardchallan_details.html')
    html_content = template.render(context)
    pdf_file = HTML(string=html_content).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="onwardchallan_{pk}.pdf"'
    return response



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from Purchase.models import *

class inwardchallanview(APIView):
    def get(self, request):
        supplier = request.query_params.get('supplier')
        if not supplier:
            return Response({"error": "supplier parameter is required."}, status=400)

        supplier = supplier.strip()
        purchase_orders = NewJobWorkPoInfo.objects.filter(
            Q(Supplier__icontains=supplier) |
            Q(Supplier__iexact=supplier)
        )
        if not purchase_orders.exists():
            return Response(
                {"error": f"No NewJobWorkPoInfo found for supplier '{supplier}'"},
                status=404
            )

        results = []
        all_details = []

        for po in purchase_orders:
            
            item_details_qs = po.Item_Detail_Enter.all()
            gst_details_qs = po.Gst_Details.all()
            schedule_line_qs = po.Schedule_Line.all()
            ship_to_add_qs = po.Ship_To_Add.all()

            items_data = NewJobWorkItemDetailsSerializer(item_details_qs, many=True).data
            # gst_data = NewJobWorkGstDetailsSerializer(gst_details_qs, many=True).data
            # schedule_data = NewJobWorkScheduleLineSerializer(schedule_line_qs, many=True).data
            # ship_to_data = NewJobWorkShipToAddSerializer(ship_to_add_qs, many=True).data

            results.append({
                "po_no": po.PoNo,
                "po_type": po.PoType,
                "supplier": po.Supplier,
                "po_date": po.PoDate,
                "items": items_data,
                # "gst_details": gst_data,
                # "schedule_lines": schedule_data,
                # "ship_to_address": ship_to_data,
            })

            # Flatten all details if needed
            all_details.extend(items_data)
            # all_details.extend(gst_data)
            # all_details.extend(schedule_data)
            # all_details.extend(ship_to_data)

        return Response({
            "supplier": supplier,
            "results": results,
            "all_details": all_details,
        }, status=status.HTTP_200_OK)




# class inwardchallanview(APIView):
#     def get(self, request):
#         supplier = request.query_params.get('supplier')

#         if not supplier:
#             return Response({"error": "supplier parameter is required."}, status=400)

#         supplier = supplier.strip()
#         purchase_orders = NewJobWorkPoInfo.objects.filter(
#             Q(Supplier__icontains=supplier) |
#             Q(Supplier__iexact=supplier)
#         )

#         if not purchase_orders.exists():
#             return Response(
#                 {"error": f"No NewJobWorkPoInfo found for supplier '{supplier}'"},
#                 status=404
#             )

#         results = []
#         all_details = []

#         for po in purchase_orders:
           
#             item_details_qs = po.Item_Detail_Enter.filter(item_type__iexact="FG")

#             items_data = NewJobWorkItemDetailsSerializer(item_details_qs, many=True).data

#             # Skip PO if no FG items
#             if not items_data:
#                 continue

#             results.append({
#                 "po_no": po.PoNo,
#                 "po_type": po.PoType,
#                 "supplier": po.Supplier,
#                 "po_date": po.PoDate,
#                 "items": items_data,
#             })

#             all_details.extend(items_data)

#         return Response({
#             "supplier": supplier,
#             "item_type": "FG",   # Always FG
#             "results": results,
#             "all_details": all_details,
#         }, status=status.HTTP_200_OK)



class InwardChallanRMView(APIView):
    def get(self, request):
        supplier = request.query_params.get('supplier')

        if not supplier:
            return Response({"error": "supplier parameter is required."}, status=400)

        supplier = supplier.strip()
        purchase_orders = NewJobWorkPoInfo.objects.filter(
            Q(Supplier__icontains=supplier) |
            Q(Supplier__iexact=supplier)
        )

        if not purchase_orders.exists():
            return Response(
                {"error": f"No NewJobWorkPoInfo found for supplier '{supplier}'"},
                status=404
            )

        results = []
        # all_details = []

        for po in purchase_orders:
            #  Always filter items with item_type = 'RM'
            item_details_qs = po.Item_Detail_Enter.filter(item_type__iexact="RM")

            items_data = NewJobWorkItemDetailsSerializer(item_details_qs, many=True).data

            # Skip PO if no RM items
            if not items_data:
                continue

            results.append({
                "po_no": po.PoNo,
                "po_type": po.PoType,
                "supplier": po.Supplier,
                "po_date": po.PoDate,
                "items": items_data,
            })

            # all_details.extend(items_data)

        return Response({
            "supplier": supplier,
            "item_type": "RM",   # Always RM
            "results": results,
            # "all_details": all_details,
        }, status=status.HTTP_200_OK)

from .utils import create_reworknumber
class generate_unique_rework_number(APIView):
    def get(self, request):
        try:
            rework_no = create_reworknumber()
            return Response({"Rework_no": rework_no}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum, F, Value, FloatField
from django.db.models.functions import Cast, Coalesce
from collections import defaultdict

from Store.models import MaterialChallan, MaterialChallanTable
from Production.models import   ProductionEntry


def safe_float(value):
    try:
        return float(value)
    except:
        return 0


class ItemFullReport(APIView):
    """
    ONE API = HeatNo Summary + Production Summary
    """

    def get(self, request):
        item = request.query_params.get("item")
        operation = request.query_params.get("operation")
        prod_no = request.query_params.get("prod_no")

        if not item:
            return Response(
                {"error": "item parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # =====================================================
        #         🔹 1) Heat No Wise Qty Summary
        # =====================================================
        challans = MaterialChallan.objects.filter(Item__icontains=item)

        if not challans.exists():
            heat_qty_list = []
        else:
            heat_qty_data = (
                MaterialChallanTable.objects
                .filter(MaterialChallanDetail__in=challans)
                .values("HeatNo")
                .annotate(
                    total_qty=Sum(
                        Coalesce(Cast(F("Qty"), FloatField()), Value(0.0))
                    )
                )
                .order_by("HeatNo")
            )

            heat_qty_list = [
                {
                    "HeatNo": entry["HeatNo"] if entry["HeatNo"] else "No HeatNo",
                    "Qty": entry["total_qty"]
                }
                for entry in heat_qty_data
            ]

        # =====================================================
        #         🔹 2) Production Operation-wise Lot Summary
        # =====================================================
        entries = ProductionEntry.objects.filter(item=item)

        if operation:
            entries = entries.filter(operation=operation)

        if prod_no:
            entries = entries.filter(Prod_no=prod_no)

        prod_result = {}

        for e in entries:
            opno = e.operation
            lot = (e.lot_no or "").split("|")[0]
            qty = safe_float(e.prod_qty or 0)

            if opno not in prod_result:
                prod_result[opno] = defaultdict(float)

            prod_result[opno][lot] += qty

        prod_output = {
            op: [{"lot_no": lot, "prod_qty": qty} for lot, qty in lots.items()]
            for op, lots in prod_result.items()
        }

        # =====================================================
        #              🔹 FINAL COMBINED RESPONSE
        # =====================================================

        return Response({
            "item": item,
            "heat_qty_summary": heat_qty_list,
            "production_summary": prod_output
        }, status=status.HTTP_200_OK)



from .serializers import *
from .models import *
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            print("❌ VALIDATION ERRORS →", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class NewsalesOrederViewSet(viewsets.ModelViewSet):
    queryset = NewSalesOrder.objects.all()
    serializer_class= NewSalesOrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print("❌ SERIALIZER ERRORS:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



from All_Masters.models import Item
class CustomerItemListView(APIView):
    def get(self, request):
        customers = Item.objects.filter(type='Customer')
        serializer = ItemSerializer(customers, many=True)
        return Response({
            "message": "Customer type data fetched successfully",
            "count": customers.count(),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    


from All_Masters.models import ItemTable,TaxDetails
from All_Masters.serializers import ItemTableSerializer2

class ItemTableListView(APIView):
    def get(self, request):
        items = ItemTable.objects.all().order_by('id')
        serializer = ItemTableSerializer2(items, many=True)

        data = serializer.data  # serialized itemtable data

        # attach tax details manually
        for item in data:
            hsn_code = item.get("HSN_SAC_Code")

            if hsn_code:
                tax = TaxDetails.objects.filter(
                    HSN_SAC_Code=hsn_code
                ).values().first()
                item["tax_details"] = tax
            else:
                item["tax_details"] = None

        return Response({
            "message": "Items fetched successfully",
            "count": len(data),
            "data": data
        })


from .utils import create_invoiceno
class generate_invoice_number(APIView):
    def get(self ,request):
        try:
            invoice_no=create_invoiceno()
            return Response ({"Invoice_no": invoice_no}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# class LastOperationProdQtyAPI(APIView):

#     def get(self, request):
#         query = request.query_params.get('q', '').strip()
#         if not query:
#             return Response(
#                 {"error": 'Search query "q" is required'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         item = ItemTable.objects.filter(
#             Q(Part_Code__icontains=query) |
#             Q(part_no__icontains=query) |
#             Q(Name_Description__icontains=query)
#         ).first()

#         if not item:
#             return Response(
#                 {"error": "Item not found"},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         bom_items = BOMItem.objects.filter(item=item)

#         if not bom_items.exists():
#             return Response(
#                 {"error": "No BOM found for item"},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         last_op_data = None
#         last_op_no = -1

#         for bom in bom_items:
#             if not bom.OPNo:
#                 continue

#             try:
#                 op_no_int = int(bom.OPNo.strip())
#             except ValueError:
#                 continue

#             production = ProductionEntry.objects.filter(
#                 item__icontains=item.Part_Code,
#                 operation__startswith=bom.OPNo
#             ).order_by('-id').first()   # 🔥 latest entry for that OP

#             prod_qty = float(production.prod_qty) if production else 0.0

#             # 🔥 Pick highest OPNo
#             if op_no_int > last_op_no:
#                 last_op_no = op_no_int
#                 last_op_data = {
#                     "part_code": item.Part_Code,
#                     "part_no": item.part_no,
#                     "Name_Description": item.Name_Description,
#                     "OPNo": bom.OPNo,
#                     "Operation": bom.Operation,
#                     "prod_qty": prod_qty
#                 }

#         if not last_op_data:
#             return Response(
#                 {"error": "No production data found"},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         return Response(
#             {"last_operation": last_op_data},
#             status=status.HTTP_200_OK
#         )


from All_Masters.models import BOMItem

class LastOperationProdQtyAPI(APIView):

    def get(self, request):
        query = request.query_params.get("q", "").strip()
        if not query:
            return Response(
                {"error": 'Search query "q" is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        item = ItemTable.objects.filter(
            Q(Part_Code__icontains=query) |
            Q(part_no__icontains=query) |
            Q(Name_Description__icontains=query)
        ).first()

        if not item:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        bom_items = BOMItem.objects.filter(item=item)

        last_op_no = -1
        last_bom = None

        # 🔥 Find LAST OPNo
        for bom in bom_items:
            if not bom.OPNo:
                continue
            try:
                op_int = int(bom.OPNo.strip())
            except ValueError:
                continue

            if op_int > last_op_no:
                last_op_no = op_int
                last_bom = bom

        if not last_bom:
            return Response({"error": "No valid OP found"}, status=status.HTTP_404_NOT_FOUND)

        # 🔥 Get production entries for LAST OP
        prod_entries = ProductionEntry.objects.filter(
            item__icontains=item.Part_Code,
            operation__startswith=last_bom.OPNo
        )

        lot_map = defaultdict(float)
        total_prod_qty = 0.0

        for e in prod_entries:
            lot = (e.lot_no or "").split("|")[0].strip()
            qty = safe_float(e.prod_qty or 0)

            lot_map[lot] += qty
            total_prod_qty += qty

        lot_list = [
            {
                "lot_no": lot,
                "prod_qty": round(qty, 3)
            }
            for lot, qty in lot_map.items()
        ]

        return Response(
            {
                "last_operation": {
                    "part_code": item.Part_Code,
                    "part_no": item.part_no,
                    "Name_Description": item.Name_Description,
                    "OPNo": last_bom.OPNo,
                    "Operation": last_bom.Operation,
                    "prod_qty": round(total_prod_qty, 3),
                    "lots": lot_list
                }
            },
            status=status.HTTP_200_OK
        )
