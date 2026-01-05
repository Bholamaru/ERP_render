from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import onwardchallan, ChallanCounter
from .models import transportdetails
from .models import vehicaldetails
from .models import outwardchallan
from .models import *

@admin.register(onwardchallan)
class OnwardChallanAdmin(admin.ModelAdmin):
    readonly_fields = ('challan_no',)
    # or to hide it completely:
    # exclude = ('challan_no',)
@admin.register(transportdetails)
class TransportDetailsAdmin(admin.ModelAdmin):
    pass

@admin.register(vehicaldetails)
class VehicalDetailsAdmin(admin.ModelAdmin):
    pass

@admin.register(ChallanCounter)
class ChallanCounterAdmin(admin.ModelAdmin):
    pass
@admin.register(outwardchallan)
class outwardchallanAdmin(admin.ModelAdmin):
    pass

admin.site.register(OnwardChallanItem)
admin.site.register(NewSalesOrder)
admin.site.register(NewSalesItemdetails)
admin.site.register(Invoice)
admin.site.register(InvoiceItemdetails)
admin.site.register(GstdetailsInvoice)