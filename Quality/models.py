from django.db import models

# Create your models here.


class InwardtestQCinfo(models.Model):
    qc_no=models.CharField(max_length=50,blank=True,null=True)
    sample_qty=models.CharField(max_length=50,blank=True,null=True)
    prod_qty=models.CharField(max_length=50,blank=True,null=True)
    qc_qty=models.CharField(max_length=50,blank=True,null=True)
    ok_qty=models.CharField(max_length=50,blank=True,null=True)
    date=models.DateField(blank=True,null=True)
    qc_time=models.TimeField(blank=True,null=True)
    a_u_d_qty=models.CharField(max_length=50,blank=True,null=True)
    drawing_rev_no=models.CharField(max_length=50,blank=True,null=True)
    format_no=models.CharField(max_length=50,blank=True,null=True)
    rev_no=models.CharField(max_length=50,blank=True,null=True)
    rev_date=models.DateField(blank=True,null=True)
    accepted_or_rejected=models.TextField(max_length=200,blank=True,null=True)
    accepted_under_deviation=models.TextField(max_length=200,blank=True,null=True)
    suggestion=models.TextField(max_length=200,blank=True,null=True)
    inspected_by=models.CharField(max_length=50,blank=True,null=True)
    remark=models.TextField(max_length=200,blank=True,null=True)
    non_conformece=models.TextField(max_length=200,blank=True,null=True)
    approved_by=models.CharField(max_length=200,blank=True,null=True)


class InwardtestDimensional(models.Model):
    qc = models.ForeignKey(InwardtestQCinfo,related_name='dimension_tests', on_delete=models.CASCADE)
    test_no=models.CharField(max_length=200,blank=True,null=True)
    test_description=models.CharField(max_length=200,blank=True,null=True)
    specification=models.CharField(max_length=200,blank=True,null=True)
    dimensions=models.CharField(max_length=200,blank=True,null=True)
    tol_sub=models.CharField(max_length=200,blank=True,null=True)
    tol_add=models.CharField(max_length=200,blank=True,null=True)
    methods_of_check=models.CharField(max_length=200,blank=True,null=True)
    one=models.CharField(max_length=200,blank=True,null=True)
    two=models.CharField(max_length=200,blank=True,null=True)
    three=models.CharField(max_length=200,blank=True,null=True)
    four=models.CharField(max_length=200,blank=True,null=True)
    five=models.CharField(max_length=200,blank=True,null=True)
    remark=models.TextField(max_length=250,blank=True,null=True)
    actual_observation=models.CharField(max_length=250,blank=True,null=True)


class Inwardtestvisulainspection(models.Model):
    qc = models.ForeignKey(InwardtestQCinfo,related_name='visual_tests', on_delete=models.CASCADE)

    test_no=models.CharField(max_length=200,blank=True,null=True)
    test_description=models.CharField(max_length=200,blank=True,null=True)
    specification=models.CharField(max_length=200,blank=True,null=True)
    methods_of_check=models.CharField(max_length=200,blank=True,null=True)
    one=models.CharField(max_length=200,blank=True,null=True)
    two=models.CharField(max_length=200,blank=True,null=True)
    three=models.CharField(max_length=200,blank=True,null=True)
    four=models.CharField(max_length=200,blank=True,null=True)
    five=models.CharField(max_length=200,blank=True,null=True)
    merge=models.BooleanField(default=True)
    remark=models.TextField(max_length=250,blank=True,null=True)


class InwardtestreworkQty(models.Model):
    qc = models.ForeignKey(InwardtestQCinfo,related_name='rework_qty', on_delete=models.CASCADE)

    description=models.CharField(max_length=200,blank=True,null=True)
    qty=models.CharField(max_length=200,blank=True,null=True)

class InwardtestrejectQty(models.Model):
    qc = models.ForeignKey(InwardtestQCinfo,related_name='reject_qty', on_delete=models.CASCADE)

    description=models.CharField(max_length=200,blank=True,null=True)
    qty=models.CharField(max_length=200,blank=True,null=True)





