from django.db import models
from django.contrib.auth.models import User 

    
# New Purchase Order:- PO Info
class PoInfo(models.Model):
    PoNo = models.CharField(max_length=30)
    EnquiryNo = models.CharField(max_length=30)
    QuotNo = models.CharField(max_length=30)
    PaymentTerms = models.CharField(max_length=30)
    DeliveryDate = models.DateField()
    AMC_PO = models.CharField(max_length=30)
    ModeOfShipment = models.CharField(max_length=30)
    PreparedBy = models.CharField(max_length=30)
    PoNote = models.CharField(max_length=30)
    PoSpecification = models.CharField(max_length=30)
    PoDate = models.DateField()
    EnquiryDate = models.DateField()
    QuotDate = models.DateField()
    PaymentRemark = models.CharField(max_length=30)
    DeliveryType = models.CharField(max_length=30)
    DeliveryNote = models.CharField(max_length=30)
    IndentNo = models.CharField(max_length=30)
    ApprovedBy = models.CharField(max_length=30)
    InspectionTerms = models.CharField(max_length=30)
    PF_Charges = models.CharField(max_length=30)
    Time = models.TimeField()
    PoFor = models.CharField(max_length=30)
    Freight = models.CharField(max_length=30)
    PoRateType = models.CharField(max_length=30)
    ContactPerson = models.CharField(max_length=30)
    PoValidityDate = models.DateField()
    PoEffectiveDate = models.DateField()
    TransportName = models.CharField(max_length=30)
    PoValidity_WarrantyTerm = models.CharField(max_length=30)
    GstTaxes = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.PoNo} - {self.PoNo}"



# New JobWork Purchase Order:
class JwPoInfo(models.Model):
    PoNo = models.CharField(max_length=30)
    PaymentTerm = models.CharField(max_length=30)
    QuotNo = models.CharField(max_length=30)
    Delivery = models.DateField()
    PoValidityDate = models.DateField()
    PoNote = models.CharField(max_length=30)
    GST = models.CharField(max_length=30)
    PoDate = models.DateField()
    PaymentRemark = models.CharField(max_length=30)
    QuotationDate = models.DateField()
    freight = models.CharField(max_length=30)
    ContactPersion = models.CharField(max_length=30)
    PF_Charges = models.CharField(max_length=30)
    PoRateType = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.PoNo} - {self.PoNo}"
    
# New JobWork Purchase Order:- ItemDetail
class JwItemDetail(models.Model):
    SelectItem = models.CharField(max_length=30)
    ItemDescription = models.CharField(max_length=30)
    Out = models.CharField(max_length=30)
    In = models.CharField(max_length=30)
    Rate = models.CharField(max_length=30)
    RType = models.CharField(max_length=30)
    Disc = models.CharField(max_length=30)
    PoQty = models.CharField(max_length=30)
    Unit = models.CharField(max_length=30)
    Particular_Process = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.SelectItem} - {self.SelectItem}"
    
# New JobWork Purchase Order:- Ship To Add
class JwShipAdd(models.Model):
    ShiptoAdd = models.CharField(max_length=30)
    ContactDetail = models.CharField(max_length=30)
    ProjectName = models.CharField(max_length=30)
    CRName = models.CharField(max_length=30)
    SoNo = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.ShiptoAdd} - {self.ShiptoAdd}"
    

# Quote Comparison:- Quote Comparison Statement
class Quote_Comparison_Statement(models.Model):
    SelectRFQ = models.CharField(max_length=30)
    Item = models.CharField(max_length=30)
    Make = models.CharField(max_length=30)
    MinPurchQty = models.CharField(max_length=30)
    OtherCharges = models.CharField(max_length=30)
    PaymentTerms = models.CharField(max_length=30)
    Date = models.CharField(max_length=30)
    Supplier = models.CharField(max_length=30)
    UOM = models.CharField(max_length=30)
    TaxApplicable = models.CharField(max_length=30)
    RemarkDetails = models.CharField(max_length=30)
    SuppQuotNo = models.CharField(max_length=30)
    BasicRate = models.CharField(max_length=30)
    DeliveryMode = models.CharField(max_length=30)
    QuoteDate = models.CharField(max_length=30)
    Discount = models.CharField(max_length=30)
    DeliveryTime = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.SelectRFQ} - {self.SelectRFQ}"




