from django.db import models

# GST Rate Master models
class TaxDetails(models.Model):
    HSN_SAC_Code = models.CharField(max_length=255)
    HSN_SAC_Desc = models.CharField(max_length=255)
    CGST = models.CharField(max_length=20)
    SGST = models.CharField(max_length=20)
    IGST = models.CharField(max_length=20)
    UTGST = models.CharField(max_length=20)	    
    export_SGST = models.CharField(max_length=20)
    export_CGST = models.CharField(max_length=20)
    export_IGST = models.CharField(max_length=20)
    Cess = models.CharField(max_length=20)
    Is_Exempt = models.CharField(max_length=20)
    Type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.HSN_SAC_Code} - {self.HSN_SAC_Desc}"


# Tax Code Master models
class TaxCode(models.Model):
    Tax_Code = models.CharField(max_length=20)
    Tax_Desc = models.CharField(max_length=255)
    Module= models.CharField(max_length=255)
    GST_Tax_Code = models.CharField(max_length=20)
    CGST  = models.CharField(max_length=20)
    SGST = models.CharField(max_length=20)
    IGST = models.CharField(max_length=20)
    Cess = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.Tax_Code} - {self.Tax_Desc}"
    

#Cust-Wise GST Master
class Cut_Wise(models.Model):
    HSN_Code = models.CharField(max_length=50, blank=True, null=True)
    Cust_Name = models.CharField(max_length=50, blank=True, null=True)
    Item = models.CharField(max_length=50, blank=True, null=True)
    Cust_PO_NO = models.CharField(max_length=50, blank=True, null=True)
    CGST = models.CharField(max_length=50, blank=True, null=True)
    SGST = models.CharField(max_length=50, blank=True, null=True)
    IGST = models.CharField(max_length=50, blank=True, null=True)
    UTGST = models.CharField(max_length=50, blank=True, null=True)
    EXPORT_CGST = models.CharField(max_length=50, blank=True, null=True)
    EXPORT_SGST = models.CharField(max_length=50, blank=True, null=True)
    EXPORT_IGST = models.CharField(max_length=50, blank=True, null=True)
    CESS = models.CharField(max_length=50, blank=True, null=True)
    
     
    def __str__(self):
        return f"{self.HSN_Code} - {self.HSN_Code}"
    


#GST RATE EXCEL UPLOAD
from django.db import models

class ExcelFile(models.Model):
    file = models.FileField(upload_to='excel_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

    

# Item Master models      _________________remaining work.____________________
class ItemMaster(models.Model):
    Main_Group = models.CharField(max_length=50, blank=True, null=True)
    SE_Item = models.CharField(max_length=50, blank=True, null=True)
    Unit_Code = models.CharField(max_length=50, blank=True, null=True)
    Part_Code = models.CharField(max_length=50, blank=True, null=True)
    Cut_Weight_kg = models.CharField(max_length=50, blank=True, null=True)
    Rate = models.CharField(max_length=50, blank=True, null=True)
    Revision_No = models.CharField(max_length=50, blank=True, null=True)
    Item_Size = models.CharField(max_length=50, blank=True, null=True)
    Heat_Treatment = models.CharField(max_length=50, blank=True, null=True)
    Color_Code = models.CharField(max_length=50, blank=True, null=True)
    Min_Rate = models.CharField(max_length=50, blank=True, null=True)
    Length = models.CharField(max_length=50, blank=True, null=True)
    Shape = models.CharField(max_length=50, blank=True, null=True)
    Rate_Remark = models.CharField(max_length=50, blank=True, null=True)
    Metal_Type = models.CharField(max_length=50, blank=True, null=True)
    Specific_Gravity = models.CharField(max_length=50, blank=True, null=True)
    Item_Group = models.CharField(max_length=50, blank=True, null=True)
    Name_Description = models.CharField(max_length=50, blank=True, null=True)
    Store_Location = models.CharField(max_length=50, blank=True, null=True)
    Route = models.CharField(max_length=50, blank=True, null=True)
    Parent_FG_Code = models.CharField(max_length=50, blank=True, null=True)
    Finish_Weight = models.CharField(max_length=50, blank=True, null=True)
    Sector = models.CharField(max_length=50, blank=True, null=True)
    SAC_Code = models.CharField(max_length=50, blank=True, null=True)
    Item_Sector = models.CharField(max_length=50, blank=True, null=True)
    Hardness = models.CharField(max_length=50, blank=True, null=True)
    Male = models.CharField(max_length=50, blank=True, null=True)
    Max_Rate = models.CharField(max_length=50, blank=True, null=True)
    Thickness = models.CharField(max_length=50, blank=True, null=True)
    Diameter = models.CharField(max_length=50, blank=True, null=True)
    Other_Desce = models.CharField(max_length=50, blank=True, null=True)
    Metal = models.CharField(max_length=50, blank=True, null=True)
    Finish = models.CharField(max_length=50, blank=True, null=True)
    Subgroup = models.CharField(max_length=50, blank=True, null=True)
    HSN_SAC_Code = models.CharField(max_length=50, blank=True, null=True)
    Gross_Weight = models.CharField(max_length=50, blank=True, null=True)
    Tool_Die_Life = models.CharField(max_length=50, blank=True, null=True)
    Resharpening_Reconditionning = models.CharField(max_length=50, blank=True, null=True)
    Item_ClassName = models.CharField(max_length=50, blank=True, null=True)
    QC_Application = models.CharField(max_length=50, blank=True, null=True)
    Jominy = models.CharField(max_length=50, blank=True, null=True)
    Microstructure = models.CharField(max_length=50, blank=True, null=True)
    Drawing_No = models.CharField(max_length=50, blank=True, null=True)
    Width = models.CharField(max_length=50, blank=True, null=True)
    Old_ERP_Code = models.CharField(max_length=50, blank=True, null=True)
    Note = models.CharField(max_length=50, blank=True, null=True)
    KgMM3 = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self. Main_Group} - {self.Main_Group}"

