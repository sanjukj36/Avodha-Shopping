from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                password=password, email=email)
                user.save()
                print('..........user..saved..', username, '.........')
        else:
            messages.info(request, 'incorrect password')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'Registration.html')


def login(request):
    if request.method == 'POST':
        un = request.POST['username']
        p = request.POST['password']
        user = auth.authenticate(username=un, password=p)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid details')
            return redirect('login')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
