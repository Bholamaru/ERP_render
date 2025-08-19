from django.db import models
from django.contrib.auth.models import User 

class ScrapRejection(models.Model):
    series = models.CharField(max_length=255, blank=True, null=True)
    transaction_type = models.CharField(max_length=255, blank=True, null=True)
    scrap_rejection_no = models.CharField(max_length=100, unique=True)
    scrap_rejection_date = models.CharField(max_length=255, blank=True, null=True)
    item_no_code = models.CharField(max_length=255, blank=True, null=True)
    heat_no_stock = models.CharField(max_length=255, blank=True, null=True)
    scrap_rejection_qty = models.CharField(max_length=255, blank=True, null=True)
    scrap_rejection_remark = models.CharField(max_length=255, blank=True, null=True)
    reject_reason = models.CharField(max_length=255, blank=True, null=True)
    cust_supp = models.CharField(max_length=255, blank=True, null=True)
    scrap_rej_item = models.CharField(max_length=255, blank=True, null=True)
    scrap_qty = models.CharField(max_length=255, blank=True, null=True)


    @staticmethod
    def generate_next_scrap_rejection_no(shortyear):
        """
        Generate the next scrap rejection number based on the Shortyear.
        Example: Line R 272800001, Line R 272800002, ...
        """
        # Ensure that shortyear is 4 digits, like '2728' from '2028'
        prefix = f"Line R {shortyear}"

        # Get the latest scrap rejection number for the current shortyear
        latest_rejection = ScrapRejection.objects.filter(scrap_rejection_no__startswith=prefix).order_by('-scrap_rejection_no').first()

        if latest_rejection:
            # Extract the last 6 digits (sequential number) and increment it
            latest_number = int(latest_rejection.scrap_rejection_no[-5:])
            next_number = latest_number + 1
        else:
            # If no existing rejection, start from 000001
            next_number = 1
        
        # Format the next number as a 6-digit number
        next_scrap_rejection_no = f"{prefix}{next_number:05d}"
        return next_scrap_rejection_no

    def __str__(self):
        return self.scrap_rejection_no


# Production Entry
class MachineIdleTime(models.Model):
    idle_reason = models.CharField(max_length=255, blank=True, null=True)
    from_time = models.CharField(max_length=255, blank=True, null=True)
    to_time = models.CharField(max_length=255, blank=True, null=True)
    total_time = models.CharField(max_length=255, blank=True, null=True)
    supervisor_operator = models.CharField(max_length=255, blank=True, null=True)
    setting_part = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.Item} - {self.Item}"


