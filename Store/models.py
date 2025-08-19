from django.db import models
from django.contrib.auth.models import User 
from Sales.models import OnwardChallanItem

# Store Module:- Gate Inward Entry:- General Details
class GeneralDetails(models.Model):
    Plant = models.CharField(max_length=255, blank=True, null=True)
    Series = models.CharField(max_length=255, blank=True, null=True)
    Type = models.CharField(max_length=255, blank=True, null=True)
    Supp_Cust = models.CharField(max_length=255, blank=True, null=True)
    GE_No = models.CharField(max_length=255, blank=True, null=True)
    GE_Date = models.CharField(max_length=255, blank=True, null=True)
    GE_Time = models.CharField(max_length=255, blank=True, null=True)
    ChallanNo = models.CharField(max_length=255, blank=True, null=True)
    ChallanDate = models.DateField()
    Select = models.CharField(max_length=255, blank=True, null=True)
    InVoiceNo = models.CharField(max_length=255, blank=True, null=True)
    Invoicedate = models.DateField()
    EWayBillNo = models.CharField(max_length=255, blank=True, null=True)
    EWayBillDate = models.DateField()
    ContactPerson = models.CharField(max_length=255, blank=True, null=True)
    VehicleNo = models.CharField(max_length=255, blank=True, null=True)
    LrNo = models.CharField(max_length=255, blank=True, null=True)
    Transporter = models.CharField(max_length=255, blank=True, null=True)
    Remark = models.CharField(max_length=255, blank=True, null=True)
    po_reference = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.Plant} - {self.Plant}"
    
# Store Module:- Gate Inward Entry:- Item Details
class ItemDetails(models.Model):
    Work_Order_detail = models.ForeignKey(GeneralDetails, related_name='ItemDetails', on_delete=models.CASCADE)
    ItemNo = models.CharField(max_length=255, blank=True, null=True)
    Description = models.CharField(max_length=255, blank=True, null=True)
    Qty_NOS = models.CharField(max_length=255, blank=True, null=True)
    QTY_KG = models.CharField(max_length=255, blank=True, null=True)
    Unit_Code = models.CharField(max_length=255, blank=True, null=True)
    Remark = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return f"{self.ItemNo} - {self.Description}"

# Store Module:- NEW MRN
class NewMrn(models.Model):
    Plant = models.CharField(max_length=255, blank=True, null=True)
    Series = models.CharField(max_length=255, blank=True, null=True)
    MRN_no = models.CharField(max_length=255, blank=True, null=True)
    General = models.BooleanField(default=False)
    Work_order = models.BooleanField(default=False)
    ItemCode = models.CharField(max_length=255, blank=True, null=True)
    Description = models.CharField(max_length=255, blank=True, null=True)
    Qty_1 = models.CharField(max_length=255, blank=True, null=True)
    QtyUnit = models.CharField(max_length=255, blank=True, null=True)
    Unit = models.CharField(max_length=255, blank=True, null=True)
    Type = models.CharField(max_length=255, blank=True, null=True)
    Machine = models.CharField(max_length=255, blank=True, null=True)
    Employee = models.CharField(max_length=255, blank=True, null=True)  
    Dept = models.CharField(max_length=255, blank=True, null=True)
    Remark_1 = models.CharField(max_length=255, blank=True, null=True)
    MRN_date = models.CharField(max_length=255, blank=True, null=True)
    MRN_time = models.CharField(max_length=255, blank=True, null=True)
    Remark_2 = models.CharField(max_length=255, blank=True, null=True)
    Approve_choices =[
        ('Approved', 'approved'),
        ('Pending', 'pending'),
        ('Rejected', 'rejected')
    ]
    Approve_status = models.CharField(choices=Approve_choices, default='pending',max_length=255)

    def __str__(self):
        return f"{self.ItemCode} - {self.ItemCode}"
    
class NewMRNTable(models.Model):
    New_MRN_Detail = models.ForeignKey(NewMrn, related_name="NewMRNTable", on_delete=models.CASCADE)
    ItemCode = models.CharField(max_length=255, blank=True, null=True)
    Description = models.CharField(max_length=255, blank=True, null=True)
    QtyUnit = models.CharField(max_length=255, blank=True, null=True)
    Qty_1 = models.CharField(max_length=255, blank=True, null=True)
    Type = models.CharField(max_length=255, blank=True, null=True)
    Machine = models.CharField(max_length=255, blank=True, null=True)
    Employee = models.CharField(max_length=255, blank=True, null=True)
    Dept = models.CharField(max_length=255, blank=True, null=True)
    Remark_1 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.ItemCode - self.Description

