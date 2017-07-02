from django.conf.urls import url,include
from django.contrib import admin

from .views import country,state,city,statesInCountries,citiesInStates
urlpatterns = [
    url(r'^$', country, name='index'),
url(r'^(?P<number>\d+)$', statesInCountries,name='detailCountry'),
url(r'^state/(?P<number>\d+)$', citiesInStates,name='detailstate'),
url(r'^state', state),
url(r'^city', city),
]