class SubconJobworkQCInfo(models.Model):
    qc=models.CharField(max_length=50,blank=True,null=True)
    qc_date=models.DateTimeField(blank=True,null=True)
    format_no=models.CharField(blank=True ,null=True)
    vendor_heat_code=models.CharField(max_length=50,blank=True,null=True)
    vendor_tc_no = models.CharField(max_length=200,blank=True,null=True)
    rev_no=models.CharField(max_length=200,blank=True ,null=True)
    lot_accepted_rejected=models.CharField(max_length=200,blank=True,null=True)
    sample_qty=models.CharField(max_length=50,blank=True,null=True)
    rev_date = models.DateField(blank=True,null=True)
    control_plan_no= models.CharField(max_length=200,blank=True,null=True)
    wire_size = models.CharField(max_length=200,blank=True,null=True)
    total_coil=models.CharField(max_length=200,blank=True,null=True)
    coil_from_no = models.CharField(max_length=200 ,blank=True , null=True)
    coil_to_no =models.CharField(max_length=200,blank=True,null=True)
    heat_no = models.CharField(max_length=200,blank=True,null=True)
    grn_qty=models.CharField(max_length=200,blank=True ,null=True)
    qc_qty = models.CharField(max_length=200,blank=True,null=True)
    qc_pending_qty=models.CharField(max_length=200, blank=True ,null=True)
    qc_qty=models.CharField(max_length=200,blank=True,null=True)
    ok_qty=models.CharField(max_length=200,blank=True,null=True)
    rework_qty=models.CharField(max_length=200,blank=True,null=True)
    reject_qty=models.CharField(max_length=200,blank=True,null=True)
    store_qty=models.CharField(max_length=200,blank=True,null=True)
    a_u_d_qty=models.CharField(max_length=200,blank=True,null=True)
    raw_material=models.CharField(max_length=200,blank=True,null=True)
    drawing_rev_no = models.CharField(max_length=200,blank=True,null=True)
    lab_mill_tc_no =models.CharField(max_length=200,blank=True,null=True)
    lab_mill_tc_name =models.CharField(max_length=200,blank=True,null=True)
    lab_mill_tc_date =models.DateField(blank=True,null=True)
    remark = models.TextField(max_length=250,blank=True,null=True)
    def __str__(self):
        return f"QC - {self.qc}"

class SubconJobworkDimensional(models.Model): 
    qc = models.ForeignKey(SubconJobworkQCInfo,related_name="dimension_tests", on_delete=models.CASCADE )   
    test_no=models.CharField(max_length=200,blank=True,null=True)
    test_description=models.CharField(max_length=200,blank=True,null=True)
    specification=models.CharField(max_length=200,blank=True,null=True)
    dimensions=models.CharField(max_length=200,blank=True,null=True)
    tol_sub=models.CharField(max_length=200,blank=True,null=True)
    tol_add=models.CharField(max_length=200,blank=True,null=True)
    methods_of_check=models.CharField(max_length=200,blank=True,null=True)
    one=models.CharField(max_length=200,blank=True,null=True)
    two=models.CharField(max_length=200,blank=True,null=True)
    three=models.CharField(max_length=200,blank=True,null=True)
    four=models.CharField(max_length=200,blank=True,null=True)
    five=models.CharField(max_length=200,blank=True,null=True)
    remark=models.TextField(max_length=250,blank=True,null=True)
  

class SubconJobworkvisulainspection(models.Model):
    qc = models.ForeignKey(SubconJobworkQCInfo,related_name="visual_tests",on_delete=models.CASCADE  )

    test_no=models.CharField(max_length=200,blank=True,null=True)
    test_description=models.CharField(max_length=200,blank=True,null=True)
    specification=models.CharField(max_length=200,blank=True,null=True)
    methods_of_check=models.CharField(max_length=200,blank=True,null=True)
    one=models.CharField(max_length=200,blank=True,null=True)
    two=models.CharField(max_length=200,blank=True,null=True)
    three=models.CharField(max_length=200,blank=True,null=True)
    four=models.CharField(max_length=200,blank=True,null=True)
    five=models.CharField(max_length=200,blank=True,null=True)
    merge=models.BooleanField(default=True)
    remark=models.TextField(max_length=250,blank=True,null=True)


