from rest_framework import serializers
from .models import * 
# from models import 




# GST Rate Master serializers
class  GSTMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxDetails
        fields = ['id', 'HSN_SAC_Code', 'HSN_SAC_Desc', 'CGST', 'SGST', 'IGST', 'UTGST', 'export_SGST',
                  'export_CGST', 'export_IGST', 'Cess', 'Is_Exempt', 'Type']
        
# TaxCode serializers
class TaxCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxCode
        fields = ['id', 'Tax_Code', 'Tax_Desc', 'Module', 'GST_Tax_Code', 'CGST', 'SGST', 'IGST', 'Cess']

#Cust-Wise GST Master
class Cut_WiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cut_Wise
        fields = ['id', 'HSN_Code', 'Cust_Name', 'Item', 'Cust_PO_NO', 'CGST', 'SGST', 'IGST', 'UTGST', 
                  'EXPORT_CGST', 'EXPORT_SGST', 'EXPORT_IGST', 'CESS']
        




#GST RATE EXCEL UPLOAD
from rest_framework import serializers
from .models import ExcelFile

class ExcelFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelFile
        fields = ['id', 'file', 'uploaded_at']


# Item Master Genral Page
class ItemMaster_Serializer(serializers.ModelSerializer):
    class Meta:
        model=ItemMaster
        fields = ['Main_Group', 'SE_Item', 'Unit_Code', 'Part_Code', 'Cut_Weight_kg', 'Rate', 
'Revision_No', 'Item_Size', 'Heat_Treatment', 'Color_Code', 'Min_Rate', 
'Length', 'Shape', 'Rate_Remark', 'Metal_Type', 'Specific_Gravity', 'Item_Group', 
'Name_Description', 'Store_Location', 'Route', 'Parent_FG_Code', 'Finish_Weight', 
'Sector', 'SAC_Code', 'Item_Sector', 'Hardness', 'Male', 'Max_Rate', 
'Thickness', 'Diameter', 'Other_Desce', 'Metal', 'Finish', 'Subgroup', 
'HSN_SAC_Code', 'Gross_Weight', 'Tool_Die_Life', 'Resharpening_Reconditionning', 
'Item_ClassName', 'QC_Application', 'Jominy', 'Microstructure', 'Drawing_No', 
'Width', 'Old_ERP_Code', 'Note', 'KgMM3']
        
# Item Master models Data2
class  Item_Master_Data2_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Item_Master_Data2_Model
        fields = ['id', 'Max_GRN_Qty', 'Scrap_Rate', 'Machine', 'Item_Shelf_Life', 'Item_Wip_Wt', 'Min_Level',
                   'Inventry_Service', 'CPC_Code', 'Auxiliary_Factor', 'Department', 'Mechanical_Std',
                     'Tool_Layout_No', 'Is_Service', 'Sales_Conversion_Factor', 'GRN_Conversion_Factor',
                       'Packing_Cost', 'Production_Lead_Time', 'Buyer', 'Qty_Packing', 'Item_Category',
                         'Machine_Weight', 'Buffer_Qty', 'MOQ', 'Max_Level', 'BOM_Type', 'Product_Category',
                           'Over_Head_Rate', 'Valuation_Method', 'Dimensional_Std_Reference',
                             'Raw_Material_Grade', 'RM_Tolerance', 'FG_Std_Cavity', 'Design_Cost',
                               'Transport_Cost', 'Purchase_Lead_Time', 'Business_Head', 'Project_Name',
                                 'Eoonomical_Batch_Size', 'Re_Order_Level', 'Pre_Shift_Qty', 'Scrap_Item',
                                   'Scrap_Qty', 'Purchase_GL', 'Business_Associate']


# Item Master Technical Specification
class  Technical_Specification_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Technical_Specification_Model
        fields = ['id', 'Specification', 'Parameter']
        

# Item Master NPD
class  NPD_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  NPD_Model
        fields = ['id', 'NPD', 'CustomerName', 'NPD_Qty', 'NPD_Due_Date']   
  
        
# Item Master General Page Fields MainGroup
class  MainGroup_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  MainGroup_Model
        fields = ['id', 'Prefix', 'Sub_Group_Code', 'Sub_Group_Name', 'Inventory']
        

# Item Master General Page Fields UnitCode
class  UnitCode_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  UnitCode_Model
        fields = ['id', 'UnitName']