# Store Module:- Purchase GRN: General Details
class GrnGenralDetail(models.Model):
    item = models.ForeignKey(OnwardChallanItem, on_delete=models.CASCADE, related_name='grndetails',null=True,)
    Plant = models.CharField(max_length=255, blank=True, null=True)
    Series = models.CharField(max_length=255, blank=True, null=True)
    GateEntryNo = models.CharField(max_length=255, blank=True, null=True)
    SelectSupplier = models.CharField(max_length=255, blank=True, null=True)
    SelectPO = models.CharField(max_length=255, blank=True, null=True)
    AddChallanGrnQty = models.BooleanField(default=False)
    SelectItem = models.CharField(max_length=255, blank=True, null=True)
    ItemDropdown = models.CharField(max_length=255, blank=True, null=True)
    HeatNo = models.CharField(max_length=255, blank=True, null=True)
        
    GrnNo = models.CharField(max_length=255, blank=True, null=True)
    GrnDate = models.CharField(max_length=255, blank=True, null=True)
    GrnTime = models.CharField(max_length=255, blank=True, null=True)
    ChallanNo = models.CharField(max_length=255, blank=True, null=True)
    ChallanDate = models.CharField(max_length=255, blank=True, null=True)
    InvoiceNo = models.CharField(max_length=255, blank=True, null=True)
    InvoiceDate = models.CharField(max_length=255, blank=True, null=True)
    EWayBillNo = models.CharField(max_length=255, blank=True, null=True)
    EWayBillDate = models.CharField(max_length=255, blank=True, null=True)
    VehicleNo = models.CharField(max_length=255, blank=True, null=True)
    LrNo = models.CharField(max_length=255, blank=True, null=True)
    Transporter = models.CharField(max_length=255, blank=True, null=True)
    PreparedBy = models.CharField(max_length=255, blank=True, null=True)
    CheckedBy = models.CharField(max_length=255, blank=True, null=True)
    TcNo = models.CharField(max_length=255, blank=True, null=True)
    TcDate = models.CharField(max_length=255, blank=True, null=True)
    QcCheck = models.BooleanField(default=False)
    Delivery = models.BooleanField(default=False)
    Remark = models.CharField(max_length=255, blank=True, null=True)
    PaymentTermDay = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return f"{self.Plant} - {self.Plant}"

class NewGrnList(models.Model):
    New_MRN_Detail = models.ForeignKey(GrnGenralDetail, related_name="NewGrnList", on_delete=models.CASCADE)
    PoNo = models.CharField(max_length=255, blank=True, null=True)
    Date = models.CharField(max_length=255, blank=True, null=True)
    ItemNoCode = models.CharField(max_length=255, blank=True, null=True)
    Description = models.CharField(max_length=255, blank=True, null=True)
    Rate = models.CharField(max_length=255, blank=True, null=True)
    PoQty = models.CharField(max_length=255, blank=True, null=True)
    BalQty = models.CharField(max_length=255, blank=True, null=True)
    ChalQty = models.CharField(max_length=255, blank=True, null=True)
    GrnQty = models.CharField(max_length=255, blank=True, null=True)
    ShortExcessQty = models.CharField(max_length=255, blank=True, null=True)
    UnitCode = models.CharField(max_length=255, blank=True, null=True)
    Total = models.CharField(max_length=255, blank=True, null=True)
    HeatNo = models.CharField(max_length=255, blank=True, null=True)
    MfgDate = models.CharField(max_length=255, blank=True, null=True)

class GrnGst(models.Model):
    New_MRN_Detail = models.ForeignKey(GrnGenralDetail, related_name="GrnGst", on_delete=models.CASCADE)
    ItemCode = models.CharField(max_length=255, blank=True, null=True)
    HSN = models.CharField(max_length=255, blank=True, null=True)
    PoRate = models.CharField(max_length=255, blank=True, null=True)
    DiscRate = models.CharField(max_length=255, blank=True, null=True)
    Qty = models.CharField(max_length=255, blank=True, null=True)
    Discount = models.CharField(max_length=255, blank=True, null=True)
    PackAmt = models.CharField(max_length=255, blank=True, null=True)
    TransAmt = models.CharField(max_length=255, blank=True, null=True)
    AssValue = models.CharField(max_length=255, blank=True, null=True)
    CGST = models.CharField(max_length=255, blank=True, null=True)
    SGST = models.CharField(max_length=255, blank=True, null=True)
    IGST = models.CharField(max_length=255, blank=True, null=True)
    VAT = models.CharField(max_length=255, blank=True, null=True)
    CESS = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.ItemCode - self.Description

