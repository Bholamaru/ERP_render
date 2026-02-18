from django.db import models
from django.core.validators import RegexValidator
from All_Masters.models import Item as Item2

from decimal import Decimal

class outwardchallan(models.Model):
    Plant = models.CharField(max_length=100, blank=True, null=True)
    Series = models.CharField(max_length=100, blank=True, null=True)
    Vendor = models.CharField(max_length=100, blank=True, null=True)
    challan_no = models.CharField(max_length=100, blank=True, null=True)  # e.g., F6252600001
    challan_date = models.CharField(max_length=100, blank=True, null=True)
    challan_time = models.CharField(max_length=100, blank=True, null=True)
    DcNo = models.CharField(max_length=100, blank=True, null=True)
    transport_name = models.CharField(max_length=100, blank=True, null=True)
    vehicle_no = models.CharField(max_length=100, blank=True, null=True)
    estimated_value = models.CharField(max_length=100, blank=True, null=True)
    DcDate = models.CharField(max_length=100, blank=True, null=True)
    eway_bill_no = models.CharField(max_length=100, blank=True, null=True)
    eway_bill_date = models.CharField(max_length=100, blank=True, null=True)
    rev_charges = models.CharField(max_length=100, blank=True, null=True)
    rev_charges_amount = models.CharField(max_length=100, blank=True, null=True)
    eway_bill_qty = models.CharField(max_length=100, blank=True, null=True)
    remarknote = models.CharField(max_length=100, blank=True, null=True)
    ship_to_add_code = models.CharField(max_length=100, blank=True, null=True)
    challan_due_date = models.CharField(max_length=100, blank=True, null=True)
    SelectWorkOrder = models.CharField(max_length=100, blank=True, null=True)
    assessable_value = models.CharField(max_length=100, blank=True, null=True)
    cgst = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    sgst = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    igst = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    grand_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    lr_no = models.CharField(max_length=100, blank=True, null=True)
    lr_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return f"Challan {self.challan_no} - {self.vendor_name}"
class ChallanCounter(models.Model):
    last_number = models.IntegerField(default=0)
    def __str__(self):
        return f"Last Used: {self.last_number}"
    
# trial code

class onwardchallan(models.Model):
    challan_no        = models.CharField(max_length=20, unique=True, blank=True, null=True)
    challan_date      = models.DateField()
    challan_time      = models.TimeField()
    DC_no             = models.CharField(max_length=50, blank=True)
    Transport_name    = models.CharField(max_length=100, blank=True)
    vehical_no        = models.CharField(max_length=20, blank=True)
    Estimated_value   = models.CharField(max_length=50, blank=True)
    DC_date           = models.DateField()
    EWay_bill_no      = models.CharField(max_length=50, blank=True)
    eway_bill_date    = models.DateField(null=True, blank=True)
    REV_CHARGES_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
    rev_charges       = models.CharField(max_length=1, choices=REV_CHARGES_CHOICES, default='N')
    rec_ch_amt        = models.CharField(max_length=50, blank=True)
    Eway_bill_Qty     = models.CharField(max_length=50, blank=True, null=True)
    remarks           = models.CharField(max_length=100, blank=True, null=True)
    plant             = models.CharField(max_length=30, blank=True, default='')
    series            = models.CharField(max_length=30, blank=True)
    vender            = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.challan_no or str(self.pk)

class OnwardChallanItem(models.Model):
    challan     = models.ForeignKey(onwardchallan, on_delete=models.CASCADE, related_name='items')
    item_code   = models.CharField(max_length=100, default='DEFAULT_ITEM')
    type        = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    store       = models.CharField(max_length=100)
    stock  = models.CharField(max_length=100,blank=True,null=True)
    suppRefNo   = models.CharField(max_length=50)
    qtyNo       = models.DecimalField(max_digits=12, decimal_places=2)
    qtyKg       = models.DecimalField(max_digits=12, decimal_places=2)
    process     = models.CharField(max_length=100, blank=True)
    pkg         = models.CharField(max_length=50, blank=True)
    wRate       = models.DecimalField(max_digits=12, decimal_places=2)
    wValue      = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.challan} → {self.item_code}"
    