from django.db import models
from All_Masters.models import BOMItem
class ProductionEntry(models.Model):
    MachineIdleTime_Detail_Enter = models.ManyToManyField(MachineIdleTime, related_name='ItemDetail_orders', blank=True)
    # bom_item = models.ForeignKey(BOMItem, related_name='item', on_delete=models.CASCADE)
    Series = models.CharField(max_length=255, blank=True, null=True)
    General = models.CharField(max_length=255, blank=True, null=True)
    MachineDowntime = models.CharField(max_length=255, blank=True, null=True)
    Prod_no = models.CharField(max_length=255, blank=True, null=True)
    contractor = models.CharField(max_length=255, blank=True, null=True)
    unit_machine = models.CharField(max_length=255, blank=True, null=True)
    item = models.CharField(max_length=255, blank=True, null=True)
    operation = models.CharField(max_length=255, blank=True, null=True)
    prod_qty = models.CharField(max_length=255, blank=True, null=True)
    Date = models.CharField(max_length=255, blank=True, null=True)
    Time = models.CharField(max_length=255, blank=True, null=True)
    Supervisor = models.CharField(max_length=255, blank=True, null=True)
    machine_speed = models.CharField(max_length=255, blank=True, null=True)
    Helper = models.CharField(max_length=255, blank=True, null=True)
    ParentOperation = models.CharField(max_length=255, blank=True, null=True)
    ProdTime = models.CharField(max_length=255, blank=True, null=True)
    shift = models.CharField(max_length=255, blank=True, null=True)
    operator = models.CharField(max_length=255, blank=True, null=True)
    lot_no = models.CharField(max_length=255, blank=True, null=True)
    rework_qty = models.CharField(max_length=255, blank=True, null=True)
    reject_qty = models.CharField(max_length=255, blank=True, null=True) 

    raw_material=models.CharField(max_length=255, blank=True, null=True) 

    shift_from = models.CharField(max_length=255, blank=True, null=True)
    shift_to = models.CharField(max_length=255, blank=True, null=True)
    break_from = models.CharField(max_length=255, blank=True, null=True)
    break_to = models.CharField(max_length=255, blank=True, null=True)
    break_total = models.CharField(max_length=255, blank=True, null=True)
    shift_time = models.CharField(max_length=255, blank=True, null=True)
    prod_time = models.CharField(max_length=255, blank=True, null=True)
    avail_time = models.CharField(max_length=255, blank=True, null=True)
    cycle_time = models.CharField(max_length=255, blank=True, null=True)
    op_time = models.CharField(max_length=255, blank=True, null=True)
    lu_time = models.CharField(max_length=255, blank=True, null=True)
    mo_time = models.CharField(max_length=255, blank=True, null=True)
    total_time = models.CharField(max_length=255, blank=True, null=True)

    electricity_start_unit = models.CharField(max_length=255, blank=True, null=True)
    electricity_end_unit = models.CharField(max_length=255, blank=True, null=True)
    electricity_total_unit = models.CharField(max_length=255, blank=True, null=True)
    scrap_end_piece_qty = models.CharField(max_length=255, blank=True, null=True)
    scrap_qty = models.CharField(max_length=255, blank=True, null=True)
    scrap_end_remark = models.CharField(max_length=255, blank=True, null=True)

    mill_name = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    target_qty = models.CharField(max_length=255, blank=True, null=True)
    production_hours = models.CharField(max_length=255, blank=True, null=True)
    idle_hours = models.CharField(max_length=255, blank=True, null=True)
    actual_hours = models.CharField(max_length=255, blank=True, null=True)

    Rework_Description = models.CharField(max_length=255, blank=True, null=True)
    ReworkQty = models.CharField(max_length=255, blank=True, null=True)
    Reject_Description = models.CharField(max_length=255, blank=True, null=True)
    Reject_Quantity = models.CharField(max_length=255, blank=True, null=True)
    
    ItemCode = models.CharField(max_length=255, blank=True, null=True)
    ItemDescription = models.CharField(max_length=255, blank=True, null=True)


    @classmethod
    def generate_prod_no(cls, series, year):
        if series != 'DP':
            raise ValueError("Invalid series. Only 'DP' is supported.")
    
        # Find the last entry for the specific year and series
        last_prod = cls.objects.filter(Series=series, Prod_no__startswith=f"DP {year}").order_by('-Prod_no').first()
    
        # If there are no previous entries, start from 1
        if last_prod:
            # Extract the numeric part after the year (the last part after "DP <year>")
            last_number = last_prod.Prod_no[len(f"DP {year}"):].strip()  # Get the part after "DP <year>"
            try:
                # Increment the number and ensure it is a valid integer
                new_number = int(last_number) + 1
            except ValueError:
                raise ValueError(f"Invalid Prod_no format: {last_number}")
        else:
            # Start from 1 if no previous entries
            new_number = 1
    
        # Format the new product number with zero padding to ensure it has 3 digits
        new_prod_no = f"DP {year}{str(new_number).zfill(5)}"
        return new_prod_no


# Rework Production Entry 2
class MachineIdleTime2(models.Model):
    idle_reason = models.CharField(max_length=255, blank=True, null=True)
    from_time = models.CharField(max_length=255, blank=True, null=True)
    to_time = models.CharField(max_length=255, blank=True, null=True)
    total_time = models.CharField(max_length=255, blank=True, null=True)
    supervisor_operator = models.CharField(max_length=255, blank=True, null=True)
    setting_part = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.Item} - {self.Item}"


# from django.db import models

