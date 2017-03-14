from django.shortcuts import render
from django.conf import settings

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import OdmOrganization, OdmPeople
from .forms import OdmOrgForm, OdmPeopleForm
from .serializers import OdmOrgSerializer, OdmPeopleSerializer, UserSerializer, GroupSerializer
import requests
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



def index(request):
    return render(request, 'djangoRestfulApp/index.html')

def organization(request):
    if request.method == "POST":
        form = OdmOrgForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            r = requests.get('https://api.crunchbase.com/v/3/odm-organizations?name=' + name + '&user_key=' + settings.CRUNCHBASE_KEY)
            json = r.json()
            return render(request, 'djangoRestfulApp/organizations.html', {
            'organization': json,
            })
    else:
        form = OdmOrgForm()

    return render(request, 'djangoRestfulApp/organizationForm.html', {
        'form': form,
    })


def people(request):
    if request.method == "POST":
        form = OdmPeopleForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            r = requests.get('https://api.crunchbase.com/v/3/odm-people?name=' + name + '&user_key=' + settings.CRUNCHBASE_KEY)
            json = r.json()
            return render(request, 'djangoRestfulApp/people.html', {
            'people': json,
            })

    else:
        form = OdmPeopleForm()

    return render(request, 'djangoRestfulApp/peopleForm.html', {
        'form': form,
    })