class Store(models.Model):
    name = models.CharField(max_length=100, unique=True)
    available_qty = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.name} ({self.available_qty})"



# class onwardchallan(models.Model):
#     challan_no = models.CharField(max_length=20, unique=True, blank=True,null=True)
#     item_code=models.CharField(max_length=100 , default='DEFAULT_ITEM')
#     challan_date=models.DateField()
#     challan_time=models.TimeField()
#     DC_no=models.CharField(max_length=50,blank=True)
#     Transport_name=models.CharField(max_length=100,blank=True)
#     vehical_no=models.CharField(max_length=20,blank=True)
#     Estimated_value=models.CharField(max_length=50,blank=True)
#     DC_date=models.DateField()
#     EWay_bill_no=models.CharField(max_length=50,blank=True)
#     eway_bill_date=models.DateField(null=True, blank=True)
#     REV_CHARGES_CHOICES = [
#         ('Y', 'Yes'),
#         ('N', 'No'),
#     ]
#     rev_charges = models.CharField(max_length=1,choices=REV_CHARGES_CHOICES,default='N')
#     rec_ch_amt=models.CharField(max_length=50,blank=True)
#     Eway_bill_Qty=models.CharField(max_length=50,blank=True,null=True)
#     remarks=models.CharField(max_length=100,blank=True,null=True)
#     plant=models.CharField(max_length=30,blank=True,default='')
#     series=models.CharField(max_length=30,blank=True)
#     vender=models.CharField(max_length=30,blank=True)

#     def __str__(self):
#         return f"{self.challan_no} - {self.vehical_no}"
#     def save(self, *args, **kwargs):
#         # Check if Transport_name exists in transportdetails
#         if not transportdetails.objects.filter(transport_name=self.Transport_name).exists():
#             # Create new transportdetails entry
#             last_serial = transportdetails.objects.aggregate(models.Max('serial_no'))['serial_no__max'] or 0
#             transportdetails.objects.create(
#                 serial_no=last_serial + 1,
#                 transport_name=self.Transport_name,
#                 EWAY_bill_no=self.EWay_bill_no
#             )
#         if not vehicaldetails.objects.filter(vehical_no=self.vehical_no).exists():
#             last_serial=vehicaldetails.objects.aggregate(models.Max('serial_no'))['serial_no__max'] or 0
#             vehicaldetails.objects.create(
#                 serial_no=last_serial+1,
#                 customer='',
#                 vehical_no=self.vehical_no,
#             )
#         super().save(*args, **kwargs)


class transportdetails(models.Model):
    serial_no = models.IntegerField(unique=True)
    transport_name=models.CharField(max_length=50)
    EWAY_bill_no=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.serial_no} - {self.transport_name}"
class vehicaldetails(models.Model):
    vehicle_no_validator = RegexValidator(
    regex=r'^[A-Z]{2}\s?[0-9]{1,2}\s?[A-Z]{1,3}\s?[0-9]{1,4}$',
    message='Enter a valid Indian vehicle number (e.g., MH12AB1234)')
    serial_no=models.IntegerField(unique=True)
    customer=models.CharField(max_length=50 , blank=True)
    vehical_no=models.CharField(max_length=50,validators=[vehicle_no_validator])
    def __str__(self):
        return f'{self.vehical_no}'