# Item Master:- General Table

from django.contrib.auth.models import User 

class ItemTable(models.Model):
    main_group = models.CharField(max_length=50, blank=True, null=True)
    item_group = models.CharField(max_length=50, blank=True, null=True)
    part_no = models.CharField(max_length=100, unique=True)
    Unit_Code = models.CharField(max_length=50, blank=True, null=True)
    Part_Code = models.CharField(max_length=50, blank=True, null=True)
    Cut_Weight_kg = models.CharField(max_length=50, blank=True, null=True)
    Rate = models.CharField(max_length=50, blank=True, null=True)
    Revision_No = models.CharField(max_length=50, blank=True, null=True)
    Item_Size = models.CharField(max_length=50, blank=True, null=True)
    Heat_Treatment = models.CharField(max_length=50, blank=True, null=True)
    Color_Code = models.CharField(max_length=50, blank=True, null=True)
    Min_Rate = models.CharField(max_length=50, blank=True, null=True)
    Length = models.CharField(max_length=50, blank=True, null=True)
    Shape = models.CharField(max_length=50, blank=True, null=True)
    Rate_Remark = models.CharField(max_length=50, blank=True, null=True)
    Metal_Type = models.CharField(max_length=50, blank=True, null=True)
    Specific_Gravity = models.CharField(max_length=50, blank=True, null=True)
    Name_Description = models.CharField(max_length=50, blank=True, null=True)
    Store_Location = models.CharField(max_length=50, blank=True, null=True)
    Route = models.CharField(max_length=50, blank=True, null=True)
    Parent_FG_Code = models.CharField(max_length=50, blank=True, null=True)
    Finish_Weight = models.CharField(max_length=50, blank=True, null=True)
    Sector = models.CharField(max_length=50, blank=True, null=True)
    SAC_Code = models.CharField(max_length=50, blank=True, null=True)
    Item_Sector = models.CharField(max_length=50, blank=True, null=True)
    Hardness = models.CharField(max_length=50, blank=True, null=True)
    Male = models.CharField(max_length=50, blank=True, null=True)
    Max_Rate = models.CharField(max_length=50, blank=True, null=True)
    Thickness = models.CharField(max_length=50, blank=True, null=True)
    Diameter = models.CharField(max_length=50, blank=True, null=True)
    Other_Desce = models.CharField(max_length=50, blank=True, null=True)
    Metal = models.CharField(max_length=50, blank=True, null=True)
    Finish = models.CharField(max_length=50, blank=True, null=True)
    Subgroup = models.CharField(max_length=50, blank=True, null=True)
    HSN_SAC_Code = models.CharField(max_length=50, blank=True, null=True)
    Gross_Weight = models.CharField(max_length=50, blank=True, null=True)
    Tool_Die_Life = models.CharField(max_length=50, blank=True, null=True)
    Resharpening_Reconditionning = models.CharField(max_length=50, blank=True, null=True)
    Item_ClassName = models.CharField(max_length=50, blank=True, null=True)
    QC_Application = models.CharField(max_length=50, blank=True, null=True)
    Jominy = models.CharField(max_length=50, blank=True, null=True)
    Microstructure = models.CharField(max_length=50, blank=True, null=True)
    Drawing_No = models.CharField(max_length=50, blank=True, null=True)
    Width = models.CharField(max_length=50, blank=True, null=True)
    Old_ERP_Code = models.CharField(max_length=50, blank=True, null=True)
    Note = models.CharField(max_length=50, blank=True, null=True)
    KgMM3 = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_verified = models.BooleanField(default=True)
    
    def __str__(self):
      return f"Item {self.pk or 'New'}"
    