class ProductionEntry2(models.Model):
    MachineIdleTime_Detail_Enter = models.ManyToManyField(MachineIdleTime2, related_name='ItemDetail_orders', blank=True)
    ReworkNo = models.CharField(max_length=255, blank=True, null=True)
    ReworkDate = models.CharField(max_length=255, blank=True, null=True)
    Reworktime = models.CharField(max_length=255, blank=True, null=True)
    shift = models.CharField(max_length=255, blank=True, null=True)
    contractor = models.CharField(max_length=255, blank=True, null=True)
    Supervisor = models.CharField(max_length=255, blank=True, null=True)
    operator = models.CharField(max_length=255, blank=True, null=True)
    ItemCode = models.CharField(max_length=255, blank=True, null=True)
    PartCode = models.CharField(max_length=255, blank=True, null=True)
    HeatNo = models.CharField(max_length=255, blank=True, null=True)
    unit_machine = models.CharField(max_length=255, blank=True, null=True)
    ProdTime = models.CharField(max_length=255, blank=True, null=True)
    ReworktoOk = models.CharField(max_length=255, blank=True, null=True)
   
    ProductionHours = models.CharField(max_length=255, blank=True, null=True)
    IdleHours = models.CharField(max_length=255, blank=True, null=True)
    ActualHours = models.CharField(max_length=255, blank=True, null=True)
    shift_from = models.CharField(max_length=255, blank=True, null=True)
    shift_till = models.CharField(max_length=255, blank=True, null=True)
    break_from = models.CharField(max_length=255, blank=True, null=True)
    break_till = models.CharField(max_length=255, blank=True, null=True)
    total = models.CharField(max_length=255, blank=True, null=True)
    op_time = models.CharField(max_length=255, blank=True, null=True)
    lu_time = models.CharField(max_length=255, blank=True, null=True)
    mo_time = models.CharField(max_length=255, blank=True, null=True)
    total_time = models.CharField(max_length=255, blank=True, null=True)
    target_qty = models.CharField(max_length=255, blank=True, null=True)
    target_qty_hours = models.CharField(max_length=255, blank=True, null=True)
    ReasonForRework = models.CharField(max_length=255, blank=True, null=True)
   

    @classmethod
    def generate_next_rework_no(cls, year):
        # Ensure the year is in the correct format
        year_str = str(year)
        if len(year_str) != 4:
            raise ValueError("Year must be in 4-digit format (e.g., 2324).")
        
        # Find the last entry for the specific year
        last_rework = cls.objects.filter(ReworkNo__startswith=f"{year_str}").order_by('-ReworkNo').first()
        
        # If there are no previous entries, start from 1
        if last_rework:
            # Extract the numeric part after the year (the last part after "<year>")
            last_number = last_rework.ReworkNo[len(year_str):].strip()  # Get the part after the year
            try:
                # Increment the number and ensure it is a valid integer
                new_number = int(last_number) + 1
            except ValueError:
                raise ValueError(f"Invalid ReworkNo format: {last_number}")
        else:
            # Start from 1 if no previous entries
            new_number = 1

        # Format the new rework number with zero padding to ensure it has 5 digits
        new_rework_no = f"{year_str}{str(new_number).zfill(5)}"
        return new_rework_no
    

#Rework Production: Rework production Entry

from django.db import models

class ProductDetail2(models.Model):
    # Removed old fields and added new ones
    Plant = models.CharField(max_length=255, blank=True, null=True)
    series = models.CharField(max_length=255, blank=True, null=True)
    rework_no = models.CharField(max_length=100, blank=True, null=True)
    rework_date = models.CharField(max_length=100, blank=True, null=True)
    rework_time = models.CharField(max_length=100, blank=True, null=True)
    machine = models.CharField(max_length=100, blank=True, null=True)
    work_order = models.CharField(max_length=100, blank=True, null=True)
    item_code = models.CharField(max_length=100, blank=True, null=True)
    part_code = models.CharField(max_length=100, blank=True, null=True)
    heat_code = models.CharField(max_length=100, blank=True, null=True)
    rework_to_ok_qty = models.CharField(max_length=100, blank=True, null=True)
    reject_to_ok_qty = models.CharField(max_length=100, blank=True, null=True)
    change_fg = models.CharField(max_length=100, blank=True, null=True)
    part_code2 = models.CharField(max_length=100, blank=True, null=True)
    heat_code2 = models.CharField(max_length=100, blank=True, null=True)
    reason_for_rework = models.CharField(max_length=100, blank=True, null=True)
    quality_remark = models.CharField(max_length=100, blank=True, null=True)
    operator = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.item_code


