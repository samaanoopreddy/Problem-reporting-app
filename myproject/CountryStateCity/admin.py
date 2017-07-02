from django.contrib import admin
from django.db import models

# Register your models here.
from . models import Country,City,State
class CountryAdmin(admin.ModelAdmin):
    list_display = ("__str__", "name", "code","created_at","updated_at")
    list_filter = ['name','code']
    search_fields = ['name','code']
    list_display_links = list_display


    fieldsets = (
        ('NAME AND CODE OF THE COUNTRIES', {'fields': ('name', 'code')}),
    )

    def get_queryset(self, request):
        query = super(CountryAdmin, self).get_queryset(request)
        queryset = query.order_by('name')
        return queryset

    class Meta:
        model=Country


class StateAdmin(admin.ModelAdmin):
    list_display = ("__str__", "name","country", "code")
    list_filter = ('country',)
    search_fields = ['name','code']
    list_display_links = list_display
    fieldsets = (
        ('name and code of the contries',{'fields':('name','code')}),
        ('country of the state', {'fields': ('country',)})

    )




    class Meta:
        model=State

class CityAdmin(admin.ModelAdmin):
    list_display = ("__str__", "name",'state')
    list_filter = (
        ('state', admin.RelatedOnlyFieldListFilter),
    )
    search_fields = ['name']
    list_display_links = list_display
    class Meta:
        model=City

    fieldsets = (
        ('name of the city',{'fields':('name',)}),
        ('name of the state',{'fields':('state',)}),
    )

admin.site.register(Country,CountryAdmin)
admin.site.register(City,CityAdmin)
admin.site.register(State,StateAdmin)