# Item Master General Page Fields TDC
class  TDC_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  TDC_Model
        fields = ['id', 'Prefix', 'Name']

# Item Master General Page Fields MetalType
class  MetalType_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  MetalType_Model
        fields = ['id', 'Prefix', 'MetalType', 'ItemSizeUnit']

# Item Master General Page Fields Item Group
class  Item_Group_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Item_Group_Item_Master_Model
        fields = ['id', 'MainGroupName', 'Prefix', 'GroupName']

# Item Master General Page Fields Store Location
class  Store_Location_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Store_Location_Item_Master_Model
        fields = ['id', 'EnterStoreName']
    
# Item Master General Page Fields Route
class  Route_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Route_Item_Master_Model
        fields = ['id', 'Prefix', 'Name']

# Item Master General Page Fields Parent FG Code
class  Parent_FG_Code_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Parent_FG_Code_Item_Master_Model
        fields = ['id', 'Parent_FG_Code']

# Item Master General Page Fields Sector
class  Sector_Item_Master_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Sector_Item_Master_Model
        fields = ['id', 'Sector_Prefix', 'Sector_Name']

# Item Master General Page Fields Item Section
class  Item_Section_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Item_Section_Item_Master_Model
        fields = ['id', 'Prefix', 'Section_Name']

# Item Master General Page Fields Type/Grade New
class  Type_Grade_New_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Type_Grade_New_Model
        fields = ['id', 'SubGroup', 'Prefix', 'Item_Grade_Name', 'Colour_Code']

# Item Master General Page Fields Sub Group
class  Sub_Group_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Sub_Group_Item_Master_Model
        fields = ['id', 'Main_Group', 'Sub_Group', 'Prefix', 'Name']

# Item Master Data2 Page Fields Qty_Packing
class  Qty_Packing_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Qty_Packing_Model
        fields = ['id', 'EnterUnit_Name']

# Item Masters:- Fetch Item List
class ItemMaster_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMaster
        fields = ['id', 'SE_Item', 'Name_Description', 'Part_Code', 'Item_Size', 'Main_Group', 'Item_Group', 
                  'Store_Location', 'Unit_Code', 'HSN_SAC_Code']




# Supplier_Customer_Masters serializers
class  Supplier_Customer_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Supplier_Customer
        fields = ['id', 'Type', 'Name', 'Address_Line_1', 'Region', 'PAN_Type','PAN_NO',
                   'State_Code', 'GST_Tax_Code', 'Email_Id', 'Contact_No', 'TCS', 'Insurance_Policy_No',
                    'Subcon_Challan', 'GL', 'Code_No', 'Payment_Term', 'Country', 'Currency', 'Pin_Code',
                    'City', 'TDS_Rate', 'GST_No', 'GST_No2', 'Invoice_Type', 'CIN_No', 'Website',
                    'Incoterms', 'Insurance_Policy_Expiry_Date', 'VAT_TIN', 'Montly_Sale',
                    'Sector', 'Group', 'Distance', 'Vendor_Code', 'Legal_Name_GST',
                    'Cust_Short_Name', 'MSME_Type', 'MSME_No', 'LUT_No', 'ISO', 'QMSC_Code', 'QMSC_Date', 'Active',
                    'Std_Packing', 'Old_ERP_Code', 'Delivery_Lead_Time', 'EORI_No', 'Montly_Purchase', 'Discount_Per'
]


#Supplier_Customer_Buyer serializers
class  Buyer_Contact_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Buyer_Contact
        fields = ['id', 'Person_Name', 'Contact_No', 'Email', 'Department', 'Designation', 'Birth_Date']


 #Supplier_Customer_Bank serializers
class  Bank_Details_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Bank_Details                                                                                                                                                                                                                                                                                                                                                                                                   
        fields = ['id', 'Account_Holder_name', 'Bank_Name', 'Branch_Name', 'Bank_Account', 'IFSC_Code']


# Supplier Masters Type:- Customer,Supplier,JobWork,CSJW
from rest_framework import serializers
from .models import Customer, Supplier,JobWork,CSJW

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'code']

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'code']


class JobWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobWork
        fields = ['id', 'name', 'code']

class CSJWSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSJW
        fields = ['id', 'name', 'code']


