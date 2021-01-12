from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    else:
        return HttpResponseRedirect(reverse("flights_app:index"))


def login3(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user1=authenticate(request,password=password,username=username)
        if user1 is not None:
            login(request,user1) 
            return HttpResponseRedirect(reverse("users:index"))
        else:    
            return HttpResponseRedirect(reverse("users:login"),{
                "message":"invalid credentials"
            })
    return render(request,"users/login.html",{

    })

def logout3(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:login"),{
        "logout_message":"logged out successfully"
    })