class SubconJobworkreworkQty(models.Model):
    qc = models.ForeignKey(SubconJobworkQCInfo,related_name="rework_items",on_delete=models.CASCADE  )  
    description=models.CharField(max_length=200,blank=True,null=True)
    qty=models.CharField(max_length=200,blank=True,null=True)
    supplier = models.CharField(max_length=200,blank=True,null=True)

class SubconJobworkrejectQty(models.Model):
    qc = models.ForeignKey(SubconJobworkQCInfo,related_name="reject_items",on_delete=models.CASCADE )
    description=models.CharField(max_length=200,blank=True,null=True)
    qty=models.CharField(max_length=200,blank=True,null=True)
    supplier = models.CharField(max_length=200,blank=True,null=True)




class SalesReturnQcInfo(models.Model):
    rejection_series=models.CharField(max_length=200,blank=True,null=True)
    qc_no=models.CharField(max_length=200,blank=True,null=True)
    qc_date=models.DateField(blank=True,null=True)
    cust_vender_name=models.CharField(max_length=200,blank=True,null=True)
    select_item=models.CharField(max_length=200,blank=True,null=True)
    part_code=models.CharField(max_length=200,blank=True,null=True)
    heat_no=models.CharField(max_length=200,blank=True,null=True)
    New_heat_no=models.CharField(max_length=200,blank=True,null=True)
    return_qty=models.CharField(max_length=200,blank=True,null=True)
    ok_qty=models.CharField(max_length=200,blank=True,null=True)
    rework_qty=models.CharField(max_length=200,blank=True,null=True)
    reject_qty=models.CharField(max_length=200,blank=True,null=True)
    rework_reason=models.CharField(max_length=200,blank=True,null=True)
    reject_reason=models.CharField(max_length=200,blank=True,null=True)
    action_plan=models.CharField(max_length=200,blank=True,null=True)
    action=models.CharField(max_length=200,blank=True,null=True)
    action_date=models.DateField(blank=True,null=True)
    remark=models.TextField(max_length=250,blank=True,null=True)
    inspected_by=models.CharField(max_length=200,blank=True,null=True)
    approved_by=models.CharField(max_length=200,blank=True,null=True)




class SalesReturnDimensional(models.Model): 
    qc = models.ForeignKey(SalesReturnQcInfo,related_name="dimension_tests",on_delete=models.CASCADE   )
    test_no=models.CharField(max_length=200,blank=True,null=True)
    test_description=models.CharField(max_length=200,blank=True,null=True)
    specification=models.CharField(max_length=200,blank=True,null=True)
    dimensions=models.CharField(max_length=200,blank=True,null=True)
    tol_sub=models.CharField(max_length=200,blank=True,null=True)
    tol_add=models.CharField(max_length=200,blank=True,null=True)
    methods_of_check=models.CharField(max_length=200,blank=True,null=True)
    one=models.CharField(max_length=200,blank=True,null=True)
    two=models.CharField(max_length=200,blank=True,null=True)
    three=models.CharField(max_length=200,blank=True,null=True)
    four=models.CharField(max_length=200,blank=True,null=True)
    five=models.CharField(max_length=200,blank=True,null=True)
    remark=models.TextField(max_length=250,blank=True,null=True)
  

class SalesReturnvisulainspection(models.Model):
    qc = models.ForeignKey(SalesReturnQcInfo,related_name="visual_tests",on_delete=models.CASCADE )
    test_no=models.CharField(max_length=200,blank=True,null=True)
    test_description=models.CharField(max_length=200,blank=True,null=True)
    check_points=models.CharField(max_length=200,blank=True,null=True)
    actual_observation=models.CharField(max_length=200,blank=True,null=True)
    one=models.CharField(max_length=200,blank=True,null=True)
    two=models.CharField(max_length=200,blank=True,null=True)
    three=models.CharField(max_length=200,blank=True,null=True)
    four=models.CharField(max_length=200,blank=True,null=True)
    five=models.CharField(max_length=200,blank=True,null=True)
    merge=models.BooleanField(default=True)
    remark=models.TextField(max_length=250,blank=True,null=True)