class GrnGstTDC(models.Model):
    New_MRN_Detail = models.ForeignKey(GrnGenralDetail, related_name="GrnGstTDC", on_delete=models.CASCADE)
    assessable_value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    packing_forwarding_charges = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    transport_charges = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    insurance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    installation_charges = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    other_charges = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Tds = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cgst = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    sgst = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    igst = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    vat = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cess_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tcs_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Tax Details {self.id} - Grand Total: {self.grand_total}"

class RefTC(models.Model):
    New_MRN_Detail = models.ForeignKey(GrnGenralDetail, related_name="RefTC", on_delete=models.CASCADE)
    ItemCode = models.CharField(max_length=255, blank=True, null=True)
    ItemDesc = models.CharField(max_length=255, blank=True, null=True)
    MillTcName = models.CharField(max_length=255, blank=True, null=True)
    MillTcNo = models.CharField(max_length=255, blank=True, null=True)
    MillTcDate = models.CharField(max_length=255, blank=True, null=True)
    Location = models.CharField(max_length=255, blank=True, null=True)





# Store Module:- SubCon GRN: 57F4 Inward Challan
class InwardChallan(models.Model):
    InwardF4No = models.CharField(max_length=255, blank=True, null=True)
    InwardDate = models.CharField(max_length=255, blank=True, null=True)
    InwardTime = models.CharField(max_length=255, blank=True, null=True)
    ChallanNo = models.CharField(max_length=255, blank=True, null=True)
    ChallanDate = models.DateField()
    GateEnrtyNo = models.CharField(max_length=255, blank=True, null=True)
    InvoiceNo = models.CharField(max_length=255, blank=True, null=True)
    InvoiceDate = models.DateField()
    EWayBillQty = models.CharField(max_length=255, blank=True, null=True)
    EWayBillNo = models.CharField(max_length=255, blank=True, null=True)
    VehicleNo = models.CharField(max_length=255, blank=True, null=True)
    LrNo = models.CharField(max_length=255, blank=True, null=True)
    Transporter = models.CharField(max_length=255, blank=True, null=True)
    PreparedBy = models.CharField(max_length=255, blank=True, null=True)
    CheckedBy = models.CharField(max_length=255, blank=True, null=True)
    TcNo = models.CharField(max_length=255, blank=True, null=True)
    TcDate = models.DateField()
    Remark = models.CharField(max_length=255, blank=True, null=True)
    DeliveryInTime = models.BooleanField(default=True)
    TotalItem = models.CharField(max_length=255, blank=True, null=True)
    TotalQtyNo = models.CharField(max_length=255, blank=True, null=True)
    TotalQtyKg = models.CharField(max_length=255, blank=True, null=True)
    Store = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.InwardF4No} - {self.InwardF4No}"

# Store Module:- SubCon GRN: Job Work Inward Challan
class Job_Work(models.Model):
    InwardF4No = models.CharField(max_length=255, blank=True, null=True)
    InwardDate = models.CharField(max_length=255, blank=True, null=True)
    InwardTime = models.CharField(max_length=255, blank=True, null=True)
    ChallanNo = models.CharField(max_length=255, blank=True, null=True)
    ChallanDate = models.DateField()
    SubVendor = models.CharField(max_length=255, blank=True, null=True)
    DcNo = models.CharField(max_length=255, blank=True, null=True)
    DcDate = models.CharField(max_length=255, blank=True, null=True)
    EWayBillQty = models.CharField(max_length=255, blank=True, null=True)
    EWayBillNo = models.CharField(max_length=255, blank=True, null=True)
    VehicleNo = models.CharField(max_length=255, blank=True, null=True)
    LrNo = models.CharField(max_length=255, blank=True, null=True)
    Transporter = models.CharField(max_length=255, blank=True, null=True)
    PreparedBy = models.CharField(max_length=255, blank=True, null=True)
    CheckedBy = models.CharField(max_length=255, blank=True, null=True)
    VehicleTime = models.CharField(max_length=255, blank=True, null=True)
    TcNo = models.CharField(max_length=255, blank=True, null=True)
    TcDate = models.DateField()
    Remark = models.CharField(max_length=255, blank=True, null=True)
    DeliveryInTime = models.BooleanField(default=True)
    ClearingStatus = models.CharField(max_length=255, blank=True, null=True) 
    VehicleOutTime = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.InwardF4No} - {self.InwardF4No}"
    