# Supplier_Customer_Masters_General Type_Field_API
class  Type_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Type_Model                                                                                                                                                                                                                                                                                                                                                                                                   
        fields = ['id', 'Prefix', 'Category_Name']


# Supplier_Customer_Masters_General Region_Field_API
class  Region_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Region_Model                                                                                                                                                                                                                                                                                                                                                                                                  
        fields = ['id', 'RegionCode', 'RegionName']

# Supplier_Customer_Masters_General State_Field_API
class StateUTSerializer(serializers.Serializer):
    name = serializers.CharField()
    code = serializers.CharField()


# Fetch_Region
class Fetch_Region_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Region_Model
        fields = ['RegionName']


# Supplier_Customer_Masters_General StateCode_Field_API
class  StateCode_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  StateCode_Model                                                                                                                                                                                                                                                                                                                                                                                                  
        fields = ['id', 'StateName', 'State_No_Numeric', 'State_Code_Alpha']

# Supplier_Customer_Masters_General Payment_Term_Field_API
class  PaymentTerm_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  PaymentTerm_Model                                                                                                                                                                                                                                                                                                                                                                                                  
        fields = ['id', 'Days']

# Supplier_Customer_Masters_General Country_Field_API
class  Country_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Country_Model                                                                                                                                                                                                                                                                                                                                                                                                  
        fields = ['id', 'Code', 'Country']

# Supplier Genral Page Country
class CountrySerializer(serializers.Serializer):
    name = serializers.CharField()

# Supplier_Customer_Masters_General Currency_Field_API
class  Currency_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Currency_Model                                                                                                                                                                                                                                                                                                                                                                                                  
        fields = ['id', 'Code', 'Symbol', 'Description']


# Supplier Genral Page Currency
class CurrencySerializer(serializers.Serializer):
    code = serializers.CharField(max_length=3)


# Supplier_Customer_Masters_General City_Field_API
class  City_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  City_Model                                                                                                                                                                                                                                                                                                                                                                                                  
        fields = ['id', 'CityName']

# Supplier_Customer_Masters_General Sector_Field_API
class  Sector_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Sector_Model                                                                                                                                                                                                                                                                                                                                                                                                 
        fields = ['id', 'Sector_Prefix', 'SectorName']

# Supplier_Customer_Masters_General Group_Field_API
class  Group_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Group_Model                                                                                                                                                                                                                                                                                                                                                                                                 
        fields = ['id', 'Prefix', 'Group']

# Supplier_Customer_Masters_General QMSC_Code_Field_API
class  QMSC_Code_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  QMSC_Code_Model                                                                                                                                                                                                                                                                                                                                                                                                
        fields = ['id', 'QMSC_Code', 'QMSC_Code_Desc']

# Supplier_Customer_Masters:- Fetch Supplier List
class Supplier_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier_Customer
        fields = ['id', 'Type', 'Code_No', 'Name', 'Contact_No', 'Email_Id', 'Vendor_Code', 'Payment_Term',
                   'GST_No', 'GST_No2', 'GST_Tax_Code']
        

# Supplier_Customer_Masters:- State, CodeNo, City
# serializers.py

from rest_framework import serializers

class StateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=2)
    gst_code = serializers.CharField(max_length=10)
    cities = serializers.ListField(child=serializers.CharField(max_length=100))

class CitySerializer(serializers.Serializer):
    city = serializers.CharField(max_length=100)

class StateCitySerializer(serializers.Serializer):
    state = StateSerializer()
    cities = serializers.ListField(child=CitySerializer())




# Supplier Master Type:- Customer, Supplier, JobWork, CSJW
from rest_framework import serializers
from .models import SupplierType, CustomerType, JobworkType, CSJWType

class SupplierTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierType
        fields = ['id', 'name', 'code']

class CustomerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerType
        fields = ['id', 'name', 'code']

class JobworkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobworkType
        fields = ['id', 'name', 'code']

class CSJWTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSJWType
        fields = ['id', 'name', 'code']



# Cross Reference: Item Cross Reference
class  Item_Cross_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Item_Cross_Model                                                                                                                                                                                                                                                                                                                                                                                                
        fields = ['id', 'ItemName', 'Cust_Supp_Name', 'Cross_Ref_Item_No', 'Cross_Ref_Item_Desc', 'Remark',
                   'Model', 'ModelNo', 'DrawingNo', 'RevNo', 'Min_Order_Qty', 'Packing_Qty']

