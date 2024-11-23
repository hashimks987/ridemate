from django.shortcuts import render
from .models import TravelPackage
from django.db.models import Q
from .models import Car
# Create your views here.
def home(request):
    package = TravelPackage.objects.all()
    print(package)
    return render(request, 'index.html', {'packages': package})

def packages_list(request):
    package = TravelPackage.objects.all()
    return render(request, 'packages-list.html', {'packages': package})


def travaller(request):
    cars = Car.objects.filter(is_available=True, category__name='Traveller')
    return render(request, 'traveller.html', {'cars': cars})
 



def sedans(request):
   
    cars = Car.objects.filter(is_available=True, category__name='Sedan')
    return render(request, 'sedan.html', {'cars': cars})

def suvs(request):
    cars = Car.objects.filter(is_available=True, category__name='SUV')
    return render(request, 'suv.html', {'cars': cars})

