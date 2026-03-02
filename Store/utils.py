from datetime import datetime
from .models import InwardChallan2

def create_inwardNumber():
        current_year = datetime.now().year % 100  # e.g., 25
        next_year = (datetime.now().year + 1) % 100  # e.g., 26
        prefix = f"{current_year:02d}{next_year:02d}"  # '2526'
        
        # Start from 0001 to 9999 (max 4-digit counter)
        for counter in range(1, 10000):
            Inward = f"{prefix}{counter:05d}"  # '252600001' ... '252609999'
            
            # Ensure uniqueness in DB
            if not InwardChallan2.objects.filter(InwardF4No=Inward).exists():
                return Inward
        raise ValueError("No available challan numbers left for the current year range.")

from datetime import datetime
from .models import MaterialChallan

def create_challan_no():
    current_year = datetime.now().year % 100
    next_year = (datetime.now().year + 1) % 100
    prefix = f"{current_year:02d}{next_year:02d}"

    for counter in range(1, 10000):
        challan_no = f"{prefix}{counter:05d}"
        if not MaterialChallan.objects.filter(ChallanNo=challan_no).exists():
            return challan_no

    # only raise after all 9999 numbers are used
    raise ValueError("No available challan number left for the current year range.")



from datetime import datetime
from .models import JobworkInwardChallan

def create_jobwork_challan_no():
    current_year = datetime.now().year % 100
    next_year = (datetime.now().year + 1) % 100
    prefix = f"{current_year:02d}{next_year:02d}"

    for counter in range(1, 10000):
        inward_f4_no = f"{prefix}{counter:05d}"
        if not JobworkInwardChallan.objects.filter(InwardF4No=inward_f4_no).exists():
            return inward_f4_no

    raise ValueError("No available challan number left for the current year range.")