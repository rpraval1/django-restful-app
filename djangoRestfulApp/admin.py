from django.contrib import admin

# Register your models here.
from .models import OdmOrganization, OdmPeople

class OdmOrganizationAdmin(admin.ModelAdmin):
    fields = ['name', 'domain_name', 'locations']

class OdmPeopleAdmin(admin.ModelAdmin):
    fields = ['name', 'locations', 'socials', 'types']

admin.site.register(OdmOrganization, OdmOrganizationAdmin)
admin.site.register(OdmPeople, OdmPeopleAdmin)
