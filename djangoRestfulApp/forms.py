
from django import forms
from .models import OdmOrganization, OdmPeople


class OdmOrgForm(forms.ModelForm):
    class Meta:
        model = OdmOrganization
        fields = ('name',)#name of the fields you want to show on the form

class OdmPeopleForm(forms.ModelForm):
    class Meta:
        model = OdmPeople
        fields = ('name',)#name of the fields you want to show on the form