# Item Master models Data2
class Item_Master_Data2_Model(models.Model):
    item = models.OneToOneField(ItemTable, related_name='item_master_data', on_delete=models.CASCADE)
    Max_GRN_Qty = models.CharField(max_length=50, blank=True, null=True)
    Scrap_Rate = models.CharField(max_length=50, blank=True, null=True)
    Machine = models.CharField(max_length=50, blank=True, null=True)
    Item_Shelf_Life = models.CharField(max_length=50, blank=True, null=True)
    Item_Wip_Wt = models.CharField(max_length=50, blank=True, null=True)
    Min_Level = models.CharField(max_length=50, blank=True, null=True)
    Inventry_Service = models.CharField(max_length=50, blank=True, null=True)
    CPC_Code = models.CharField(max_length=50, blank=True, null=True)
    Auxiliary_Factor = models.CharField(max_length=50, blank=True, null=True)
    Department = models.CharField(max_length=50, blank=True, null=True)
    Mechanical_Std = models.CharField(max_length=50, blank=True, null=True)
    Tool_Layout_No = models.CharField(max_length=50, blank=True, null=True)
    Is_Service = models.CharField(max_length=50, blank=True, null=True)
    Sales_Conversion_Factor = models.CharField(max_length=50, blank=True, null=True)
    GRN_Conversion_Factor = models.CharField(max_length=50, blank=True, null=True)
    Packing_Cost = models.CharField(max_length=50, blank=True, null=True)
    Production_Lead_Time = models.CharField(max_length=50, blank=True, null=True)
    Buyer = models.CharField(max_length=50, blank=True, null=True)
    Qty_Packing = models.CharField(max_length=50, blank=True, null=True)
    Item_Category = models.CharField(max_length=50, blank=True, null=True)
    Machine_Weight = models.CharField(max_length=50, blank=True, null=True)
    Buffer_Qty = models.CharField(max_length=50, blank=True, null=True)
    MOQ = models.CharField(max_length=50, blank=True, null=True)
    Max_Level = models.CharField(max_length=50, blank=True, null=True)
    BOM_Type = models.CharField(max_length=50, blank=True, null=True)
    Product_Category = models.CharField(max_length=50, blank=True, null=True)
    Over_Head_Rate = models.CharField(max_length=50, blank=True, null=True)
    Valuation_Method = models.CharField(max_length=50, blank=True, null=True)
    Dimensional_Std_Reference = models.CharField(max_length=50, blank=True, null=True)
    Raw_Material_Grade = models.CharField(max_length=50, blank=True, null=True)
    RM_Tolerance = models.CharField(max_length=50, blank=True, null=True)
    FG_Std_Cavity = models.CharField(max_length=50, blank=True, null=True)
    Design_Cost = models.CharField(max_length=50, blank=True, null=True)
    Transport_Cost = models.CharField(max_length=50, blank=True, null=True)
    Purchase_Lead_Time = models.CharField(max_length=50, blank=True, null=True)
    Business_Head = models.CharField(max_length=50, blank=True, null=True)
    Project_Name = models.CharField(max_length=50, blank=True, null=True)
    Department = models.CharField(max_length=50, blank=True, null=True)
    Eoonomical_Batch_Size = models.CharField(max_length=50, blank=True, null=True)
    Re_Order_Level = models.CharField(max_length=50, blank=True, null=True)
    Pre_Shift_Qty = models.CharField(max_length=50, blank=True, null=True)
    Scrap_Item = models.CharField(max_length=50, blank=True, null=True)
    Scrap_Qty = models.CharField(max_length=50, blank=True, null=True)
    Purchase_GL = models.CharField(max_length=50, blank=True, null=True)
    Business_Associate = models.CharField(max_length=50, blank=True, null=True)    

# Item Master Technical Specification
class Technical_Specification_Model(models.Model):
    item = models.ForeignKey(ItemTable, related_name='technical_specifications', on_delete=models.CASCADE)
    Specification = models.CharField(max_length=50, blank=True, null=True)
    Parameter = models.CharField(max_length=50, blank=True, null=True)

# Item Master NPD
class NPD_Model(models.Model):
    item = models.ForeignKey(ItemTable, related_name='npd_details', on_delete=models.CASCADE)
    NPD = models.CharField(max_length=50, blank=True, null=True)
    CustomerName = models.CharField(max_length=50, blank=True, null=True)
    NPD_Qty = models.CharField(max_length=50, blank=True, null=True)
    NPD_Due_Date = models.CharField(max_length=50, blank=True, null=True)

# Item Master MainGrop+ItemGroup Code Generated Code Model 

from django.db import models

class MainGroup2(models.Model):
    prefix = models.CharField(max_length=100, unique=True)
    subgroup_code = models.CharField(max_length=100, unique=True)
    subgroup_name = models.CharField(max_length=100, unique=True)
    inventory = models.CharField(max_length=10)

    def __str__(self):
        return self.prefix


class ItemGroup2(models.Model):
    main_group_name = models.CharField(max_length=100)
    prefix = models.CharField(max_length=100, unique=True, null=True, blank=True)
    group_name = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if self.prefix == "":
            self.prefix = None
        super().save(*args, **kwargs)


    def __str__(self):
        return self.group_name



  
    
# Item Master General Page Fields MainGroup
class MainGroup_Model(models.Model):
    Prefix = models.CharField(max_length=50, blank=True, null=True)
    Sub_Group_Code = models.CharField(max_length=50, blank=True, null=True)
    Sub_Group_Name = models.CharField(max_length=50, blank=True, null=True)
    Inventory = models.CharField(max_length=50, blank=True, null=True)

# Item Master General Page Fields UnitCode
class UnitCode_Model(models.Model):
    UnitName = models.CharField(max_length=50, blank=True, null=True)

# Item Master General Page Fields TDC
class TDC_Model(models.Model):
    Prefix = models.CharField(max_length=50, blank=True, null=True)
    Name = models.CharField(max_length=50, blank=True, null=True)
   
# Item Master General Page Fields MetalType
class MetalType_Model(models.Model):
    Prefix = models.CharField(max_length=50, blank=True, null=True)
    MetalType = models.CharField(max_length=50, blank=True, null=True)
    ItemSizeUnit = models.CharField(max_length=50, blank=True, null=True)

# Item Master General Page Fields Item Group
class Item_Group_Item_Master_Model(models.Model):
    MainGroupName = models.CharField(max_length=50, blank=True, null=True)
    Prefix = models.CharField(max_length=50, blank=True, null=True)
    GroupName = models.CharField(max_length=50, blank=True, null=True)


# Item Master General Page Fields Store Location
class Store_Location_Item_Master_Model(models.Model):
    EnterStoreName = models.CharField(max_length=50, blank=True, null=True)

# Item Master General Page Fields Route
class Route_Item_Master_Model(models.Model):
    Prefix = models.CharField(max_length=50, blank=True, null=True)
    Name = models.CharField(max_length=50, blank=True, null=True)

# Item Master General Page Fields Parent FG Code
class Parent_FG_Code_Item_Master_Model(models.Model):
    Parent_FG_Code = models.CharField(max_length=50, blank=True, null=True)

# Item Master General Page Fields Sector
class Sector_Item_Master_Model(models.Model):
    Sector_Prefix = models.CharField(max_length=50, blank=True, null=True)
    Sector_Name = models.CharField(max_length=50, blank=True, null=True)

# Item Master General Page Fields Item Section
class Item_Section_Item_Master_Model(models.Model):
    Prefix = models.CharField(max_length=50, blank=True, null=True)
    Section_Name = models.CharField(max_length=50, blank=True, null=True)

