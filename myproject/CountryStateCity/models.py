from django.db import models

# Create your models here.
from django.core.validators import URLValidator
from smart_selects.db_fields import ChainedForeignKey
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


class University(models.Model):
    name = models.CharField(max_length=255)
    website = models.CharField(max_length=255, validators=[URLValidator()], default="")

    established_year = models.DateField()

    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    state = ChainedForeignKey(
        State, chained_field="country", chained_model_field="country",
        show_all=False, auto_choose=True, sort=True,null=True,blank = True)

    cities = ChainedForeignKey(
        City, chained_field="state", chained_model_field="state",
        show_all=False, auto_choose=True, sort=True,null=True,blank = True)

    def __str__(self):
        return self.name