########## po number
# models.py 
from django.db import models

class CodeGenerator(models.Model):
    FIELD_CHOICES = [
        ('RM', 'RM'),
        ('CONSUMABLE', 'CONSUMABLE'),
        ('SERVICE', 'SERVICE'),
        ('ASSET', 'ASSET'),
    ]

    field = models.CharField(max_length=20, choices=FIELD_CHOICES)
    year = models.IntegerField()
    last_code = models.IntegerField(default=0)  # Last generated code number
    PoNo = models.CharField(max_length=30, blank=True, null=True)
    EnquiryNo = models.CharField(max_length=30, blank=True, null=True)
    QuotNo = models.CharField(max_length=30, blank=True, null=True)
    PaymentTerms = models.CharField(max_length=30, blank=True, null=True)
    DeliveryDate = models.DateField(blank=True, null=True)
    AMC_PO = models.CharField(max_length=30, blank=True, null=True)
    ModeOfShipment = models.CharField(max_length=30, blank=True, null=True)
    PreparedBy = models.CharField(max_length=30, blank=True, null=True)
    PoNote = models.CharField(max_length=30, blank=True, null=True)
    PoSpecification = models.CharField(max_length=30, blank=True, null=True)
    PoDate = models.DateField(blank=True, null=True)
    EnquiryDate = models.DateField(blank=True, null=True)
    QuotDate = models.DateField(blank=True, null=True)
    PaymentRemark = models.CharField(max_length=30, blank=True, null=True)
    DeliveryType = models.CharField(max_length=30, blank=True, null=True)
    DeliveryNote = models.CharField(max_length=30, blank=True, null=True)
    IndentNo = models.CharField(max_length=30, blank=True, null=True)
    ApprovedBy = models.CharField(max_length=30, blank=True, null=True)
    InspectionTerms = models.CharField(max_length=30, blank=True, null=True)
    PF_Charges = models.CharField(max_length=30, blank=True, null=True)
    Time = models.TimeField(blank=True, null=True)
    PoFor = models.CharField(max_length=30, blank=True, null=True)
    Freight = models.CharField(max_length=30, blank=True, null=True)
    PoRateType = models.CharField(max_length=30, blank=True, null=True)
    ContactPerson = models.CharField(max_length=30, blank=True, null=True)
    PoValidityDate = models.DateField(blank=True, null=True)
    PoEffectiveDate = models.DateField(blank=True, null=True)
    TransportName = models.CharField(max_length=30, blank=True, null=True)
    PoValidity_WarrantyTerm = models.CharField(max_length=30, blank=True, null=True)
    GstTaxes = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f'{self.field} - {self.year} - {self.last_code}'
    
    def generate_new_code(self):
        self.last_code += 1
        new_code = f'{self.year}{self.last_code:05d}'
        return new_code
    

from django.db import models

class PurchaseOrder(models.Model):
    POType = models.CharField(max_length=30, blank=True, null=True)
    Plant = models.CharField(max_length=30, blank=True, null=True)
    Series = models.CharField(max_length=30, blank=True, null=True)
    Supplier = models.CharField(max_length=30, blank=True, null=True)
    PoNo = models.CharField(max_length=20, unique=True)
    PaymentTerm = models.CharField(max_length=30)
    QuotNo = models.CharField(max_length=30)
    Delivery = models.DateField()
    PoValidityDate = models.DateField()
    PoNote = models.CharField(max_length=30)
    GST = models.CharField(max_length=30)
    PoDate = models.DateField()
    PaymentRemark = models.CharField(max_length=30)
    QuotationDate = models.DateField()
    freight = models.CharField(max_length=30)
    ContactPersion = models.CharField(max_length=100)
    PF_Charges = models.CharField(max_length=30)
    PoRateType = models.CharField(max_length=30)

    def __str__(self):
        return self.PoNo
    