# Item Master General Page Fields Type/Grade New
class Type_Grade_New_Model(models.Model):
    SubGroup = models.CharField(max_length=50, blank=True, null=True)
    Prefix = models.CharField(max_length=50, blank=True, null=True)
    Item_Grade_Name = models.CharField(max_length=50, blank=True, null=True)
    Colour_Code = models.CharField(max_length=50, blank=True, null=True)


# Item Master General Page Fields Sub Group
class Sub_Group_Item_Master_Model(models.Model):
    Main_Group = models.CharField(max_length=50, blank=True, null=True)
    Sub_Group = models.CharField(max_length=50, blank=True, null=True)
    Prefix = models.CharField(max_length=50, blank=True, null=True)
    Name = models.CharField(max_length=50, blank=True, null=True)
 

# Item Master Data2 Page Fields Qty_Packing
class Qty_Packing_Model(models.Model):
    EnterUnit_Name = models.CharField(max_length=50, blank=True, null=True)





# Supplier_Customer_Masters
class Supplier_Customer(models.Model):
    Type = models.CharField(max_length=30, blank=True, null=True)
    Name = models.CharField(max_length=30, blank=True, null=True)
    Address_Line_1 = models.CharField(max_length=30, blank=True, null=True)
    Region = models.CharField(max_length=30, blank=True, null=True)
    PAN_NO = models.CharField(max_length=30, blank=True, null=True)
    PAN_Type = models.CharField(max_length=30, blank=True, null=True)
    State_Code = models.CharField(max_length=30, blank=True, null=True)
    GST_Tax_Code = models.CharField(max_length=30, blank=True, null=True)
    Email_Id = models.CharField(max_length=30, blank=True, null=True)
    Contact_No = models.CharField(max_length=30, blank=True, null=True)
    TCS = models.CharField(max_length=30, blank=True, null=True)
    Insurance_Policy_No = models.CharField(max_length=30, blank=True, null=True)
    Subcon_Challan = models.CharField(max_length=30, blank=True, null=True)
    GL = models.CharField(max_length=30, blank=True, null=True)
    Code_No = models.CharField(max_length=30, blank=True, null=True)
    Payment_Term = models.CharField(max_length=30, blank=True, null=True)
    Country = models.CharField(max_length=30, blank=True, null=True)
    Currency = models.CharField(max_length=30, blank=True, null=True)
    Pin_Code = models.CharField(max_length=30, blank=True, null=True)
    City = models.CharField(max_length=30, blank=True, null=True)
    TDS_Rate = models.CharField(max_length=30, blank=True, null=True)
    GST_No = models.CharField(max_length=30, blank=True, null=True)
    GST_No2 = models.CharField(max_length=30, blank=True, null=True)
    Invoice_Type = models.CharField(max_length=30, blank=True, null=True)
    CIN_No = models.CharField(max_length=30, blank=True, null=True)
    Website = models.CharField(max_length=30, blank=True, null=True)
    Incoterms = models.CharField(max_length=30, blank=True, null=True)
    Insurance_Policy_Expiry_Date = models.CharField(max_length=30, blank=True, null=True)
    VAT_TIN = models.CharField(max_length=30, blank=True, null=True)
    Montly_Sale = models.CharField(max_length=30, blank=True, null=True)
    Sector = models.CharField(max_length=30, blank=True, null=True)
    Group = models.CharField(max_length=30, blank=True, null=True)
    Distance = models.CharField(max_length=30, blank=True, null=True)
    Vendor_Code = models.CharField(max_length=30, blank=True, null=True)
    Legal_Name_GST = models.CharField(max_length=30, blank=True, null=True)
    Cust_Short_Name = models.CharField(max_length=30, blank=True, null=True)
    MSME_Type = models.CharField(max_length=30, blank=True, null=True)
    MSME_No = models.CharField(max_length=30, blank=True, null=True)
    LUT_No = models.CharField(max_length=30, blank=True, null=True)
    ISO = models.CharField(max_length=30, blank=True, null=True)
    QMSC_Code = models.CharField(max_length=30, blank=True, null=True)
    QMSC_Date = models.CharField(max_length=30, blank=True, null=True)
    Active = models.CharField(max_length=30, blank=True, null=True)
    Std_Packing = models.CharField(max_length=30, blank=True, null=True)
    Old_ERP_Code = models.CharField(max_length=30, blank=True, null=True)
    Delivery_Lead_Time = models.CharField(max_length=30, blank=True, null=True)
    EORI_No = models.CharField(max_length=30, blank=True, null=True)
    Montly_Purchase = models.CharField(max_length=30, blank=True, null=True)
    Discount_Per = models.CharField(max_length=30, blank=True, null=True)


    def __str__(self):
        return f"{self.Type} - {self.Type}"

    
