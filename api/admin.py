from django.contrib import admin

from api.models import *

class BaseModelAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'modified_at')
    list_filter = ('created_at', 'modified_at')
    readonly_fields = ('created_at', 'modified_at')

    list_per_page = 50
    show_full_result_count = False

class CompanyAdmin(BaseModelAdmin):
    list_display = ('id', 'name', 'gst', 'created_at', 'modified_at')
    search_fields = ('id', 'name', 'gst', )

admin.site.register(Company, CompanyAdmin)

class ProductAdmin(BaseModelAdmin):
    list_display = ('id', 'name', 'cost', 'company', 'created_at', 'modified_at')
    search_fields = ('id', 'name', 'cost', 'company__name', )

admin.site.register(Product, ProductAdmin)

class PurchaseOrderAdmin(BaseModelAdmin):
    list_display = ('id', 'order_number', 'rate', 'total_price', 'created_at', 'modified_at')
    search_fields = ('id', 'order_number', 'rate', 'total_price', )

admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
