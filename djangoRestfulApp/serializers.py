from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import OdmOrganization, OdmPeople

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class OdmOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = OdmOrganization
        fields = ['name']


class OdmPeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OdmPeople
        fields = ('url', 'name')