class Item2(models.Model):
    # Removed old fields and added new ones
    product_detail = models.ForeignKey(ProductDetail2, related_name='items', on_delete=models.CASCADE)
    item_desc = models.CharField(max_length=255, blank=True, null=True)
    heat_code = models.CharField(max_length=255, blank=True, null=True)
    rework_to_ok_qty = models.CharField(max_length=255, blank=True, null=True)
    reject_to_ok_qty = models.CharField(max_length=255, blank=True, null=True)
    rework_to_reject_qty = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.item_desc


class ConsumptionDetails(models.Model):
    product_detail = models.ForeignKey(ProductDetail2, related_name='consumption_details', on_delete=models.CASCADE)
    item_desc = models.CharField(max_length=255, blank=True, null=True)
    heat_code = models.CharField(max_length=255, blank=True, null=True)
    qty = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.item_desc



# Production Entry Assembly:-

class AssemblyProductionDetails(models.Model):  
    Plant = models.CharField(max_length=255, blank=True, null=True)
    series = models.CharField(max_length=255, blank=True, null=True)
    General = models.CharField(max_length=255, blank=True, null=True)
    Prod_no = models.CharField(max_length=255, blank=True, null=True)
    Date = models.CharField(max_length=255, blank=True, null=True)
    Time = models.CharField(max_length=255, blank=True, null=True)
    shift = models.CharField(max_length=255, blank=True, null=True)
    contractor = models.CharField(max_length=255, blank=True, null=True)
    Supervisor = models.CharField(max_length=255, blank=True, null=True)
    operator = models.CharField(max_length=255, blank=True, null=True)
    unit_machine = models.CharField(max_length=255, blank=True, null=True)
    Helper = models.CharField(max_length=255, blank=True, null=True)
    FGItem = models.CharField(max_length=255, blank=True, null=True)
    operation = models.CharField(max_length=255, blank=True, null=True)
    BOM = models.CharField(max_length=255, blank=True, null=True)
    Heat_Lot_No = models.CharField(max_length=255, blank=True, null=True)
    ProdQty = models.CharField(max_length=255, blank=True, null=True)
    ProdTime = models.CharField(max_length=255, blank=True, null=True)
    Rework_Qty = models.CharField(max_length=255, blank=True, null=True)
    Reject_Qty = models.CharField(max_length=255, blank=True, null=True)
    Change_Produced_Qty = models.CharField(max_length=255, blank=True, null=True)  

    ShiftFrom = models.CharField(max_length=255, blank=True, null=True)
    ShiftTo = models.CharField(max_length=255, blank=True, null=True)
    BreakFrom = models.CharField(max_length=255, blank=True, null=True)
    BreakTo = models.CharField(max_length=255, blank=True, null=True)
    BreakTotal = models.CharField(max_length=255, blank=True, null=True)
    shiftTime = models.CharField(max_length=255, blank=True, null=True)
    cycleTime = models.CharField(max_length=255, blank=True, null=True)
    OpTime = models.CharField(max_length=255, blank=True, null=True)
    LuTime = models.CharField(max_length=255, blank=True, null=True)
    MoTime = models.CharField(max_length=255, blank=True, null=True)
    TotalTime = models.CharField(max_length=255, blank=True, null=True)

    ScrapEndPieceCode = models.CharField(max_length=255, blank=True, null=True)
    ScrapEndPieceQty = models.CharField(max_length=255, blank=True, null=True)
    ScrapEndPieceRemark = models.CharField(max_length=255, blank=True, null=True)
    BomScrapCode = models.CharField(max_length=255, blank=True, null=True)
    BomScrapWt = models.CharField(max_length=255, blank=True, null=True)
    StdScracpQty = models.CharField(max_length=255, blank=True, null=True)

    Remark = models.CharField(max_length=255, blank=True, null=True)
    TargetQty = models.CharField(max_length=255, blank=True, null=True)
    Prod = models.CharField(max_length=255, blank=True, null=True)

    ProductionHours = models.CharField(max_length=255, blank=True, null=True)
    IdleHours = models.CharField(max_length=255, blank=True, null=True)
    ActualHours = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.Plant


