from django.shortcuts import render,HttpResponse,Http404,get_object_or_404
from . models  import Country,State,City
# Create your views here.
def country(request):
    countries=Country.objects.all()
    dic = {'countries': countries}
    return render(request, 'CountryStateCity\country.html',context={'di':dic})

def state(request):
    states=State.objects.all()
    return render(request, 'CountryStateCity\state.html',context={'dic':states})

def city(request):
    cities=City.objects.all()
    return render(request, 'CountryStateCity\city.html',{'dic':cities})

def statesInCountries(request,number):
    try:
        category=Country.objects.get(id=number).state_set.all()
    except:
        category=None
        raise Http404("hey , there are only 5 countries so, please enter a number less than 5")
    # category=get_object_or_404(Country,pk=number)

    dic={'category':category}
    return render(request, 'CountryStateCity\statesInCountries.html', {'di':dic })

def citiesInStates(request,number):
    try:
        category = State.objects.get(id=number).city_set.all()
    except:
        category=None
    dic = {'category': category}
    return render(request, 'CountryStateCity\citiesInStates.html', {'di': dic})