# Supplier Masters Type:- Customer,Supplier,JobWork,CSJW
class Customer(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.code:
            last_code = Customer.objects.count() + 1
            self.code = f'C{last_code:04d}'
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.code:
            last_code = Supplier.objects.count() + 1
            self.code = f'S{last_code:04d}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class JobWork(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.code:
            last_code = JobWork.objects.count() + 1
            self.code = f'J{last_code:04d}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class CSJW(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.code:
            last_code = CSJW.objects.count() + 1
            self.code = f'J{last_code:04d}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name




# Supplier_Customer_Masters_General Type_Field_API
class Type_Model(models.Model):
    Prefix = models.CharField(max_length=30, blank=True, null=True)
    Category_Name = models.CharField(max_length=50, blank=True, null=True)


# Supplier_Customer_Masters_General Region_Field_API
class Region_Model(models.Model):
    RegionCode = models.CharField(max_length=50, blank=True, null=True)
    RegionName = models.CharField(max_length=50, blank=True, null=True)

# Supplier_Customer_Masters_General StateCode_Field_API
class StateCode_Model(models.Model):
    StateName = models.CharField(max_length=50, blank=True, null=True)
    State_No_Numeric = models.CharField(max_length=50, blank=True, null=True)
    State_Code_Alpha = models.CharField(max_length=50, blank=True, null=True)

# Supplier_Customer_Masters_General Payment_Term_Field_API
class PaymentTerm_Model(models.Model):
    Days = models.IntegerField()

# Supplier_Customer_Masters_General Country_Field_API
class Country_Model(models.Model):
    Code = models.CharField(max_length=50, blank=True, null=True)
    Country = models.CharField(max_length=50, blank=True, null=True)



# Supplier_Customer_Masters_General Currency_Field_API
class Currency_Model(models.Model):
    Code = models.CharField(max_length=50, blank=True, null=True)
    Symbol = models.CharField(max_length=50, blank=True, null=True)
    Description = models.CharField(max_length=50, blank=True, null=True)


# Supplier_Customer_Masters_General City_Field_API
class City_Model(models.Model):
    CityName = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.CityName} - {self.CityName}"

# Supplier_Customer_Masters_General Sector_Field_API
class Sector_Model(models.Model):
    Sector_Prefix = models.CharField(max_length=50, blank=True, null=True)
    SectorName = models.CharField(max_length=50, blank=True, null=True)

# Supplier_Customer_Masters_General Group_Field_API
class Group_Model(models.Model):
    Prefix = models.CharField(max_length=50, blank=True, null=True)
    Group = models.CharField(max_length=50, blank=True, null=True)

# Supplier_Customer_Masters_General QMSC_Code_Field_API
class QMSC_Code_Model(models.Model):
    QMSC_Code = models.CharField(max_length=50, blank=True, null=True)
    QMSC_Code_Desc = models.CharField(max_length=50, blank=True, null=True)


# Supplier Master Type:- Customer, Supplier, JobWork, CSJW
class SupplierType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} - {self.code}"

class CustomerType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} - {self.code}"

class JobworkType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} - {self.code}"

class CSJWType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"CSJW {self.name} - {self.code}"



# Cross Reference: Item Cross Reference
class Item_Cross_Model(models.Model):
    ItemName = models.CharField(max_length=50, blank=True, null=True)
    Cust_Supp_Name = models.CharField(max_length=50, blank=True, null=True)
    Cross_Ref_Item_No = models.CharField(max_length=50, blank=True, null=True)
    Cross_Ref_Item_Desc = models.CharField(max_length=50, blank=True, null=True)
    Remark = models.CharField(max_length=50, blank=True, null=True)
    Model = models.CharField(max_length=50, blank=True, null=True)
    ModelNo = models.CharField(max_length=50, blank=True, null=True)
    DrawingNo = models.CharField(max_length=50, blank=True, null=True)
    RevNo = models.CharField(max_length=50, blank=True, null=True)
    Min_Order_Qty = models.CharField(max_length=50, blank=True, null=True)
    Packing_Qty = models.CharField(max_length=50, blank=True, null=True)

# Cross Reference: Supplier Item 
class Supplier_Item_Model(models.Model):
    Cust_Supp_Name = models.CharField(max_length=50, blank=True, null=True)
    Main_Group = models.CharField(max_length=50, blank=True, null=True)
    ItemName = models.CharField(max_length=50, blank=True, null=True)
    Rate = models.CharField(max_length=50, blank=True, null=True)

# Cross Reference: Customer_Item_VA_Rate
class Item_VA_Rate_Model(models.Model):
    Cust_Supp_Name = models.CharField(max_length=50, blank=True, null=True)
    ItemName = models.CharField(max_length=50, blank=True, null=True)
    VARate1 = models.CharField(max_length=50, blank=True, null=True)
    VARate2 = models.CharField(max_length=50, blank=True, null=True)

# New Work Center Master: Add New
class Work_Center_Model(models.Model):
    Plant = models.CharField(max_length=50, blank=True, null=True)
    Category = models.CharField(max_length=50, blank=True, null=True)
    WorkCenterCode = models.CharField(max_length=50, blank=True, null=True)
    WorkCenterName = models.CharField(max_length=50, blank=True, null=True)
    WorkCenterType = models.CharField(max_length=50, blank=True, null=True)
    Mhr_Rate = models.CharField(max_length=50, blank=True, null=True)
    Electricity = models.CharField(max_length=50, blank=True, null=True)
    PPM_SPM = models.CharField(max_length=50, blank=True, null=True)
    PPM = models.CharField(max_length=50, blank=True, null=True)
    BatchQty = models.CharField(max_length=50, blank=True, null=True)
    Oil = models.CharField(max_length=50, blank=True, null=True)
    Proud_Hours = models.CharField(max_length=50, blank=True, null=True)
    Daily_Running_Hr = models.CharField(max_length=50, blank=True, null=True)
    Operator = models.CharField(max_length=50, blank=True, null=True)

# New Work Center Master: Machine Group Work Center Type Group
class Machine_Work_Center_Group_Model(models.Model):
    EnterType = models.CharField(max_length=50, blank=True, null=True)
    

# New Work Center Master: Work Center Type Group
class WorkCenterTypeGroup_Model(models.Model):
    TypeGroup = models.CharField(max_length=50, blank=True, null=True)
    Prod_Wt = models.CharField(max_length=50, blank=True, null=True)