# Cross Reference: Supplier Item 
class  Supplier_Item_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Supplier_Item_Model                                                                                                                                                                                                                                                                                                                                                                                          
        fields = ['id', 'Cust_Supp_Name', 'Main_Group', 'ItemName', 'Rate']

# Cross Reference: Customer_Item_VA_Rate
class  Item_VA_Rate_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Item_VA_Rate_Model                                                                                                                                                                                                                                                                                                                                                                                         
        fields = ['id', 'Cust_Supp_Name', 'ItemName', 'VARate1', 'VARate2']


# Cross Reference: Supplier Name Fetch
class Cross_Ref_Supplier_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier_Customer
        fields = ['id', 'Name', 'Code_No']


# Item Cross Reference:- Fetch Item
class Item_Cross_Item_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMaster
        fields = ['id', 'SE_Item', 'Name_Description']

# Item Master UnitCode HardCoded
class UnitCodeHardCodedSerializer(serializers.Serializer):
    name = serializers.CharField()


# New Work Center Master: Add New
class  Work_Center_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Work_Center_Model                                                                                                                                                                                                                                                                                                                                                                                        
        fields = ['id', 'Plant', 'Category', 'WorkCenterCode', 'WorkCenterName', 'WorkCenterType',
                   'Mhr_Rate', 'Electricity', 'PPM_SPM', 'PPM', 'BatchQty', 'Oil', 'Proud_Hours',
                     'Daily_Running_Hr', 'Operator']

# New Work Center Master: Machine Group Work Center Type Group
class  Machine_Group_Work_Center_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Machine_Work_Center_Group_Model                                                                                                                                                                                                                                                                                                                                                                                       
        fields = ['id', 'EnterType']


# New Work Center Master: Work Center Type Group
class  WorkCenterTypeGroup_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  WorkCenterTypeGroup_Model                                                                                                                                                                                                                                                                                                                                                                                         
        fields = ['id', 'TypeGroup', 'Prod_Wt']

# Cycle Time Master
class  Cycle_Time_Master_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Cycle_Time_Master_Model                                                                                                                                                                                                                                                                                                                                                                                         
        fields = ['id', 'Plant', 'PartCode', 'MachineType', 'Machine', 'OPTime', 'Load_Unload_Time', 'MO_Time', 'Total_Time', 'Time_in_Minutes']

# Shift Master
class  Shift_Master_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Shift_Master_Model                                                                                                                                                                                                                                                                                                                                                                                        
        fields = ['id', 'Plant', 'Shift_Name', 'Shift_Prefix', 'Shift_From', 'Shift_Till', 'Break_Name', 'Break_Till', 'Break_Time', 'Total_Hours']


# Add_New_Operator_Supervisor_Master
class  Add_New_Operator_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Add_New_Operator_Model                                                                                                                                                                                                                                                                                                                                                                                     
        fields = ['id', 'Department', 'Name', 'Address', 'Contact_No', 'Birth_Date', 'Salary', 
                  'Date_Of_Leaving', 'Aadhar_No', 'Code', 'Designation', 'CorrespondingAddress',
                    'Type', 'Joining_Sal_Date', 'Contractor', 'DailyWorkHours', 'PanNo', 'BankName',
                      'BankAccountNo', 'BankIFSC_Code']
        
# Add_New_Operator_Supervisor_Master: Department_Master
class  Department_Master_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Department_Master_Model                                                                                                                                                                                                                                                                                                                                                                                    
        fields = ['id', 'SelectCategory', 'EnterDeptName']

# Add_New_Operator_Supervisor_Master: Department_Category_Master
class  Department_Category_Master_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Department_Category_Master_Model                                                                                                                                                                                                                                                                                                                                                                                    
        fields = ['id', 'CategoryName']

# Add_New_Operator_Supervisor_Master: Designation Api Field
class  Designation_Api_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Designation_Api_Model                                                                                                                                                                                                                                                                                                                                                                                   
        fields = ['id', 'EnterType']

# Add_New_Operator_Supervisor_Master: Contractor Api Field
class  Contractor_Api_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Contractor_Api_Model                                                                                                                                                                                                                                                                                                                                                                                  
        fields = ['id', 'Plant', 'ContractorName', 'ContactNo', 'GstNo', 'NatureOfService', 'Email', 
                  'RefCode', 'Address', 'PanNo', 'Tds', 'FirName']
        

