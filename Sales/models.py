from django.db import models
from django.core.validators import RegexValidator
from All_Masters.models import Item as Item2


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
    suppRefNo   = models.CharField(max_length=50)
    qtyNo       = models.DecimalField(max_digits=12, decimal_places=2)
    qtyKg       = models.DecimalField(max_digits=12, decimal_places=2)
    process     = models.CharField(max_length=100, blank=True)
    pkg         = models.CharField(max_length=50, blank=True)
    wRate       = models.DecimalField(max_digits=12, decimal_places=2)
    wValue      = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.challan} → {self.item_code}"


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