class Invoice(models.Model):
    invoice_no=models.CharField(max_length=100,blank=True,null=True)
    invoice_Date=models.DateField(blank=True,null=True)
    invoice_time=models.TimeField(blank=True,null=True)
    payment_Date=models.DateField(blank=True,null=True)
    note=models.TextField(blank=True,null=True)
    date_of_removal=models.DateField(blank=True,null=True)
    time=models.TimeField(blank=True,null=True)
    mode_of_trans=models.CharField(max_length=100,blank=True,null=True)
    freight=models.CharField(max_length=100,blank=True,null=True)
    vehical_no=models.CharField(max_length=50,blank=True,null=True)
    transporter=models.CharField(max_length=50,blank=True,null=True)
    bill_to=models.CharField(max_length=50,blank=True,null=True)
    ship_to=models.CharField(max_length=50,blank=True,null=True)
    addr_code=models.CharField(max_length=20,blank=True,null=True)
    l_r_gc_note=models.TextField(max_length=200,blank=True,null=True)
    place_of_supply=models.CharField(max_length=200,blank=True,null=True)
    Eway_bill_Date=models.DateField(blank=True,null=True)
    Eway_bill_no=models.CharField(max_length=50,blank=True,null=True)
    destenation_code=models.CharField(max_length=50,blank=True,null=True)
    note_remark=models.TextField(max_length=100,blank=True,null=True)
    # pdi_no=models.IntegerField(blank=True,null=True)
    # bank=models.CharField(max_length=50,blank=True,null=True)
    d_c_no=models.CharField(max_length=50,blank=True,null=True)
    d_c_Date=models.DateField(blank=True,null=True)
    delivery_terms=models.TextField(max_length=200,blank=True,null=True)