# Unit Conversion Master
class  Unit_Conversion_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Unit_Conversion_Model                                                                                                                                                                                                                                                                                                                                                                                
        fields = ['id', 'SubGroup', 'Item', 'Unit', 'StockQty', 'StockUnit']


# Contractor Master
class  ContractorMaster_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Contractor_Master_Model                                                                                                                                                                                                                                                                                                                                                                                 
        fields = ['id', 'Plant', 'ContractorName', 'ContactNo', 'GstNo', 'NatureOfService', 'Email', 
                  'RefCode', 'Address', 'PanNo', 'Tds', 'FirName']
        

# Cost Center Master
class  Cost_Center_Master_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Cost_Center_Model                                                                                                                                                                                                                                                                                                                                                                                
        fields = ['id', 'Category_Code', 'Cost_Center_Code', 'Cost_Center_Desc']

# Cost Center Master Add New
class  Cost_Center_Master_Add_New_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Cost_Center_Master_Add_New_Model                                                                                                                                                                                                                                                                                                                                                                              
        fields = ['id', 'Category_Code', 'Cost_Center_Desc']


# Price List: Price List Master - Add Price List
class  Add_Price_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Add_Price_List_Model                                                                                                                                                                                                                                                                                                                                                                            
        fields = ['id', 'Select_Customer', 'Select_Address', 'Price_List_Code', 'Price_List_Name', 'Effective_From_Date']

# Price List: Price List Entry
class  Price_List_Entry_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Price_List_Entry_Model                                                                                                                                                                                                                                                                                                                                                                           
        fields = ['id', 'Qty', 'Rate', 'Disk', 'Weff_Date', 'Po_No', 'Po_Date', 'Amd_No', 'Amd_Date', 'Po_Line_No', 'Po_Type', 'Cust_Eff_Date', 'Remark']

# Bom Routing Master: - Production Department Master
class  Production_Department_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Production_Department_Model                                                                                                                                                                                                                                                                                                                                                                              
        fields = ['id', 'Department_Name', 'Short_Name']

# Bom Routing Master: - Operation Master
class  Operation_Master_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Operation_Master_Model                                                                                                                                                                                                                                                                                                                                                                              
        fields = ['id', 'Std_Otp', 'Operation_Name', 'Prefix', 'Mhr_Rate', 'BomQc', 
                  'ProductionDept', 'MachineType', 'Production_Cycle_Time', 'Stop_Mc_Booking', 
                  'Per_Day_Prod_Qty']
        
# Bom Routing Master: - Std Routing
class  Std_Routing_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Std_Routing_Model                                                                                                                                                                                                                                                                                                                                                                              
        fields = ['id', 'Std_Routing_No', 'Op_No', 'Op_Name', 'Part_Type', 'Wip_Wt', 'Op_Type', 'QC',
                   'Ass_Prod', 'Part_Code']
        
# Bom Routing Master: - Bom Item Group Details
class  Bom_Item_Group_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Bom_Item_Group_Model                                                                                                                                                                                                                                                                                                                                                                             
        fields = ['id', 'Bom_Item_Group', 'Item', 'Qty']



# Item Main Group Api
from rest_framework import serializers
from .models import Tool

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ['id', 'name', 'code']
        read_only_fields = ['code']  # Make the code field read-only



########GST NUMBER
from rest_framework import serializers
from .models import GSTNumber

class GSTNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = GSTNumber
        fields = ['gst_number']



# Supplier Sub Module
from rest_framework import serializers
from .models import Item, Buyer_Contact, Bank_Details

class BuyerContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer_Contact
        fields = ["Person_Name", "Contact_No", "Email", "Department", "Designation", "Birth_Date"]

class BankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank_Details
        fields = ["Account_Holder_name", "Bank_Name", "Branch_Name", "Bank_Account", "IFSC_Code"]

