from datetime import datetime
from .models import *


def generate_qc_number():
    current_year = datetime.now().year % 100      
    next_year = (datetime.now().year + 1) % 100   
    prefix = f"{current_year:02d}{next_year:02d}"  
    
    # counter from 00001 to 99999
    for counter in range(1, 100000):
        qc_no = f"{prefix}{counter:05d}"   # 252600001
        
        if not SalesReturnQcInfo.objects.filter(qc_no=qc_no).exists():
            return qc_no

    raise ValueError("No available QC numbers left for the current year range.")


def subcon_genrate_qc_no():
    current_year= datetime.now().year % 100
    next_year = (datetime.now().year +1 ) % 100
    prefix = f"{current_year:02d}{next_year:02d}"

    for counter in range(1 , 100000):
        qc=f"{prefix}{counter:05d}"

        if not SubconJobworkQCInfo.objects.filter(qc=qc).exists():
            return qc
    raise ValueError("No available QC numbers left for the current year range..")


def Inwardtedt_generate_qc_no():
    current_year = datetime.now().year % 100      
    next_year = (datetime.now().year + 1) % 100   
    prefix = f"{current_year:02d}{next_year:02d}"  
    
    # counter from 00001 to 99999
    for counter in range(1, 100000):
        qc_no = f"{prefix}{counter:05d}"   # 252600001
        
        if not InwardtestQCinfo.objects.filter(qc_no=qc_no).exists():
            return qc_no

    raise ValueError("No available QC numbers left for the current year range.")