# Store Module:- SubCon GRN: Vendor Scrap Inward
class VendorScrap(models.Model):
    InWardNo = models.CharField(max_length=255, blank=True, null=True)
    InWardDate = models.DateField()
    InWardTime = models.CharField(max_length=255, blank=True, null=True)
    ChallanNo = models.CharField(max_length=255, blank=True, null=True)
    ChallonDate = models.DateField()
    GIN_No = models.CharField(max_length=255, blank=True, null=True)
    InvoiceNo = models.CharField(max_length=255, blank=True, null=True)
    InvoiceDate = models.DateField()
    PreparedBy = models.CharField(max_length=255, blank=True, null=True)
    CheckedBy = models.CharField(max_length=255, blank=True, null=True)
    VehicleNo = models.CharField(max_length=255, blank=True, null=True)
    LrNo = models.CharField(max_length=255, blank=True, null=True)
    Transporter = models.CharField(max_length=255, blank=True, null=True)
    Remark = models.CharField(max_length=255, blank=True, null=True)
    DeliveryInTime = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.InWardNo} - {self.InWardNo}"

# Store Module:- Material Issue Challan
class MaterialIssue(models.Model):
    Item = models.CharField(max_length=255, blank=True, null=True)
    ItemDescription = models.CharField(max_length=255, blank=True, null=True)
    AvailableStock = models.CharField(max_length=255, blank=True, null=True)
    Machine = models.CharField(max_length=255, blank=True, null=True)
    StoreName = models.CharField(max_length=255, blank=True, null=True)
    Qty = models.CharField(max_length=255, blank=True, null=True)
    Unit = models.CharField(max_length=255, blank=True, null=True)
    Remark = models.CharField(max_length=255, blank=True, null=True)
    MrnNo = models.CharField(max_length=255, blank=True, null=True)
    Employee = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.ItemCode} - {self.ItemCode}"

# Store Module:- Material Issue General
class Material_Issue_General(models.Model):
    Item = models.CharField(max_length=255, blank=True, null=True)
    ItemDescription = models.CharField(max_length=255, blank=True, null=True)
    AvailableStock = models.CharField(max_length=255, blank=True, null=True)
    StockStatus = models.CharField(max_length=255, blank=True, null=True)
    Machine = models.CharField(max_length=255, blank=True, null=True)
    StoreName = models.CharField(max_length=255, blank=True, null=True)
    Qty = models.CharField(max_length=255, blank=True, null=True)
    Unit = models.CharField(max_length=255, blank=True, null=True)
    Remark = models.CharField(max_length=255, blank=True, null=True)
    MrnNo = models.CharField(max_length=255, blank=True, null=True)
    Employee = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.ItemCode} - {self.ItemCode}"

# Store Module:- DeliveryChallan
class DeliveryChallan(models.Model):
    SelectItem = models.CharField(max_length=255, blank=True, null=True)
    Store = models.CharField(max_length=255, blank=True, null=True)
    ItemCode = models.CharField(max_length=255, blank=True, null=True)
    HSNCode = models.CharField(max_length=255, blank=True, null=True)
    Description = models.CharField(max_length=255, blank=True, null=True)
    Purpose = models.CharField(max_length=255, blank=True, null=True)
    Unit = models.CharField(max_length=255, blank=True, null=True)
    Rate= models.CharField(max_length=255, blank=True, null=True)
    Qty = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.SelectItem} - {self.SelectItem}"

