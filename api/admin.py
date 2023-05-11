from django.contrib import admin
from .models import Payment
from import_export.admin import ImportExportModelAdmin, ExportActionMixin

# Register your models here.

class PaymentAdmin(ExportActionMixin,  admin.ModelAdmin):
    list_display = ("name", "amount", "notes", "payment_date")
    list_filter = ("name", "payment_date")

admin.site.register(Payment, PaymentAdmin)
