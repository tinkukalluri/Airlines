from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import flights,airports, passengers
from django.db import models
from django.urls import reverse


def index(request):
    return render(request,"flights/index.html",{
        "flights":flights.objects.all()
    })
def airports1(request):
    return render(request,"flights/airports.html",{
        "airports":airports.objects.all()
    })

def flights_id(request,flight_id):
    flight3=flights.objects.get(id=flight_id)
    passenger=passengers.objects.get(id=flight_id)
    passenger2=flight3.passenger.all()
    all_flight=flights.objects.all()
    return render(request,"flights/flights_id.html",{
        "flight_id":flight_id,
        "flights":flight3,
        "passenger":passenger2,
        "non_passengers":passengers.objects.exclude(flights6=flight3).all()
    })

def book(request,flight_id):
    if request.method=="POST" and not request.POST["passenger"]=="empty":
        f=flights.objects.get(pk=flight_id)
        passenger1=passengers.objects.get(pk=int(request.POST["passenger"]))
        passenger1.flights6.add(f)
        return HttpResponseRedirect(reverse("flights_app:flight_id",args=(flight_id,)))
    else:
        return HttpResponse("oops something went wrong")

def allpassengers(request):
    return render(request,"flights/allpassengers.html",{
        "all_passengers":passengers.objects.all()
    })