class InvoiceItemdetails(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    plant=models.CharField(max_length=100,blank=True,null=True)
    series=models.CharField(max_length=100,blank=True,null=True)
    invoice_type=models.CharField(max_length=100,blank=True,null=True)
    invoice_no=models.CharField(max_length=100,blank=True,null=True)
    customer=models.CharField(max_length=250,blank=True,null=True)
    po_no=models.CharField(max_length=250,blank=True,null=True)
    date=models.DateField(blank=True,null=True)
    stock=models.CharField(max_length=250,blank=True , null=True)
    description=models.CharField(max_length=250,blank=True,null=True)
    rate=models.CharField(max_length=250,blank=True,null=True)
    po_qty=models.CharField(max_length=250,blank=True,null=True)
    bal_qty=models.IntegerField(blank=True,null=True)
    inv_qty=models.IntegerField(blank=True,null=True)
    pkg_qty=models.IntegerField(blank=True,null=True)
    type_of_packing=models.CharField(max_length=250,blank=True,null=True)
    hsn_code=models.CharField(max_length=100,blank=True,null=True)


class GstdetailsInvoice(models.Model):
    invoice=models.ForeignKey(Invoice,related_name='GSTdetails', on_delete=models.CASCADE)
    base_value=models.IntegerField(max_length=10,blank=True,null=True)
    disc_amt=models.IntegerField(max_length=10,blank=True,null=True)
    rev_base_crg=models.IntegerField(max_length=10,blank=True,null=True)
    rev_charg_amt=models.IntegerField(max_length=10,blank=True,null=True)
    tcs=models.IntegerField(max_length=10,blank=True,null=True)
    assessble_value=models.IntegerField(max_length=10,blank=True,null=True)
    cgst=models.IntegerField(max_length=10,blank=True,null=True)
    sgst=models.IntegerField(max_length=10,blank=True,null=True)
    igst=models.IntegerField(max_length=10,blank=True,null=True)
    utgst=models.IntegerField(max_length=10,blank=True,null=True)
    pack_fwrd=models.IntegerField(max_length=10,blank=True,null=True)
    transport_crg=models.IntegerField(max_length=10,blank=True,null=True)
    freight_crg=models.IntegerField(max_length=10,blank=True,null=True)
    other_crg=models.IntegerField(max_length=10,blank=True,null=True)
    grand_total=models.IntegerField(max_length=50,blank=True,null=True)




from django.utils import timezone
class NewSalesOrder(models.Model):
    plant=models.CharField(max_length=100,blank=True,null=True)
    order_type=models.CharField(max_length=100,blank=True,null=True)
    customer=models.CharField(max_length=100,blank=True,null=True)
    cust_po=models.CharField(max_length=100,blank=True,null=True)
    cust_date=models.DateField(auto_created=True)
    pay_day=models.CharField(max_length=100,blank=True,null=True)
    pay_note=models.CharField(max_length=100,blank=True,null=True)
    valid_up=models.DateField(blank=True,null=True)
    file = models.ImageField(upload_to='newsales/', null=True,blank=True )
    # file=models.fiel(upload_to='newsales')
    so_date=models.DateField(auto_now_add=True)
    so_no=models.CharField(max_length=100,blank=True,null=True)
    po_rec_date=models.DateField(auto_now_add=True)
    incoterms=models.CharField(max_length=100,blank=True,null=True)
    ship_to=models.CharField(max_length=100,blank=True,null=True)
    ship_to_add_code= models.CharField(max_length=100,blank=True,null=True)
    ccn_no=models.CharField(max_length=100,blank=True,null=True)
    delivery_date=models.DateField(blank=True,null=True)
    buyer_name=models.CharField(max_length=100,blank=True,null=True)
    packing=models.CharField(max_length=100,blank=True,null=True)
    shift=models.CharField(max_length=100,blank=True,null=True)
    # shift=models.DateField(blank=True,null=True)
    plan_date=models.DateField(auto_now_add=True)
    l_c_no=models.CharField(max_length=100,blank=True,null=True)
    sales_person=models.CharField(max_length=100,blank=True,null=True)
    site_name=models.CharField(max_length=100,null=True ,blank=True)
    project_name=models.CharField(max_length=100, blank=True,null=True)
    terms= models.CharField(max_length=100,blank=True, null=True)


class NewSalesItemdetails(models.Model):
    newsaleoreder=models.ForeignKey(NewSalesOrder,on_delete=models.CASCADE,related_name='item')
    rev_no=models.CharField(max_length=100,blank=True,null=True)
    item_code=models.CharField(max_length=100,blank=True,null=True)
    line_no=models.CharField(max_length=100,blank=True,null=True)
    pr_no=models.CharField(max_length=100,blank=True,null=True)
    item_description=models.CharField(max_length=100,blank=True,null=True)
    rate=models.CharField(max_length=100,blank=True,null=True)
    desc=models.CharField(max_length=100,blank=True,null=True)
    qty=models.CharField(max_length=100,blank=True,null=True)
    uom=models.CharField(max_length=100,blank=True,null=True)
    rm_type=models.CharField(max_length=100,blank=True,null=True)
    item_wt=models.CharField(max_length=100,blank=True,null=True)
    pkg_trans=models.CharField(max_length=100,blank=True,null=True)
    plan_date=models.DateField(auto_now_add=True)
    due_date=models.DateField(blank=True,null=True)
    type=models.CharField(max_length=100,blank=True,null=True)
    item_category=models.CharField(max_length=100,blank=True,null=True)
    remark=models.CharField(max_length=250,blank=True,null=True)
    hsn_code=models.CharField(max_length=250,blank=True,null=True)
    assessable_value=models.DecimalField(max_digits=50,decimal_places=4,default=0)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    cgst = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    sgst = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    igst = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    utgst = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    gr_total = models.DecimalField(max_digits=50, decimal_places=2, default=0)



class DebitNote(models.Model):
    type =models.CharField(max_length=50,blank=True,null=True)
    notetype=models.CharField(max_length=100,blank=True,null=True)
    debit_note_no=models.CharField(max_length=100 ,blank=True,null=True)
    debit_note_date=models.DateField(blank= True,null= True)
    party_name=models.CharField(max_length=250,blank=True,null=True)
    mode_of_transport=models.CharField(max_length=100,blank=True,null=True)
    lr_gc_note_no=models.CharField(max_length=100,blank=True,null=True)
    eway_bill_no=models.CharField(max_length=100,blank=True,null=True)
    eway_bill_date=models.DateField(blank=True,null=True)
    vehical_no=models.CharField(max_length=100,blank=True,null=True)
    traspoter=models.CharField(max_length=100,blank=True,null=True)
    po_no=models.CharField(max_length=100,blank=True,null=True)
    po_date=models.DateField(blank=True,null=True)
    invoice_no=models.CharField(max_length=100,blank=True,null=True)
    invoice_date=models.DateField(blank=True,null=True)
    remark=models.CharField(max_length=250,blank=True,null=True)
    is_service_dn=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.debit_note_no

class DebitNoteIteam(models.Model):
    debit_note = models.ForeignKey(DebitNote,related_name="items",on_delete=models.CASCADE)
    grn_no=models.CharField(max_length=100,blank=True,null=True)
    grn_date=models.DateField(blank=True, null=True)
    item_code=models.CharField(max_length=100,blank=True,null=True)
    item_description=models.CharField(max_length=100,blank=True,null=True)
    hsn_code=models.CharField(max_length=100,blank=True,null=True)
    grn_qty=models.DecimalField(max_digits=12,decimal_places=4,blank=True,null=True)
    stock=models.DecimalField(max_digits=12,decimal_places=4,blank=True,null=True)
    remark=models.CharField(max_length=250,blank=True,null=True)
    reason=models.CharField(max_length=100,blank=True,null=True)
    quantity=models.CharField(max_length=100,blank=True,null=True)
    unit=models.CharField(max_length=100,blank=True,null=True)
    Rate=models.DecimalField(max_digits=12,decimal_places=4,blank=True,null=True)
    amount=models.DecimalField(max_digits=12,decimal_places=4,blank=True,null=True)
    transport_charges = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    cgst = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    sgst = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    igst = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    utgst = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    tcs = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    tds_on_basic = models.BooleanField(default=True)
    tds_on_grand_total = models.BooleanField(default=False)
    grand_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)





