from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Place


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    return render(request, "index.html", {'datas': obj})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        f_name = request.POST['firstname']
        l_name = request.POST['lastname']
        email = request.POST['emailid']
        password = request.POST['password']
        cpass = request.POST['cpassword']
        if password == cpass:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "Username is Taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is Taken")
                return redirect("register")
            else:
                user = User.objects.create_user(username=uname, first_name=f_name, last_name=l_name, email=email,
                                                password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "Password not Matching")
            return redirect('register')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def about(request):
    return render(request, "about.html")
