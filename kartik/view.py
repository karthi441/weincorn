from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
# Create your views here.
def home(request):
    return render(request,"index.html")
def signup(request):
    if request.method=="POST":
        print(request.POST)
        username=request.POST.get('name')
        #fname=request.POST.get('fname')
        #lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        #pass2=request.POST.get('pass2 ')
        myuser=User.objects.create_user(username=username,email=email,password=pass1)
        #myuser.first_name=username
        #myuser.last_name=lname
        myuser.save()
        HttpResponse("Your account has been created")
        return redirect('Base')
    return render(request,"signup.html")
def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass1']
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"authentication/index.html",{'fname':fname})
        else:
            messages.error(request,"Bad Credentials!")
            return redirect('home')



    return render(request,"authentication/signin.html")
def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully! ")
    return redirect('home')