# Store Module:- SecondDeliveryChallan
class SecondDeliveryChallan(models.Model):
    ChallanNo = models.CharField(max_length=255, blank=True, null=True)
    VehicleNo = models.CharField(max_length=255, blank=True, null=True)
    Contractor = models.CharField(max_length=255, blank=True, null=True)
    ChallanDate = models.DateField()
    Transport = models.CharField(max_length=255, blank=True, null=True)
    EWayBillNo = models.CharField(max_length=255, blank=True, null=True)
    PoNo = models.CharField(max_length=255, blank=True, null=True)
    Ref_Person = models.CharField(max_length=255, blank=True, null=True)
    LrNo = models.CharField(max_length=255, blank=True, null=True)
    PoDate = models.CharField(max_length=255, blank=True, null=True)
    Department = models.CharField(max_length=255, blank=True, null=True)
    Remark = models.CharField(max_length=255, blank=True, null=True)
    AssessableValue = models.CharField(max_length=255, blank=True, null=True)
    CGST = models.CharField(max_length=255, blank=True, null=True)
    SGST = models.CharField(max_length=255, blank=True, null=True)
    IGST = models.CharField(max_length=255, blank=True, null=True)
    GrandTotal = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.SelectItem} - {self.SelectItem}"

# Store Module:- DC_GRN
class DC_GRN(models.Model):
    GrnNo = models.CharField(max_length=255, blank=True, null=True)
    GrnDate = models.CharField(max_length=255, blank=True, null=True)
    GrnTime = models.CharField(max_length=255, blank=True, null=True)
    ChallanNo = models.CharField(max_length=255, blank=True, null=True)
    ChallanDate = models.DateField()
    InvoiceNo = models.CharField(max_length=255, blank=True, null=True)
    InvoiceDate = models.DateField()
    VehicleNo = models.CharField(max_length=255, blank=True, null=True)
    LrNo = models.CharField(max_length=255, blank=True, null=True)
    Transporter = models.CharField(max_length=255, blank=True, null=True)
    PreparedBy = models.CharField(max_length=255, blank=True, null=True)
    CheckedBy = models.CharField(max_length=255, blank=True, null=True)
    Remark = models.CharField(max_length=255, blank=True, null=True)
    DeliveryInTime = models.BooleanField(default=True)
    QcCheck = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.GrnNo} - {self.GrnNo}"







    

