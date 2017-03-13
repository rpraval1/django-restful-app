from django.db import models

# Create your models here.
class OdmOrganization(models.Model):
    name = models.CharField(max_length=200)
    domain_name = models.CharField(max_length=200)
    locations = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s %s' % (self.name, self.domain_name, self.locations)

class OdmPeople(models.Model):
    name = models.CharField(max_length=200)
    locations = models.CharField(max_length=200)
    socials = models.CharField(max_length=200)
    types = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s %s %s' % (self.name, self.domain_name, self.locations, self.types)
