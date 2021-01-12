from django.http.response import HttpResponse
from django.urls import path
from . import views
app_name="flights_app"
urlpatterns=[
    path('',views.index,name="index"),
    path('airports',views.airports1,name="airlines_airports"),
    path('<int:flight_id>',views.flights_id,name="flight_id"),
    path('<int:flight_id>/book',views.book,name="book"),
    path('allpassengers',views.allpassengers,name="all_passengers")
]