# Item Master General Page All Fields With MainGroup & Item Group Code
class MainGroup(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class ItemGroup(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class ItemTable(models.Model):
    main_group = models.ForeignKey(MainGroup, on_delete=models.CASCADE)
    item_group = models.ForeignKey(ItemGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField()
    part_no = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.part_no:  # Generate part_no if not set
            last_item = ItemTable.objects.filter(main_group=self.main_group, item_group=self.item_group).order_by('-id').first()
            last_number = 1 if not last_item else int(last_item.part_no[-3:]) + 1
            self.part_no = f"{self.main_group.name[:2].upper()}{self.item_group.name[:2].upper()}{str(last_number).zfill(3)}"
            
        super().save(*args, **kwargs)




# New Material Issue
class MaterialChallan(models.Model):
    Plant = models.CharField(max_length=255, blank=True, null=True)
    ChallanNo = models.CharField(max_length=255, blank=True, null= True)
    Series = models.CharField(max_length=255, blank=True, null=True)
    Type = models.CharField(max_length=255, blank=True, null=True)
    Item = models.CharField(max_length=255, blank=True, null=True)
    ItemDescription = models.CharField(max_length=255, blank=True, null=True)
    Available = models.CharField(max_length=255, blank=True, null=True)
    Stock = models.CharField(max_length=255, blank=True, null=True)
    Machine = models.CharField(max_length=255, blank=True, null=True)
    StoreName = models.CharField(max_length=255, blank=True, null=True)
    Qty = models.CharField(max_length=255, blank=True, null=True)
    Unit = models.CharField(max_length=255, blank=True, null=True)
    Remark = models.CharField(max_length=255, blank=True, null=True)
    MrnNo = models.CharField(max_length=255, blank=True, null=True)
    Employee = models.CharField(max_length=255, blank=True, null=True)
    Dept = models.CharField(max_length=255, blank=True, null=True)
    MaterialIssueDate = models.CharField(max_length=255, blank=True, null=True)
    MaterialIssueTime = models.CharField(max_length=255, blank=True, null=True)
    Contractor = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.Series} - {self.Type}"
    
class MaterialChallanTable(models.Model):
    MaterialChallanDetail = models.ForeignKey(MaterialChallan, related_name="MaterialChallanTable", on_delete=models.CASCADE )
    ItemDescription = models.CharField(max_length=255, blank=True, null=True)
    Stock = models.CharField(max_length=255, blank=True, null=True)
    Qty = models.CharField(max_length=255, blank=True, null=True)
    Unit = models.CharField(max_length=255, blank=True, null=True)
    Machine = models.CharField(max_length=255, blank=True, null=True)
    NatureOfWork = models.CharField(max_length=255, blank=True, null=True)
    MrnNo = models.CharField(max_length=255, blank=True, null=True)
    CoilNo = models.CharField(max_length=255, blank=True, null=True)
    Employee = models.CharField(max_length=255, blank=True, null=True)
    Dept = models.CharField(max_length=255, blank=True, null=True)    

    def __str__(self):
        return f"{self.ItemDescription} - {self.Stock}"
    


# New DC GRN
class NewDCgrn(models.Model):
    Plant = models.CharField(max_length=255, blank=True, null=True)
    DCGRNno = models.CharField(max_length=255, blank=True, null=True)
    Type = models.CharField(max_length=255, blank=True, null=True)
    GateEntryNo = models.CharField(max_length=255, blank=True, null=True)
    Series = models.CharField(max_length=255, blank=True, null=True)
    SuppCust = models.CharField(max_length=255, blank=True, null=True)
    SelectDC = models.CharField(max_length=255, blank=True, null=True)
    Item = models.CharField(max_length=255, blank=True, null=True)

    GRNno = models.CharField(max_length=255, blank=True, null=True)
    GRNDate = models.CharField(max_length=255, blank=True, null=True)
    GRNTime = models.CharField(max_length=255, blank=True, null=True)
    ChallanNo = models.CharField(max_length=255, blank=True, null=True)
    ChallanDate = models.CharField(max_length=255, blank=True, null=True)
    VehicleNo = models.CharField(max_length=255, blank=True, null=True)
    LRno = models.CharField(max_length=255, blank=True, null=True)
    Trasporter = models.CharField(max_length=255, blank=True, null=True)
    PreparedBy = models.CharField(max_length=255, blank=True, null=True)
    CheckedByApprovedBy = models.CharField(max_length=255, blank=True, null=True)
    Remark = models.CharField(max_length=255, blank=True, null=True)
    DeliveryInTime = models.CharField(max_length=255, blank=True, null=True)
    QCcheck = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.DCGRNno

class NewDCgrnTable(models.Model):
    NewDCgrnDetail = models.ForeignKey(NewDCgrn, related_name="NewDCgrnTable", on_delete=models.CASCADE)
    DCno = models.CharField(max_length=255, blank=True, null=True)
    Date = models.CharField(max_length=255, blank=True, null=True)
    ItemCode = models.CharField(max_length=255, blank=True, null=True)
    Description = models.CharField(max_length=255, blank=True, null=True)
    Rate = models.CharField(max_length=255, blank=True, null=True)
    DCqty = models.CharField(max_length=255, blank=True, null=True)
    Balqty = models.CharField(max_length=255, blank=True, null=True)
    Chalqty = models.CharField(max_length=255, blank=True, null=True)
    GRNqty = models.CharField(max_length=255, blank=True, null=True)
    ShortExcessqty = models.CharField(max_length=255, blank=True, null=True)
    UnitCode = models.CharField(max_length=255, blank=True, null=True)
    Total = models.CharField(max_length=255, blank=True, null=True)
    HeatCode = models.CharField(max_length=255, blank=True, null=True)
    Remark = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.ItemCode
    

# 57-F4 GRN(Inward Challan)
class InwardChallan2(models.Model):
    Routing = models.CharField(max_length=255, blank=True, null=True)
    Plant = models.CharField(max_length=255, blank=True, null=True)
    Series = models.CharField(max_length=255, blank=True, null=True)
    InwardChallanNo = models.CharField(max_length=255, blank=True, null=True)
    GateEntryNo = models.CharField(max_length=255, blank=True, null=True)
    SupplierName = models.CharField(max_length=255, blank=True, null=True)
    OutwardChallan = models.CharField(max_length=255, blank=True, null=True)
    ItemName = models.CharField(max_length=255, blank=True, null=True)
    InwardF4No = models.CharField(max_length=255, blank=True, null=True)
    InwardDate = models.CharField(max_length=255, blank=True, null=True)
    InwardTime = models.CharField(max_length=255, blank=True, null=True)
    ChallanNo = models.CharField(max_length=255, blank=True,  null=True)
    ChallanDate = models.CharField(max_length=255, blank=True, null=True)
    GateEntryNo = models.CharField(max_length=255, blank=True, null=True)
    InvoiceNo = models.CharField(max_length=255, blank=True, null=True)
    InvoiceDate = models.CharField(max_length=255, blank=True, null=True)
    EwayBillQty = models.CharField(max_length=255, blank=True, null=True)
    EwayBillNo = models.CharField(max_length=255, blank=True, null=True)
    VehicleNo = models.CharField(max_length=255, blank=True, null=True)
    LrNo = models.CharField(max_length=255, blank=True, null=True)
    Transporter = models.CharField(max_length=255, blank=True, null=True)
    PreparedBy = models.CharField(max_length=255, blank=True, null=True)
    CheckedBy = models.CharField(max_length=255, blank=True, null=True)
    TcNo = models.CharField(max_length=255, blank=True, null=True)
    TcDate = models.CharField(max_length=255, blank=True, null=True)
    Remark = models.CharField(max_length=255, blank=True, null=True)
    DeliveryInTime = models.CharField(max_length=255, blank=True, null=True)
    TotalItem = models.CharField(max_length=255, blank=True, null=True)
    TotalQtyNo = models.CharField(max_length=255, blank=True, null=True)
    TotalQtyKg = models.CharField(max_length=255, blank=True, null=True)
    Store = models.CharField(max_length=255, blank=True, null=True)
    TOC = models.CharField(max_length=255, blank=True, null=True)
    PackFwrdCharges = models.CharField(max_length=255, blank=True, null=True)
    TransportCharges = models.CharField(max_length=255, blank=True, null=True)
    Insurance = models.CharField(max_length=255, blank=True, null=True)
    InstallationCharge= models.CharField(max_length=255, blank=True, null=True)
    OtherCharges = models.CharField(max_length=255, blank=True, null=True)
    CGST = models.CharField(max_length=255, blank=True, null=True)
    SGST = models.CharField(max_length=255, blank=True, null=True)
    IGST = models.CharField(max_length=255, blank=True, null=True)
    TCS = models.CharField(max_length=255, blank=True, null=True)
    GRTotal = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.GateEntryNo

class InwardChallanTable(models.Model):
    InwardChallanDetail = models.ForeignKey(InwardChallan2, related_name="InwardChallanTable", on_delete=models.CASCADE)
    OutNo = models.CharField(max_length=255, blank=True, null=True)
    OutDate = models.CharField(max_length=255, blank=True, null=True)
    ItemDescription = models.CharField(max_length=255, blank=True, null=True)
    OutIn = models.CharField(max_length=255, blank=True, null=True)
    Unit = models.CharField(max_length=255, blank=True, null=True)
    OutQty = models.CharField(max_length=255, blank=True, null=True)
    BalQty = models.CharField(max_length=255, blank=True, null=True)
    ChallanQty = models.CharField(max_length=255, blank=True, null=True)
    InQtyNOS = models.CharField(max_length=255, blank=True, null=True)
    InQtyKg = models.CharField(max_length=255, blank=True, null=True)
    JwRate = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.OutNo

class InwardChallanGSTDetails(models.Model):
    InwardChallanDetail = models.ForeignKey(InwardChallan2, related_name="InwardChallanGSTDetails", on_delete=models.CASCADE)
    ItemCode = models.CharField(max_length=255, blank=True, null=True)
    SACCode = models.CharField(max_length=255, blank=True, null=True)
    PORate = models.CharField(max_length=255, blank=True, null=True)
    RateType = models.CharField(max_length=255, blank=True, null=True)
    Qty = models.CharField(max_length=255, blank=True, null=True)
    Discount = models.CharField(max_length=255, blank=True, null=True)
    PackAmt = models.CharField(max_length=255, blank=True, null=True)
    TransAmt = models.CharField(max_length=255, blank=True, null=True)
    AssValue = models.CharField(max_length=255, blank=True, null=True)
    CGST = models.CharField(max_length=255, blank=True, null=True)
    SGST = models.CharField(max_length=255, blank=True, null=True)
    IGST = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.ItemCode


# Subcon GRN:- JobWork Inward-Challan
class JobworkInwardChallan(models.Model):
    Plant = models.CharField(max_length=255, blank=True, null=True)
    Series = models.CharField(max_length=255, blank=True, null=True)
    NO = models.CharField(max_length=255, blank=True, null=True)
    GateEntryNo = models.CharField(max_length=255, blank=True, null=True)
    Customer = models.CharField(max_length=255, blank=True, null=True)
    SelectItem = models.CharField(max_length=255, blank=True, null=True)
    ItemCode = models.CharField(max_length=255, blank=True, null=True)
    FGPartCode = models.CharField(max_length=255, blank=True, null=True)
    ChallanQty = models.CharField(max_length=255, blank=True, null=True)
    GRNQty = models.CharField(max_length=255, blank=True, null=True)
    MaterialRate = models.CharField(max_length=255, blank=True, null=True)
    HeatNo = models.CharField(max_length=255, blank=True, null=True)
    CustHeatNo = models.CharField(max_length=255, blank=True, null=True)
    RMSpecification = models.CharField(max_length=255, blank=True, null=True)
    PaticularNatureOfProcess = models.CharField(max_length=255, blank=True, null=True)
    InwardF4No = models.CharField(max_length=255, blank=True, null=True)
    InwardDate = models.CharField(max_length=255, blank=True, null=True)
    InwardTime = models.CharField(max_length=255, blank=True, null=True)
    ChallanNo = models.CharField(max_length=255, blank=True, null=True)
    ChallanDate = models.CharField(max_length=255, blank=True, null=True)
    SubVendor = models.CharField(max_length=255, blank=True, null=True)
    DCNo = models.CharField(max_length=255, blank=True, null=True)
    DCDate = models.CharField(max_length=255, blank=True, null=True)
    WayBillQty = models.CharField(max_length=255, blank=True, null=True)
    WayBillNo = models.CharField(max_length=255, blank=True, null=True)
    VehicleNo = models.CharField(max_length=255, blank=True, null=True)
    LrNo = models.CharField(max_length=255, blank=True, null=True)
    Transporter = models.CharField(max_length=255, blank=True, null=True)
    PrepartedBy = models.CharField(max_length=255, blank=True, null=True)
    CheckedBy = models.CharField(max_length=255, blank=True, null=True)
    VehicleInTime = models.CharField(max_length=255, blank=True, null=True)
    TCNo = models.CharField(max_length=255, blank=True, null=True)
    TCDate = models.CharField(max_length=255, blank=True, null=True)
    Remark = models.CharField(max_length=255, blank=True, null=True)
    DevileryInTime = models.CharField(max_length=255, blank=True, null=True)
    ClearingStatus = models.CharField(max_length=255, blank=True, null=True)
    VehicleOutTime = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.Series
    
class JobworkInwardChallanTable(models.Model):
    JobworkInwardChallanDetail = models.ForeignKey(JobworkInwardChallan, related_name="JobworkInwardChallanTable", on_delete=models.CASCADE)
    ItemCode = models.CharField(max_length=255, blank=True, null=True)
    Operation = models.CharField(max_length=255, blank=True, null=True)
    ChallanQty = models.CharField(max_length=255, blank=True, null=True)
    GRNQty = models.CharField(max_length=255, blank=True, null=True)
    MaterialRate = models.CharField(max_length=255, blank=True, null=True)
    HeatNo = models.CharField(max_length=255, blank=True, null=True)
    CustHeatNo = models.CharField(max_length=255, blank=True, null=True)
    ParticularNatureOfProcess = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.ItemCode 
    

# models.py
from django.db import models
from django.utils import timezone

class FGMovement(models.Model):
    # Transaction details
    trn_no = models.CharField(max_length=50, unique=True, blank=True)
    date = models.DateField(default=timezone.now)
    
    # Item details
    fg_item_code = models.CharField(max_length=100)
    fg_item_name = models.CharField(max_length=255)
    fg_item_description = models.TextField(blank=True)
    
    # Operation details
    operation = models.CharField(max_length=100, blank=True)
    
    # Quantities
    ok_qty = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    rework_qty = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    reject_qty = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # Additional details
    heat_code = models.CharField(max_length=50, blank=True)
    stock_view = models.CharField(max_length=50, default='All')
    remark = models.TextField(blank=True)
    
    # System fields
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'fg_movement'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"FG Movement {self.trn_no} - {self.fg_item_code}"
    
    def save(self, *args, **kwargs):
        # Auto-generate transaction number if not provided
        if not self.trn_no:
            last_movement = FGMovement.objects.filter(
                trn_no__startswith='FGM'
            ).order_by('-id').first()
            
            if last_movement:
                last_num = int(last_movement.trn_no.replace('FGM', ''))
                self.trn_no = f'FGM{last_num + 1:06d}'
            else:
                self.trn_no = 'FGM000001'
        
        super().save(*args, **kwargs)