class PurchaseNewIndent(models.Model):
    PoNo = models.CharField(max_length=20, unique=True)
    PaymentTerm = models.CharField(max_length=30)
    QuotNo = models.CharField(max_length=30)
    Delivery = models.DateField()
    PoValidityDate = models.DateField()
    PoNote = models.CharField(max_length=30)
    GST = models.CharField(max_length=30)
    PoDate = models.DateField()
    PaymentRemark = models.CharField(max_length=30)
    QuotationDate = models.DateField()
    freight = models.CharField(max_length=30)
    ContactPersion = models.CharField(max_length=100)
    PF_Charges = models.CharField(max_length=30)
    PoRateType = models.CharField(max_length=30)

    def __str__(self):
        return self.PoNo

#############
# from django.db import models

# class PurchasePO(models.Model):
#     FIELD_CHOICES = [
#         ('RM', 'RM'),
#         ('CONSUMABLE', 'Consumable'),
#         ('SERVICE', 'Service'),
#         ('ASSET', 'Asset'),
#     ]
#     field = models.CharField(choices=FIELD_CHOICES, max_length=20)
#     PoNo = models.CharField(max_length=50)
#     EnquiryNo = models.CharField(max_length=50)

#     # Additional fields
#     QuotNo = models.CharField(max_length=30, blank=True, null=True)
#     PaymentTerms = models.CharField(max_length=30, blank=True, null=True)
#     DeliveryDate = models.DateField(blank=True, null=True)
#     AMC_PO = models.CharField(max_length=30, blank=True, null=True)
#     ModeOfShipment = models.CharField(max_length=30, blank=True, null=True)
#     PreparedBy = models.CharField(max_length=30, blank=True, null=True)
#     PoNote = models.CharField(max_length=30, blank=True, null=True)
#     PoSpecification = models.CharField(max_length=30, blank=True, null=True)
#     PoDate = models.DateField(blank=True, null=True)
#     EnquiryDate = models.DateField(blank=True, null=True)
#     QuotDate = models.DateField(blank=True, null=True)
#     PaymentRemark = models.CharField(max_length=30, blank=True, null=True)
#     DeliveryType = models.CharField(max_length=30, blank=True, null=True)
#     DeliveryNote = models.CharField(max_length=30, blank=True, null=True)
#     IndentNo = models.CharField(max_length=30, blank=True, null=True)
#     ApprovedBy = models.CharField(max_length=30, blank=True, null=True)
#     InspectionTerms = models.CharField(max_length=30, blank=True, null=True)
#     PF_Charges = models.CharField(max_length=30, blank=True, null=True)
#     Time = models.TimeField(blank=True, null=True)
#     PoFor = models.CharField(max_length=30, blank=True, null=True)
#     Freight = models.CharField(max_length=30, blank=True, null=True)
#     PoRateType = models.CharField(max_length=30, blank=True, null=True)
#     ContactPerson = models.CharField(max_length=30, blank=True, null=True)
#     PoValidityDate = models.DateField(blank=True, null=True)
#     PoEffectiveDate = models.DateField(blank=True, null=True)
#     TransportName = models.CharField(max_length=30, blank=True, null=True)
#     PoValidity_WarrantyTerm = models.CharField(max_length=30, blank=True, null=True)
#     GstTaxes = models.CharField(max_length=30, blank=True, null=True)

#     def __str__(self):
#         return f'{self.field} - {self.PoNo}'



