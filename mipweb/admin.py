from mipweb.models import TeamMember
from django.contrib import admin

from .models import TeamMember

# Register your models here.

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_filter = ('last_name',)


admin.site.register(TeamMember, TeamMemberAdmin)