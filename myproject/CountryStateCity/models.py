from django.db import models

# Create your models here.
from django.core.validators import URLValidator

from django.db import models

# Create your models here.

class Country(models.Model):
    name=models.CharField(unique=True,max_length=50)
    code=models.CharField(unique=True,max_length=5)
    created_at=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at=models.DateTimeField(auto_now_add=False, auto_now=True)
    class Meta:
        verbose_name_plural = "Countries"
    def __str__(self):
        return "<"+self.name+"-"+self.code+">"
class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=5)
    def __str__(self):
        return "<"+self.name+"-"+self.code+">"
class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name=models.CharField(unique=True,max_length=50)
    class Meta:
        verbose_name_plural = "Cities"
    def __str__(self):
        return "<"+self.name+">"