class ItemSerializer(serializers.ModelSerializer):
    buyer_contacts = BuyerContactSerializer(many=True, required=False)
    bank_details = BankDetailsSerializer(many=True, required=False)

    class Meta:
        model = Item
        fields = '__all__'

    def create(self, validated_data):
        buyer_contacts_data = validated_data.pop('buyer_contacts', [])
        bank_details_data = validated_data.pop('bank_details', [])
        item = Item.objects.create(**validated_data)

        for contact_data in buyer_contacts_data:
            Buyer_Contact.objects.create(item=item, **contact_data)

        for bank_data in bank_details_data:
            Bank_Details.objects.create(item=item, **bank_data)

        return item

    def update(self, instance, validated_data):
        buyer_contacts_data = validated_data.pop('buyer_contacts', None)
        bank_details_data = validated_data.pop('bank_details', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if buyer_contacts_data is not None:
            instance.buyer_contacts.all().delete()
            for contact_data in buyer_contacts_data:
                Buyer_Contact.objects.create(item=instance, **contact_data)

        if bank_details_data is not None:
            instance.bank_details.all().delete()
            for bank_data in bank_details_data:
                Bank_Details.objects.create(item=instance, **bank_data)

        return instance


#######################sup

# This is for GET APIs that fetch limited fields for PDF/view
class ItemPDFSerializer(serializers.ModelSerializer):
    buyer_contacts = BuyerContactSerializer(many=True, read_only=True)
    bank_details = BankDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = [
            'number', 'Payment_Term', 'Name', 'Address_Line_1', 'City', 'Country', 'Contact_No',
            'Currency', 'Email_Id', 'Pin_Code', 'State_Code', 'Vendor_Code', 'GST_No', 'GST_No2',
            'GST_Tax_Code', 'Invoice_Type', 'TCS', 'VAT_TIN', 'EORI_No',
            'buyer_contacts', 'bank_details'
        ]



from rest_framework import serializers
from .models import BOMItem

class BOMItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOMItem
        fields = '__all__'







#BOM: Item Part Master
from .models import BOM_ItemPartMaster
class BOM_ItemPartMaster_Serializer(serializers.ModelSerializer):
    class Meta:
        model = BOM_ItemPartMaster
        fields = '__all__'
        read_only_fields = ['item']

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartCode
        fields = ['name', 'prefix', 'part_code']

from rest_framework import serializers
from .models import Operation_Master_Model

class OperationMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation_Master_Model
        fields = ['Operation_Name', 'Prefix']



# Item Master
from rest_framework import serializers
from .models import ItemTable, Item_Master_Data2_Model, Technical_Specification_Model, NPD_Model

class ItemMasterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Master_Data2_Model
        exclude = ['item']

class TechnicalSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technical_Specification_Model
        exclude = ['item']

class NPDSerializer(serializers.ModelSerializer):
    class Meta:
        model = NPD_Model
        exclude = ['item']

class ItemTableSerializer(serializers.ModelSerializer):
    item_master_data = ItemMasterDataSerializer(required=False)
    technical_specifications = TechnicalSpecificationSerializer(many=True, required=False)
    npd_details = NPDSerializer(many=True, required=False)

    class Meta:
        model = ItemTable
        fields = '__all__'

    def create(self, validated_data):
        master_data = validated_data.pop('item_master_data', None)
        specs_data = validated_data.pop('technical_specifications', [])
        npd_data = validated_data.pop('npd_details', [])

        item = ItemTable.objects.create(**validated_data)

        if master_data:
            Item_Master_Data2_Model.objects.create(item=item, **master_data)

        for spec in specs_data:
            Technical_Specification_Model.objects.create(item=item, **spec)

        for npd in npd_data:
            NPD_Model.objects.create(item=item, **npd)

        return item

    def update(self, instance, validated_data):
        master_data = validated_data.pop('item_master_data', None)
        specs_data = validated_data.pop('technical_specifications', None)
        npd_data = validated_data.pop('npd_details', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if master_data is not None:
            Item_Master_Data2_Model.objects.update_or_create(item=instance, defaults=master_data)

        if specs_data is not None:
            instance.technical_specifications.all().delete()
            for spec in specs_data:
                Technical_Specification_Model.objects.create(item=instance, **spec)

        if npd_data is not None:
            instance.npd_details.all().delete()
            for npd in npd_data:
                NPD_Model.objects.create(item=instance, **npd)

        return instance


############################ Code For All_Masters
from rest_framework import serializers
from .models import MainGroup2, ItemGroup2

class MainGroupSerializer2(serializers.ModelSerializer):
    class Meta:
        model = MainGroup2
        fields = '__all__'


class ItemGroupSerializer2(serializers.ModelSerializer):
    class Meta:
        model = ItemGroup2
        fields = '__all__'

from All_Masters.models import ItemTable as ItemTable2
class ItemTableSerializer2(serializers.ModelSerializer):
    class Meta:
        model = ItemTable2
        fields = '__all__'


############################### BOM


from rest_framework import serializers
from .models import BOMItem

class BOMItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOMItem
        fields = ['id', 'OPNo', 'PartCode', 'BOMPartType', 'BomPartCode', 'QtyKg', 'ScrapCode', 'ScracpQty', 'QC', 'AssProd']


class ItemBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTable
        fields = [
            'id',
            'part_no',
            'Part_Code',
            'Name_Description',
            'main_group',
            'item_group'
        ]

class BOMItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOMItem
        fields = '__all__'


class ItemWithBOMSerializer(serializers.ModelSerializer):
    boms = BOMItemSerializer(many=True, read_only=True)

    class Meta:
        model = ItemTable
        fields = [
            'id',
            'part_no',
            'Part_Code',
            'Name_Description',
            'main_group',
            'item_group',
            'boms'
        ]


from rest_framework import serializers
from .models import ItemTable, BOMItem

# All_Masters/serializers.py


from .models import BOMItem, ItemTable


from rest_framework import serializers
from .models import BOMItem, ItemTable

class BOMItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BOMItem
        fields = [
            'id',
            'item',
            'OPNo',
            'PartCode',
            'Operation',
            'BOMPartType',
            'BomPartCode',
            'QtyKg',
            'ScrapCode',
            'ScracpQty',
            'QC',
            'ProdQty',
            'AssProd',
            'WipWt',
            'WipRate',
            'PieceRate',
            'OPRate',
            'BomPartDesc',
        ]
    

class ItemSearchSerializer2(serializers.ModelSerializer):
    bom_items = serializers.SerializerMethodField()

    class Meta:
        model = ItemTable
        fields = ['id', 'part_no', 'Part_Code', 'Name_Description', 'bom_items']

    def get_bom_items(self, obj):
        if obj.main_group in ['RM', 'FG']:
            bom_items = obj.bom_items.all()
            return BOMItemSerializer(bom_items, many=True).data
        return None

#Bom Routing & Bill of Material(BOM):- Fetch Scrap Code

from rest_framework import serializers
from .models import ItemTable

class ItemTableSerializer3(serializers.ModelSerializer):
    class Meta:
        model = ItemTable
        fields = ['Name_Description', 'part_no']  # Only include the Name_Description field




# Item Search Api With BOM
class ItemSearchSerializer5(serializers.ModelSerializer):
    bom_items = serializers.SerializerMethodField()

    class Meta:
        model = ItemTable
        fields = ['id', 'part_no', 'Part_Code', 'Name_Description', 'Rate', 'Item_Size', 'HSN_SAC_Code', 'Unit_Code', 'bom_items']

    def get_bom_items(self, obj):
        if obj.main_group in ['RM', 'FG']:
            bom_items = obj.bom_items.all()
            return BOMItemSerializer(bom_items, many=True).data
        return None

# RM Search Api
from rest_framework import serializers
from .models import ItemTable

class RMItemTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTable
        fields = ['id', 'part_no', 'Part_Code', 'Name_Description']


from rest_framework import serializers
from .models import BOM_ItemPartMaster

class BOMDropdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOM_ItemPartMaster
        fields = ['Operation', 'PartCode']



# serializers.py
from rest_framework import serializers
from .models import BOMItem

class BOMItemSerializer5(serializers.ModelSerializer):
    PartCode = serializers.SerializerMethodField()
    BomPartCode = serializers.SerializerMethodField()

    class Meta:
        model = BOMItem
        fields = [
            'OPNo', 'PartCode', 'BOMPartType', 'BomPartCode', 'QtyKg',
            'ScrapCode', 'ScracpQty', 'QC', 'ProdQty', 'AssProd',
            'WipWt', 'WipRate', 'PieceRate', 'OPRate'
        ]

    def get_PartCode(self, obj):
        return f"{self.context.get('Operation', '')} | {obj.PartCode}"

    def get_BomPartCode(self, obj):
        return f"{obj.BomPartCode} | {obj.PartCode} | Steel part"
    
