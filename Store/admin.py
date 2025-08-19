from django.contrib import admin

# Register your models here.
from .models import FGMovement

@admin.register(FGMovement)
class FGMovementAdmin(admin.ModelAdmin):
    list_display = [
        'trn_no', 'date', 'fg_item_code', 'fg_item_name', 
        'ok_qty', 'rework_qty', 'reject_qty', 'created_by', 'created_at'
    ]
    list_filter = ['date', 'stock_view', 'created_at']
    search_fields = ['trn_no', 'fg_item_code', 'fg_item_name', 'heat_code']
    readonly_fields = ['trn_no', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Transaction Info', {
            'fields': ('trn_no', 'date')
        }),
        ('Item Details', {
            'fields': ('fg_item_code', 'fg_item_name', 'fg_item_description')
        }),
        ('Operation & Quantities', {
            'fields': ('operation', 'ok_qty', 'rework_qty', 'reject_qty')
        }),
        ('Additional Info', {
            'fields': ('heat_code', 'stock_view', 'remark')
        }),
        ('System Info', {
            'fields': ('created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
