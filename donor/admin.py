from django.contrib import admin
from .models import Donor

# Register your models here.
class DonorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Donor._meta.fields if field.name != "id"]
    readonly_fields = ('name', 'email', 'donor_type', 'organisation_name', 'pledge_amount', 'pledge_date',)
    list_filter = ('name',)


admin.site.register(Donor, DonorAdmin)