# models.py
#############Purchase PO
# New Purchase Order:- Item Detail
class MYDetail(models.Model):
    Item = models.CharField(max_length=30)
    ItemDescription = models.CharField(max_length=30)
    ItemSize = models.CharField(max_length=30)
    Rate = models.CharField(max_length=30)
    Disc = models.CharField(max_length=30)
    Qty = models.CharField(max_length=30)
    Unit = models.CharField(max_length=30)
    Particular = models.CharField(max_length=30)
    Mill_Name = models.CharField(max_length=30)
    DeliveryDt = models.DateField()


    def __str__(self):
        return f"{self.Item} - {self.Item}"
    

class ItemDetail(models.Model):
    Item = models.CharField(max_length=30, blank=True, null=True)
    ItemDescription = models.CharField(max_length=30, blank=True, null=True)
    ItemSize = models.CharField(max_length=30, blank=True, null=True)
    Rate = models.CharField(max_length=30, blank=True, null=True)
    Disc = models.CharField(max_length=30, blank=True, null=True)
    Qty = models.CharField(max_length=30, blank=True, null=True)
    Unit = models.CharField(max_length=30, blank=True, null=True)
    Particular = models.CharField(max_length=30, blank=True, null=True)
    Mill_Name = models.CharField(max_length=30, blank=True, null=True)
    DeliveryDt = models.DateField(max_length=30, blank=True, null=True)


    def __str__(self):
        return f"{self.Item} - {self.Item}"


class GSTDetails(models.Model):
    ItemCode = models.CharField(max_length=30, blank=True, null=True)
    HSN = models.CharField(max_length=30, blank=True, null=True)
    Rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Qty = models.IntegerField(blank=True, null=True)
    SubTotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Packing = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Transport = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ToolAmort = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    AssValue = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    CGST = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    SGST = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    IGST = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Vat = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Cess = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    
    class Meta:
        db_table = 'gst_details'


class ItemDetailsOther(models.Model):
    ItemNo = models.CharField(max_length=30, blank=True, null=True)
    CPC_Code = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f'Item Detail {self.id}'
    


class ScheduleLine(models.Model):
    ItemCode = models.CharField(max_length=30, blank=True, null=True)
    Description = models.CharField(max_length=30, blank=True, null=True)
    TotalQty = models.CharField(max_length=30, blank=True, null=True)
    Date1 = models.CharField(max_length=30, blank=True, null=True)
    Qty1 = models.CharField(max_length=30, blank=True, null=True)
    Date2 = models.CharField(max_length=30, blank=True, null=True)
    Qty2 = models.CharField(max_length=30, blank=True, null=True)
    Date3 = models.CharField(max_length=30, blank=True, null=True)
    Qty3 = models.CharField(max_length=30, blank=True, null=True)
    Date4 = models.CharField(max_length=30, blank=True, null=True)
    Qty4 = models.CharField(max_length=30, blank=True, null=True)
    Date5 = models.CharField(max_length=30, blank=True, null=True)
    Qty5 = models.CharField(max_length=30, blank=True, null=True)
    Date6 = models.CharField(max_length=30, blank=True, null=True)
    Qty6 = models.CharField(max_length=30, blank=True, null=True)
    Date7 = models.CharField(max_length=30, blank=True, null=True)
    Qty7 = models.CharField(max_length=30, blank=True, null=True)
    Date8 = models.CharField(max_length=30, blank=True, null=True)
    Qty8 = models.CharField(max_length=30, blank=True, null=True)
    Date9 = models.CharField(max_length=30, blank=True, null=True)
    Qty9 = models.CharField(max_length=30, blank=True, null=True)
    Date10 = models.CharField(max_length=30, blank=True, null=True)
    Qty10 = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.ItemCode  # Or another field that you'd like to represent as a string


class ShipToAdd(models.Model):
    Ship_To_Add = models.CharField(max_length=30, blank=True, null=True)
    ShipToContactDetails = models.CharField(max_length=30, blank=True, null=True)
    Reference = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f'ShipToAdd {self.id}'

from django.contrib.auth.models import User 