# Cycle Time Master
class Cycle_Time_Master_Model(models.Model):
    Plant = models.CharField(max_length=50, blank=True, null=True)
    PartCode = models.CharField(max_length=50, blank=True, null=True)
    MachineType = models.CharField(max_length=50, blank=True, null=True)
    Machine = models.CharField(max_length=50, blank=True, null=True)
    OPTime = models.CharField(max_length=50, blank=True, null=True)
    Load_Unload_Time = models.CharField(max_length=50, blank=True, null=True)
    MO_Time = models.CharField(max_length=50, blank=True, null=True)
    Total_Time = models.CharField(max_length=50, blank=True, null=True)
    Time_in_Minutes = models.CharField(max_length=50, blank=True, null=True)


# Shift Master
class Shift_Master_Model(models.Model):
    Plant = models.CharField(max_length=50, blank=True, null=True)
    Shift_Name = models.CharField(max_length=50, blank=True, null=True)
    Shift_Prefix = models.CharField(max_length=50, blank=True, null=True)
    Shift_From = models.CharField(max_length=50, blank=True, null=True)
    Shift_Till = models.CharField(max_length=50, blank=True, null=True)
    Break_Name = models.CharField(max_length=50, blank=True, null=True)
    Break_Till = models.CharField(max_length=50, blank=True, null=True)
    Break_Time = models.CharField(max_length=50, blank=True, null=True)
    Total_Hours = models.CharField(max_length=50, blank=True, null=True)

# Add_New_Operator_Supervisor_Master
class Add_New_Operator_Model(models.Model):
    Department = models.CharField(max_length=50, blank=True, null=True)
    Name = models.CharField(max_length=50, blank=True, null=True)
    Address = models.CharField(max_length=50, blank=True, null=True)
    Contact_No = models.CharField(max_length=50, blank=True, null=True)
    Birth_Date = models.CharField(max_length=50, blank=True, null=True)
    Salary = models.CharField(max_length=50, blank=True, null=True)
    Date_Of_Leaving = models.CharField(max_length=50, blank=True, null=True)
    Aadhar_No = models.CharField(max_length=50, blank=True, null=True)
    Code = models.CharField(max_length=50, blank=True, null=True)
    Designation = models.CharField(max_length=50, blank=True, null=True)
    CorrespondingAddress = models.CharField(max_length=50, blank=True, null=True)
    Type = models.CharField(max_length=50, blank=True, null=True)
    Joining_Sal_Date = models.CharField(max_length=50, blank=True, null=True)
    Contractor = models.CharField(max_length=50, blank=True, null=True)
    DailyWorkHours = models.CharField(max_length=50, blank=True, null=True)
    PanNo = models.CharField(max_length=50, blank=True, null=True)
    BankName = models.CharField(max_length=50, blank=True, null=True)
    BankAccountNo = models.CharField(max_length=50, blank=True, null=True)
    BankIFSC_Code = models.CharField(max_length=50, blank=True, null=True)

# Add_New_Operator_Supervisor_Master: Department_Master
class Department_Master_Model(models.Model):
    SelectCategory = models.CharField(max_length=50, blank=True, null=True)
    EnterDeptName = models.CharField(max_length=50, blank=True, null=True)

# Add_New_Operator_Supervisor_Master: Department_Category_Master
class Department_Category_Master_Model(models.Model):
    CategoryName = models.CharField(max_length=50, blank=True, null=True)

# Add_New_Operator_Supervisor_Master: Designation Api Field
class Designation_Api_Model(models.Model):
    EnterType = models.CharField(max_length=50, blank=True, null=True)
  
# Add_New_Operator_Supervisor_Master: Contractor Api Field
class Contractor_Api_Model(models.Model):
    Plant = models.CharField(max_length=50, blank=True, null=True)
    ContractorName = models.CharField(max_length=50, blank=True, null=True)
    ContactNo = models.CharField(max_length=50, blank=True, null=True)
    GstNo = models.CharField(max_length=50, blank=True, null=True)
    NatureOfService = models.CharField(max_length=50, blank=True, null=True)
    Email = models.CharField(max_length=50, blank=True, null=True)
    RefCode = models.CharField(max_length=50, blank=True, null=True)
    Address = models.CharField(max_length=50, blank=True, null=True)
    PanNo = models.CharField(max_length=50, blank=True, null=True)
    Tds = models.CharField(max_length=50, blank=True, null=True)
    FirName = models.CharField(max_length=50, blank=True, null=True)


# Unit Conversion
class Unit_Conversion_Model(models.Model):
    SubGroup = models.CharField(max_length=50, blank=True, null=True)
    Item = models.CharField(max_length=50, blank=True, null=True)
    Unit = models.CharField(max_length=50, blank=True, null=True)
    StockQty = models.CharField(max_length=50, blank=True, null=True)
    StockUnit = models.CharField(max_length=50, blank=True, null=True)
    

# Contractor Master
class Contractor_Master_Model(models.Model):
    Plant = models.CharField(max_length=50, blank=True, null=True)
    ContractorName = models.CharField(max_length=50, blank=True, null=True)
    ContactNo = models.CharField(max_length=50, blank=True, null=True)
    GstNo = models.CharField(max_length=50, blank=True, null=True)
    NatureOfService = models.CharField(max_length=50, blank=True, null=True)
    Email = models.CharField(max_length=50, blank=True, null=True)
    RefCode = models.CharField(max_length=50, blank=True, null=True)
    Address = models.CharField(max_length=50, blank=True, null=True)
    PanNo = models.CharField(max_length=50, blank=True, null=True)
    Tds = models.CharField(max_length=50, blank=True, null=True)
    FirName = models.CharField(max_length=50, blank=True, null=True)

# Cost Center Master
class Cost_Center_Model(models.Model):
    Category_Code = models.CharField(max_length=50, blank=True, null=True)
    Cost_Center_Code = models.CharField(max_length=50, blank=True, null=True)
    Cost_Center_Desc = models.CharField(max_length=50, blank=True, null=True)

