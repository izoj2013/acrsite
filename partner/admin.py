from django.contrib import admin
from .models import Partner

# Register your models here.
class PartnerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Partner._meta.fields if field.name != "id"]
    readonly_fields = ('organisation_name', 'contact_email', 'partnership_type', 'description',)
    list_filter = ('organisation_name', 'partnership_type',)


admin.site.register(Partner, PartnerAdmin)