class PurchasePO(models.Model):
    FIELD_CHOICES = [
        ('RM', 'RM'),
        ('CONSUMABLE', 'Consumable'),
        ('SERVICE', 'Service'),
        ('ASSET', 'Asset'),
    ]
    field = models.CharField(choices=FIELD_CHOICES, max_length=20)
    PoNo = models.CharField(max_length=50)
    EnquiryNo = models.CharField(max_length=50)

    # ForeignKey to link multiple PurchasePODetails
    Item_Detail_Enter = models.ManyToManyField(ItemDetail, related_name='ItemDetail_orders', blank=True)
    Gst_Details = models.ManyToManyField(GSTDetails, related_name='Gst_orders', blank=True)
    Item_Details_Other = models.ManyToManyField(ItemDetailsOther, related_name='ItemDetails_orders', blank=True)
    Schedule_Line = models.ManyToManyField(ScheduleLine, related_name='Schedule_Line_orders', blank=True)
    Ship_To_Add = models.ManyToManyField(ShipToAdd, related_name='ShipToAdd_orders', blank=True)
    Type = models.CharField(max_length=30, blank=True, null=True)
    Plant = models.CharField(max_length=30, blank=True, null=True)
    Series = models.CharField(max_length=30, blank=True, null=True)
    Supplier = models.CharField(max_length=30, blank=True, null=True)
    CodeNo = models.CharField(max_length=30, blank=True, null=True)
    QuotNo = models.CharField(max_length=30, blank=True, null=True)
    PaymentTerms = models.CharField(max_length=30, blank=True, null=True)
    DeliveryDate = models.DateField(blank=True, null=True)
    AMC_PO = models.CharField(max_length=30, blank=True, null=True)
    ModeOfShipment = models.CharField(max_length=30, blank=True, null=True)
    PreparedBy = models.CharField(max_length=30, blank=True, null=True)
    PoNote = models.CharField(max_length=30, blank=True, null=True)
    PoSpecification = models.CharField(max_length=30, blank=True, null=True)
    PoDate = models.DateField(blank=True, null=True)
    EnquiryDate = models.DateField(blank=True, null=True)
    QuotDate = models.DateField(blank=True, null=True)
    PaymentRemark = models.CharField(max_length=30, blank=True, null=True)
    DeliveryType = models.CharField(max_length=30, blank=True, null=True)
    DeliveryNote = models.CharField(max_length=30, blank=True, null=True)
    IndentNo = models.CharField(max_length=30, blank=True, null=True)
    ApprovedBy = models.CharField(max_length=30, blank=True, null=True)
    InspectionTerms = models.CharField(max_length=30, blank=True, null=True)
    PF_Charges = models.CharField(max_length=30, blank=True, null=True)
    Time = models.CharField(max_length=30, blank=True, null=True)
    PoFor = models.CharField(max_length=30, blank=True, null=True)
    Freight = models.CharField(max_length=30, blank=True, null=True)
    PoRateType = models.CharField(max_length=30, blank=True, null=True)
    ContactPerson = models.CharField(max_length=30, blank=True, null=True)
    PoValidityDate = models.DateField(blank=True, null=True)
    PoEffectiveDate = models.DateField(blank=True, null=True)
    TransportName = models.CharField(max_length=30, blank=True, null=True)
    PoValidity_WarrantyTerm = models.CharField(max_length=30, blank=True, null=True)
    GstTaxes = models.CharField(max_length=30, blank=True, null=True)

    TOC_AssableValue = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    TOC_PackCharges = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    TOC_TransportCost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    TOC_Insurance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    TOC_InstallationCharges = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    TOC_CGST = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    TOC_SGST = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    TOC_IGST = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    TOC_VAT = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    TOC_CESS = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    TOC_TDS = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    GR_Total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    AprrovedStatusChoices = [
        ('Approved', 'approved'),
        ('Pending', 'pending'),
        ('Rejected', 'reject')
    ]
    Approved_Status = models.CharField(choices=AprrovedStatusChoices, max_length=10, default='pending')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    

    def __str__(self):
        return f'{self.field} - {self.PoNo}'