# Cost Center Master Add New
class Cost_Center_Master_Add_New_Model(models.Model):
    Category_Code = models.CharField(max_length=50, blank=True, null=True)
    Cost_Center_Desc = models.CharField(max_length=50, blank=True, null=True)


# Price List: Price List Master - Add Price List
class Add_Price_List_Model(models.Model):
    Select_Customer = models.CharField(max_length=50, blank=True, null=True)
    Select_Address = models.CharField(max_length=50, blank=True, null=True)
    Price_List_Code = models.CharField(max_length=50, blank=True, null=True)
    Price_List_Name = models.CharField(max_length=50, blank=True, null=True)
    Effective_From_Date = models.DateField()

# Price List: Price List Entry
class Price_List_Entry_Model(models.Model):
    Qty = models.CharField(max_length=50, blank=True, null=True)
    Rate = models.CharField(max_length=50, blank=True, null=True)
    Disk = models.CharField(max_length=50, blank=True, null=True)
    Weff_Date = models.DateField()
    Po_No = models.CharField(max_length=50, blank=True, null=True)
    Po_Date = models.DateField()
    Amd_No = models.CharField(max_length=50, blank=True, null=True)
    Amd_Date = models.DateField()
    Po_Line_No = models.CharField(max_length=50, blank=True, null=True)
    Po_Type = models.CharField(max_length=50, blank=True, null=True)
    Cust_Eff_Date = models.DateField()
    Remark = models.CharField(max_length=50, blank=True, null=True)


# Bom Routing Master: - Production Department Master
class Production_Department_Model(models.Model):
    Department_Name = models.CharField(max_length=50, blank=True, null=True)
    Short_Name = models.CharField(max_length=50, blank=True, null=True)


# Bom Routing Master: - Operation Master
class Operation_Master_Model(models.Model):
    Std_Otp = models.CharField(max_length=50, blank=True, null=True)
    Operation_Name = models.CharField(max_length=50, blank=True, null=True)
    Prefix = models.CharField(max_length=50, blank=True, null=True)
    Mhr_Rate = models.CharField(max_length=50, blank=True, null=True)
    BomQc = models.CharField(max_length=50, blank=True, null=True)
    ProductionDept = models.CharField(max_length=50, blank=True, null=True)
    MachineType = models.CharField(max_length=50, blank=True, null=True)
    Production_Cycle_Time = models.CharField(max_length=50, blank=True, null=True)
    Stop_Mc_Booking = models.CharField(max_length=50, blank=True, null=True)
    Per_Day_Prod_Qty = models.CharField(max_length=50, blank=True, null=True)


# Bom Routing Master: - Std Routing
class Std_Routing_Model(models.Model):
    Std_Routing_No = models.CharField(max_length=50, blank=True, null=True)
    Op_No = models.CharField(max_length=50, blank=True, null=True)
    Op_Name = models.CharField(max_length=50, blank=True, null=True)
    Part_Type = models.CharField(max_length=50, blank=True, null=True)
    Wip_Wt = models.CharField(max_length=50, blank=True, null=True)
    Op_Type = models.CharField(max_length=50, blank=True, null=True)
    QC = models.CharField(max_length=50, blank=True, null=True)
    Ass_Prod = models.CharField(max_length=50, blank=True, null=True)
    Part_Code = models.CharField(max_length=50, blank=True, null=True)


# Bom Routing Master: - Bom Item Group Details
class Bom_Item_Group_Model(models.Model):
    Bom_Item_Group = models.CharField(max_length=50, blank=True, null=True)
    Item = models.CharField(max_length=50, blank=True, null=True)
    Qty = models.CharField(max_length=50, blank=True, null=True)



# Item Main Group Api
from django.db import models

