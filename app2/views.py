from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('app2:new')
        messages.info(request,'invalid credentials')
        return redirect('app2:login')
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if cpassword==password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('app2:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('app2:register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('app2:login')
        messages.info(request,'password not matching')
        return redirect('app2:register')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def new(request):
    return render(request,'new.html')