class Item(models.Model):
    # purchase_order = models.ForeignKey(PurchasePO, related_name='items', on_delete=models.CASCADE)
    item_code = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):
        # Calculate the total price based on quantity and unit price
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.item_code} - {self.description}'


# New Indent

class Indent(models.Model):
    AUTH_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    Plant = models.CharField(max_length=255, blank=True, null=True)
    Series = models.CharField(max_length=255, blank=True, null=True)
    IndentNo = models.CharField(max_length=255, blank=True, null=True)
    Date = models.CharField(max_length=255, blank=True, null=True)
    Time = models.CharField(max_length=255, blank=True, null=True)
    Category = models.CharField(max_length=255, blank=True, null=True)
    CPCCode = models.CharField(max_length=255, blank=True, null=True)
    WorkOrder = models.CharField(max_length=255, blank=True, null=True)
    Remark = models.CharField(max_length=255, blank=True, null=True)
    Auth = models.CharField(max_length=10, choices=AUTH_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.Plant} - {self.IndentNo}"


class New_Indent(models.Model):
    New_Indent_Detail = models.ForeignKey(Indent, related_name="New_Indent", on_delete=models.CASCADE) 
    ItemNoCpcCode = models.CharField(max_length=255, blank=True, null=True)
    Description = models.CharField(max_length=255, blank=True, null=True)
    Unit = models.CharField(max_length=255, blank=True, null=True)
    MachineAndDepartment = models.CharField(max_length=255, blank=True, null=True)
    Qty = models.CharField(max_length=255, blank=True, null=True)
    Type = models.CharField(max_length=255, blank=True, null=True)
    Remark = models.CharField(max_length=255, blank=True, null=True)
    UseFor =  models.CharField(max_length=255, blank=True, null=True)
    MoRef = models.CharField(max_length=255, blank=True, null=True)
    SchDate = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.ItemNoCpcCode} - {self.ItemNoCpcCode}"


# PO GST CALUCLAT
class ItemTransaction2(models.Model):
    supplier = models.ForeignKey(Item, on_delete=models.CASCADE)
    part_no = models.CharField(max_length=100)
    ItemDescription = models.CharField(max_length=255)
    PartCode = models.CharField(max_length=100)
    Out = models.DecimalField(max_digits=10, decimal_places=2)
    Inn = models.DecimalField(max_digits=10, decimal_places=2)    
    Rate = models.DecimalField(max_digits=10, decimal_places=2)
    RType = models.CharField(max_length=50)
    Disc = models.DecimalField(max_digits=5, decimal_places=2)
    PoQty = models.DecimalField(max_digits=10, decimal_places=2)
    Unit = models.CharField(max_length=50)
    ParticularProcess = models.CharField(max_length=255)


# New JobWork Purchase Order

class NewJobWorkItemDetails(models.Model):
    purchase_order = models.ForeignKey(PurchasePO, related_name='items', on_delete=models.CASCADE, null=True)
    ItemName = models.CharField(max_length=100, blank=True, null=True)
    ItemDescription = models.CharField(max_length=100, blank=True, null=True)
    OutAndInPart = models.CharField(max_length=100, blank=True, null=True)
    Rate = models.CharField(max_length=100, blank=True, null=True)
    Disc = models.CharField(max_length=100, blank=True, null=True)
    Qty = models.CharField(max_length=100, blank=True, null=True)
    Unit = models.CharField(max_length=100, blank=True, null=True)
    Particular = models.CharField(max_length=100, blank=True, null=True)
    Version = models.CharField(max_length=100, blank=True, null=True)
    ItemStatus = models.CharField(max_length=100, blank=True, null=True)
    CSCode = models.CharField(max_length=100, blank=True, null=True)
    Note = models.CharField(max_length=100, blank=True, null=True)    