class MachineIdleTimeAss(models.Model):  # Renamed Item2 to MachineIdleTimeAss
    product_detail = models.ForeignKey(AssemblyProductionDetails, related_name='MachineIdleTimeAss', on_delete=models.CASCADE)
    idle_reason = models.CharField(max_length=255, blank=True, null=True)
    from_time = models.CharField(max_length=255, blank=True, null=True)
    to_time = models.CharField(max_length=255, blank=True, null=True)
    total_time = models.CharField(max_length=255, blank=True, null=True)
    supervisor_operator = models.CharField(max_length=255, blank=True, null=True)
    setting_part = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.idle_reason


class ItemStockDetails(models.Model):  # Renamed ConsumptionDetails to ItemStockDetails
    product_detail = models.ForeignKey(AssemblyProductionDetails, related_name='ItemStockDetails', on_delete=models.CASCADE)
    Item_Group = models.CharField(max_length=255, blank=True, null=True)
    Alt_Item = models.CharField(max_length=255, blank=True, null=True)
    Item_No = models.CharField(max_length=255, blank=True, null=True)
    Item_Code = models.CharField(max_length=255, blank=True, null=True)
    Desc = models.CharField(max_length=255, blank=True, null=True)
    Bom_Qty = models.CharField(max_length=255, blank=True, null=True)
    Reg_Qty = models.CharField(max_length=255, blank=True, null=True)
    Stock = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.Item_Group 


class ReworkReason(models.Model):  # Renamed ConsumptionDetails to ItemStockDetails
    product_detail = models.ForeignKey(AssemblyProductionDetails, related_name='ReworkReason', on_delete=models.CASCADE)
    Description = models.CharField(max_length=255, blank=True, null=True)
    Qty = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.Description


class RejectReason(models.Model):  # Renamed ConsumptionDetails to ItemStockDetails
    product_detail = models.ForeignKey(AssemblyProductionDetails, related_name='RejectReason', on_delete=models.CASCADE)
    Description = models.CharField(max_length=255, blank=True, null=True)
    Qty = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.Description
    

class ReworkReason2(models.Model):  
    Description = models.CharField(max_length=255, blank=True, null=True)
    ParentCode = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.Description


class RejectReason2(models.Model):
    Description = models.CharField(max_length=255, blank=True, null=True)
    ParentCode = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.Description




# Contractor Production Entry

class ProductionRecord(models.Model):
    date = models.DateField()
    machine = models.CharField(max_length=100)
    shift = models.CharField(max_length=50)
    item_name = models.CharField(max_length=255)
    total_production_qty = models.IntegerField()
    total_production_hours = models.FloatField()
    total_breakdown_hours = models.FloatField()
    contractor_name = models.CharField(max_length=255)
    downtime_reason = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    job_no = models.CharField(max_length=100)
    item_rate = models.DecimalField(max_digits=10, decimal_places=2)
    shift_target_qty = models.IntegerField()
    machine_rate_per_hr = models.DecimalField(max_digits=10, decimal_places=2)
    prod_amt = models.DecimalField(max_digits=12, decimal_places=2)
    bd_amt = models.DecimalField(max_digits=12, decimal_places=2)
    efficiency = models.FloatField()

    def __str__(self):
        return f"{self.date} - {self.machine} - {self.item_name}"



# FG Scrap Rejection Note

from django.db import models

class FGScrapDetails(models.Model):  
    Plant = models.CharField(max_length=255, blank=True, null=True)
    Series = models.CharField(max_length=255, blank=True, null=True)
    NoteType = models.CharField(max_length=255, blank=True, null=True)
    NoteNo = models.CharField(max_length=255, blank=True, null=True)
    NoteDate = models.CharField(max_length=255, blank=True, null=True)
    ItemCode = models.CharField(max_length=255, blank=True, null=True)
    PartCode = models.CharField(max_length=255, blank=True, null=True)
    Stock = models.CharField(max_length=255, blank=True, null=True)
    Rework = models.CharField(max_length=255, blank=True, null=True)
    Reject = models.CharField(max_length=255, blank=True, null=True)
    ScrapReason = models.CharField(max_length=255, blank=True, null=True)
    ReworkScrapRemark = models.CharField(max_length=255, blank=True, null=True)
    RejectScrapRemark = models.CharField(max_length=255, blank=True, null=True)
    ScrapItemCode = models.CharField(max_length=255, blank=True, null=True)
    ScrapWt = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_verified = models.BooleanField(default=True)

    def __str__(self):
        return self.Plant or "Unnamed Plant"