class Newgstsalesreturn(models.Model):
    plant = models.CharField(max_length=100, blank=True, null=True)
    gate_entry_no = models.CharField(max_length=50, blank=True, null=True)
    series = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    sales_return_no = models.CharField(max_length=100, blank=True, null=True)
    sales_return_date = models.DateField(blank=True, null=True)
    cust_name = models.CharField(max_length=100, blank=True, null=True)
    invoice_challan_no = models.CharField(max_length=100, blank=True, null=True)
    invoice_challan_date = models.DateField(blank=True, null=True)
    transport_name = models.CharField(max_length=100, blank=True, null=True)
    Lr_no = models.CharField(max_length=100, blank=True, null=True)
    vehical_no = models.CharField(max_length=20, blank=True, null=True)
    remark = models.CharField(max_length=250, blank=True, null=True)
    for_e_invoice = models.CharField(max_length=250, blank=True, null=True)
    is_service = models.BooleanField(default=True)


class NewgstsalesItemDetails(models.Model):
    new_gst_sales = models.ForeignKey(Newgstsalesreturn,related_name="items",on_delete=models.CASCADE )

    inv_no = models.CharField(max_length=100, blank=True, null=True)
    inv_date = models.DateField(blank=True, null=True)
    item_code = models.CharField(max_length=100, blank=True, null=True)
    hsn_code = models.CharField(max_length=100, blank=True, null=True)

    rate = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total_amt = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    inv_qty = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    return_qty = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)

    lot = models.CharField(max_length=100, blank=True, null=True)
    reason = models.CharField(max_length=100, blank=True, null=True)
    grir_no = models.CharField(max_length=100, blank=True, null=True)
    grir_date = models.DateField(blank=True, null=True)

    basic = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    disc = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    cgst = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    sgst = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    igst = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    utgst = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    toc = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tsc = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