class NewJobWorkGstDetails(models.Model):
    ItemCode = models.CharField(max_length=100, blank=True, null=True)    
    SacCode = models.CharField(max_length=100, blank=True, null=True)    
    Rate = models.CharField(max_length=100, blank=True, null=True)    
    Qty = models.CharField(max_length=100, blank=True, null=True)    
    SubTotal = models.CharField(max_length=100, blank=True, null=True)    
    Discount = models.CharField(max_length=100, blank=True, null=True)    
    Packing = models.CharField(max_length=100, blank=True, null=True)    
    Transport = models.CharField(max_length=100, blank=True, null=True)    
    AssValue = models.CharField(max_length=100, blank=True, null=True)    
    CGST = models.CharField(max_length=100, blank=True, null=True)    
    SGST = models.CharField(max_length=100, blank=True, null=True)    
    IGST = models.CharField(max_length=100, blank=True, null=True)    
    Total = models.CharField(max_length=100, blank=True, null=True)    

class NewJobWorkScheduleLine(models.Model):
    ItemCode = models.CharField(max_length=100, blank=True, null=True)    
    Description = models.CharField(max_length=100, blank=True, null=True)    
    TotalQty = models.CharField(max_length=100, blank=True, null=True)    
    Date1 = models.CharField(max_length=100, blank=True, null=True)    
    Qty1 = models.CharField(max_length=100, blank=True, null=True)    
    Date2 = models.CharField(max_length=100, blank=True, null=True)    
    Qty2 = models.CharField(max_length=100, blank=True, null=True)    
    Date3 = models.CharField(max_length=100, blank=True, null=True)    
    Qty3 = models.CharField(max_length=100, blank=True, null=True)    
    Date4 = models.CharField(max_length=100, blank=True, null=True)    
    Qty4 = models.CharField(max_length=100, blank=True, null=True)    
   
class NewJobWorkShipToAdd(models.Model):
    ShipToAdd = models.CharField(max_length=30, blank=True, null=True)
    ShipToContactDetails = models.CharField(max_length=30, blank=True, null=True)
    ProjectName = models.CharField(max_length=100, blank=True, null=True)
    CRName = models.CharField(max_length=100, blank=True, null=True)