class Tool(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.code:  # Generate code if not already set
            self.code = f'{self.name.upper()}*0'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



########GST NUMBER
from django.db import models

class GSTNumber(models.Model):
    gst_number = models.CharField(max_length=15, unique=True)
    
    def __str__(self):
        return self.gst_number


from django.db import models
from django.contrib.auth.models import User 

class Item(models.Model):
    TYPE_CHOICES = [
        ('Customer', 'Customer'),
        ('Supplier', 'Supplier'),
        ('Job Work', 'Job Work'),
        ('C/S/J/W', 'C/S/J/W'),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    Name = models.CharField(max_length=300, blank=True, null=True)
    Address_Line_1 = models.CharField(max_length=30, blank=True, null=True)
    Region = models.CharField(max_length=30, blank=True, null=True)
    PAN_NO = models.CharField(max_length=30, blank=True, null=True)
    PAN_Type = models.CharField(max_length=30, blank=True, null=True)
    State_Code = models.CharField(max_length=30, blank=True, null=True)
    GST_Tax_Code = models.CharField(max_length=30, blank=True, null=True)
    Email_Id = models.CharField(max_length=30, blank=True, null=True)
    Contact_No = models.CharField(max_length=30, blank=True, null=True)
    TCS = models.CharField(max_length=30, blank=True, null=True)
    Insurance_Policy_No = models.CharField(max_length=30, blank=True, null=True)
    Subcon_Challan = models.CharField(max_length=30, blank=True, null=True)
    GL = models.CharField(max_length=30, blank=True, null=True)
    number = models.CharField(max_length=10)
    Payment_Term = models.CharField(max_length=30, blank=True, null=True)
    Country = models.CharField(max_length=30, blank=True, null=True)
    Currency = models.CharField(max_length=30, blank=True, null=True)
    Pin_Code = models.CharField(max_length=30, blank=True, null=True)
    City = models.CharField(max_length=30, blank=True, null=True)
    TDS_Rate = models.CharField(max_length=30, blank=True, null=True)
    GST_No = models.CharField(max_length=30, blank=True, null=True)
    GST_No2 = models.CharField(max_length=30, blank=True, null=True)
    Invoice_Type = models.CharField(max_length=30, blank=True, null=True)
    CIN_No = models.CharField(max_length=30, blank=True, null=True)
    Website = models.CharField(max_length=30, blank=True, null=True)
    Incoterms = models.CharField(max_length=30, blank=True, null=True)
    Insurance_Policy_Expiry_Date = models.CharField(max_length=30, blank=True, null=True)
    VAT_TIN = models.CharField(max_length=30, blank=True, null=True)
    Montly_Sale = models.CharField(max_length=30, blank=True, null=True)
    Sector = models.CharField(max_length=30, blank=True, null=True)
    Group = models.CharField(max_length=30, blank=True, null=True)
    Distance = models.CharField(max_length=30, blank=True, null=True)
    Vendor_Code = models.CharField(max_length=30, blank=True, null=True)
    Legal_Name_GST = models.CharField(max_length=30, blank=True, null=True)
    Cust_Short_Name = models.CharField(max_length=30, blank=True, null=True)
    MSME_Type = models.CharField(max_length=30, blank=True, null=True)
    MSME_No = models.CharField(max_length=30, blank=True, null=True)
    LUT_No = models.CharField(max_length=30, blank=True, null=True)
    ISO = models.CharField(max_length=30, blank=True, null=True)
    QMSC_Code = models.CharField(max_length=30, blank=True, null=True)
    QMSC_Date = models.CharField(max_length=30, blank=True, null=True)
    Active = models.CharField(max_length=30, blank=True, null=True)
    Std_Packing = models.CharField(max_length=30, blank=True, null=True)
    Old_ERP_Code = models.CharField(max_length=30, blank=True, null=True)
    Delivery_Lead_Time = models.CharField(max_length=30, blank=True, null=True)
    EORI_No = models.CharField(max_length=30, blank=True, null=True)
    Montly_Purchase = models.CharField(max_length=30, blank=True, null=True)
    Discount_Per = models.CharField(max_length=30, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_verified = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.Name} - {self.number}"


class Buyer_Contact(models.Model):
    item = models.ForeignKey(Item, related_name="buyer_contacts", on_delete=models.CASCADE)
    Person_Name = models.CharField(max_length=50, blank=True, null=True)
    Contact_No = models.CharField(max_length=50, blank=True, null=True)
    Email = models.CharField(max_length=50, blank=True, null=True)
    Department = models.CharField(max_length=50, blank=True, null=True)
    Designation = models.CharField(max_length=50, blank=True, null=True)
    Birth_Date = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.Person_Name}"


class Bank_Details(models.Model):
    item = models.ForeignKey(Item, related_name="bank_details", on_delete=models.CASCADE)
    Account_Holder_name = models.CharField(max_length=50, blank=True, null=True)
    Bank_Name = models.CharField(max_length=50, blank=True, null=True)
    Branch_Name = models.CharField(max_length=50, blank=True, null=True)
    Bank_Account = models.CharField(max_length=50, blank=True, null=True)
    IFSC_Code = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.Account_Holder_name}"


from .models import ItemTable  

class BOMItem(models.Model):
    item = models.ForeignKey(ItemTable, related_name='bom_items', on_delete=models.CASCADE)
    OPNo = models.CharField(max_length=50, blank=True, null=True)
    PartCode = models.CharField(max_length=50, blank=True, null=True)
    BOMPartType = models.CharField(max_length=50, blank=True, null=True)
    BomPartCode = models.CharField(max_length=500, blank=True, null=True)
    QtyKg = models.CharField(max_length=50, blank=True, null=True)
    ScrapCode = models.CharField(max_length=50, blank=True, null=True)
    ScracpQty = models.CharField(max_length=50, blank=True, null=True)
    QC = models.CharField(max_length=50, blank=True, null=True)
    AssProd = models.CharField(max_length=50, blank=True, null=True)
    ProdQty = models.CharField(max_length=50, blank=True, null=True)
    WipWt = models.CharField(max_length=50, blank=True, null=True)
    WipRate = models.CharField(max_length=50, blank=True, null=True)
    PieceRate = models.CharField(max_length=50, blank=True, null=True)
    OPRate = models.CharField(max_length=50, blank=True, null=True)
    Operation = models.CharField(max_length=50, null=True, blank=True)
    BomPartDesc = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.OPNo or "BOMItem"



#BOM: Item Part Master

class BOM_ItemPartMaster(models.Model):
   item = models.ForeignKey(ItemTable, on_delete=models.CASCADE, related_name='bompartmaster_entries', null=True, blank=True)
   Operation = models.CharField(max_length=50, blank=True, null=True)
   PartCode = models.CharField(max_length=50, blank=True, null=True)

   def __str__(self):
        return self.Operation


class PartCode(models.Model):
    name = models.CharField(max_length=100, unique=True)
    prefix = models.CharField(max_length=50)
    part_code = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
# PO GST CALUCLAT
class ItemTransaction(models.Model):
    supplier = models.ForeignKey(Item, on_delete=models.CASCADE)
    part_no = models.CharField(max_length=100)
    ItemDescription = models.CharField(max_length=255)
    ItemSize = models.CharField(max_length=100)
    Rate = models.CharField(max_length=20)
    Disc = models.CharField(max_length=20)
    Qty = models.CharField(max_length=20)
    Unit = models.CharField(max_length=20)
    Particular = models.CharField(max_length=255)
    MakeMillName = models.CharField(max_length=255)
    DeliveryDate = models.DateField()
    PartCode = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.part_no


# New Job Work Purchase Order

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

    