class FGScrapItem(models.Model):  
    ItemDesc = models.ForeignKey(FGScrapDetails, related_name='scrap_items', on_delete=models.CASCADE)
    ItemDescription = models.CharField(max_length=255, blank=True, null=True)
    HeatCode = models.CharField(max_length=255, blank=True, null=True)
    ReworkQty = models.CharField(max_length=255, blank=True, null=True)
    Reason = models.CharField(max_length=255, blank=True, null=True)
    RejectQty = models.CharField(max_length=255, blank=True, null=True)
    Reason2 = models.CharField(max_length=255, blank=True, null=True)
    ScrapWt = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.HeatCode or "No Heat Code"

# Scrap Line Rejection Note
from django.db import models
class ScrapLineRejectionNote(models.Model):  
    Plant = models.CharField(max_length=255, blank=True, null=True)
    Series = models.CharField(max_length=255, blank=True, null=True)
    TrnType = models.CharField(max_length=255, blank=True, null=True)
    ScrapRejectionNo = models.CharField(max_length=255, blank=True, null=True) 
    ScrapRejectionNoteDate = models.CharField(max_length=255, blank=True, null=True)
    ItemNo = models.CharField(max_length=255, blank=True, null=True)
    HeatCode = models.CharField(max_length=255, blank=True, null=True)
    ScrapRejectionQty = models.CharField(max_length=255, blank=True, null=True)
    ScrapRejectRemark = models.CharField(max_length=255, blank=True, null=True)
    RejectReason = models.CharField(max_length=255, blank=True, null=True)
    cust_SuppName = models.CharField(max_length=255, blank=True, null=True)
    ScrapRejectionItem = models.CharField(max_length=255, blank=True, null=True)
    ScrapQty = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_verified = models.BooleanField(default=True)

    def __str__(self):
        return self.Plant or "Unnamed Plant"

class ScrapLineRejectionNoteDetails(models.Model):  
    ItemDesc = models.ForeignKey(ScrapLineRejectionNote, related_name='scrap_items', on_delete=models.CASCADE)
    ItemNo = models.CharField(max_length=255, blank=True, null=True)
    ScrapRejectionQty = models.CharField(max_length=255, blank=True, null=True)
    ReasonNote= models.CharField(max_length=255, blank=True, null=True)
    RejectReason=models.CharField(max_length=50,blank=True, null=True)
    ScrapRejectionItem = models.CharField(max_length=255, blank=True, null=True)
    ScrapQty = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.ItemNo or "ItemNo" 


# New Work Order
from django.db import models

class WorkOrderEntry(models.Model):
    wo_series = models.CharField(max_length=255, blank=True, null=True)
    wo_no = models.CharField(max_length=255, blank=True, null=True)
    customer = models.CharField(max_length=60, blank=True, null=True)
    wo_type = models.CharField(max_length=255, blank=True, null=True)
    wo_date = models.DateField(max_length=50, blank=True, null=True)
    Purchase_order_detail = models.CharField(max_length=50, blank=True, null=True)
    schedule_month = models.CharField(max_length=50, blank=True, null=True)
    target_date = models.DateField(max_length=50, blank=True, null=True)
    item = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return f"{self.wo_series} - {self.wo_no}"

class NewWorkOrderItem(models.Model):  # Renamed Item2 to MachineIdleTimeAss
    Work_Order_detail = models.ForeignKey(WorkOrderEntry, related_name='NewWorkOrderItem', on_delete=models.CASCADE)
    Purchase_order_detail = models.CharField(max_length=255, blank=True, null=True)
    item = models.CharField(max_length=255, blank=True, null=True)
    Description = models.CharField(max_length=255, blank=True, null=True)
    SO_Sch_Qty = models.CharField(max_length=255, blank=True, null=True)
    Bal_Qty = models.CharField(max_length=255, blank=True, null=True)
    Work_Order_Qty = models.CharField(max_length=255, blank=True, null=True)
    Remark = models.CharField(max_length=255, blank=True, null=True)
    Machine = models.CharField(max_length=255, blank=True, null=True)
    Shift = models.CharField(max_length=255, blank=True, null=True)
    Process = models.CharField(max_length=255, blank=True, null=True)
    Raw_Material = models.CharField(max_length=255, blank=True, null=True)

    def _str_(self):
        return self.Item_number