class NewJobWorkPoInfo(models.Model):
    PoType = models.CharField(max_length=100, blank=True, null=True)
    Plant = models.CharField(max_length=100, blank=True, null=True)
    Series = models.CharField(max_length=100, blank=True, null=True)
    Supplier = models.CharField(max_length=100, blank=True, null=True)
    PoNo = models.CharField(max_length=100, blank=True, null=True)
    PaymentTerm = models.CharField(max_length=100, blank=True, null=True)
    QuotNo = models.CharField(max_length=100, blank=True, null=True)
    Delivery = models.CharField(max_length=100, blank=True, null=True)
    PoValidityDate = models.CharField(max_length=100, blank=True, null=True)
    PoNote = models.CharField(max_length=100, blank=True, null=True)
    GST = models.CharField(max_length=100, blank=True, null=True)
    PoDate = models.CharField(max_length=100, blank=True, null=True)
    PaymentRemark = models.CharField(max_length=100, blank=True, null=True)
    QuotationDate = models.CharField(max_length=100, blank=True, null=True)
    freight = models.CharField(max_length=100, blank=True, null=True)
    ContactPersion = models.CharField(max_length=100, blank=True, null=True)
    PF_Charges = models.CharField(max_length=100, blank=True, null=True)
    PoRateType = models.CharField(max_length=100, blank=True, null=True)

    TOC_AssableValue = models.CharField(max_length=100, blank=True, null=True)
    PackCharges = models.CharField(max_length=100, blank=True, null=True)
    TransportCharges = models.CharField(max_length=100, blank=True, null=True)
    Insurance = models.CharField(max_length=100, blank=True, null=True)
    InstallationCharges = models.CharField(max_length=100, blank=True, null=True)
    OtherCharges = models.CharField(max_length=100, blank=True, null=True)
    CGST = models.CharField(max_length=100, blank=True, null=True)
    SGST = models.CharField(max_length=100, blank=True, null=True)
    IGST = models.CharField(max_length=100, blank=True, null=True)
    TCS = models.CharField(max_length=100, blank=True, null=True)
    GR_Total = models.CharField(max_length=100, blank=True, null=True)

    Item_Detail_Enter = models.ManyToManyField(NewJobWorkItemDetails, related_name='ItemDetail_orders', blank=True)
    Gst_Details = models.ManyToManyField(NewJobWorkGstDetails, related_name='Gst_orders', blank=True)
    Schedule_Line = models.ManyToManyField(NewJobWorkScheduleLine, related_name='Schedule_Line_orders', blank=True)
    Ship_To_Add = models.ManyToManyField(NewJobWorkShipToAdd, related_name='ShipToAdd_orders', blank=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
     
    def __str__(self):
        return self.PoNo or "Unnamed PO"
    
class QuotationComparison(models.Model):
    select_RFQ = models.CharField(max_length=50, blank=True, null=True)
    item = models.CharField(max_length=20, blank=True, null=True)
    make = models.CharField(max_length=50, blank=True, null=True)
    minimum_purchase_quantity = models.IntegerField(blank=True, null=True)
    other_charges = models.IntegerField(blank=True, null=True)
    payment_terms = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    supplier = models.CharField(max_length=50, blank=True, null=True)
    uom = models.CharField(max_length=20, blank=True, null=True)
    tax_applicable = models.CharField(max_length=50, blank=True, null=True)
    remark_details = models.CharField(max_length=100, blank=True, null=True)
    supplier_quote_no = models.CharField(max_length=20, blank=True, null=True)
    basic_rate = models.IntegerField(blank=True, null=True)
    delivery_mode = models.CharField(max_length=20, blank=True, null=True)
    quote_date = models.DateField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    delivery_time = models.TimeField(blank=True, null=True)

    def _str_(self):
        return self.supplier 

    


class RFQ(models.Model):
    RFQ_TYPE_CHOICES = [
        ('single', 'For Single'),
        ('enquiry', 'Against Enquiry'),
    ]
    UNIT_CHOICES = [
    ('PCS', 'PCS'),
    ('KGS', 'KGS'),
    ('Box', 'Box'),
    ('LTR', 'LTR'),
    ('NOS', 'NOS'),
    ('SQFT', 'SQFT'),
    ('MTR', 'MTR'),
    ('FOOT', 'FOOT'),
    ('SQMTR', 'SQMTR'),
    ('PAIR', 'PAIR'),
    ('BAG', 'BAG'),
    ('PACKET', 'PACKET'),
    ('RIM', 'RIM'),
    ('SET', 'SET'),
    ('MT', 'MT'),
    ('PER DAY', 'PER DAY'),
    ('DOZEN', 'DOZEN'),
    ('JOB', 'JOB'),
    ('SQUINCH', 'SQUINCH'),]

    rfq_type = models.CharField(max_length=10,choices=RFQ_TYPE_CHOICES )
    rfq_no = models.CharField(max_length=50, unique=True,blank=True,null=True)
    ITEM_TYPE_CHOICES = [
        ('new', 'New'),
        ('existing', 'Existing'),
    ]
    item = models.CharField(max_length=10,choices=ITEM_TYPE_CHOICES)
    item_no = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_location = models.TextField()
    payment_term = models.TextField()
    delivery_schedule = models.TextField()
    to_date = models.DateField()
    indent_no = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=50,choices=UNIT_CHOICES)
    quality_terms = models.TextField()
    remark_details = models.TextField(blank=True, null=True)
    expected_date = models.DateField(blank=True, null=True)
    project_name=models.CharField(max_length=50,blank=True) 

    def _str_(self):
        return f"RFQ {self.rfq_no}"