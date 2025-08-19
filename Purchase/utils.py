from num2words import num2words
from datetime import datetime
from .models import RFQ

def convert_to_words(amount):
    # Convert float or int to words, using Indian English currency style
    return num2words(amount, to='currency', lang='en_IN')


def Create_RFQ_No():
        current_year = datetime.now().year % 100  # e.g., 25
        next_year = (datetime.now().year + 1) % 100  # e.g., 26
        prefix = f"{current_year:02d}{next_year:02d}"  # '2526'
        
        # Start from 0001 to 9999 (max 4-digit counter)
        for counter in range(1, 10000):
            rfq_no = f"{prefix}{counter:05d}"  # '252600001' ... '252609999'
            
            # Ensure uniqueness in DB
            if not RFQ.objects.filter(rfq_no=rfq_no).exists():
                 return rfq_no
        raise ValueError("No available rfq numbers left for the current year range.")