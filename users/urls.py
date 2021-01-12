from django.urls import path
from . import views

app_name="users"
urlpatterns=[
    path('',views.index,name="index"),
    path("login",views.login3,name="login"),
    path("logout",views.logout3,name="logout")
]