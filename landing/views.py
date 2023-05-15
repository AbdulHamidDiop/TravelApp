from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import isPasswordValid
from user.models import Traveller, Guide

# Create your views here.
class SignUp(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/signup.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        context = {
            'username': username,
            'email': email,
        }

        if username == ""  or email == "" or password == "":
            messages.info(request, 'All fields must be filled')
            context = {'username': username, 'email': email}
            return render(request, 'landing/signup.html', context)
        
        if not isPasswordValid(password):
            messages.info(request, 'Password must have at least 8 caracters including at least 1 number')
            context = {'username': username, 'email': email}
            return render(request, 'landing/signup.html', context)

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use')
                context = {'username': username, 'email': ''}
                return render(request, 'landing/signup.html', context)
            
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                context = {'username': '', 'email': email}
                return render(request, 'landing/signup.html', context)
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #Log user in and direct to settings page 

                #create a Traveller object for the new user
                userModel = User.objects.get(username=username)
                newTraveller = Traveller.objects.create(user=userModel, userID = userModel.id)
                newTraveller.save()
                return redirect('login')
        else:
            messages.info(request, "Passwords don't match, please retry")
            context = {'username': username, 'email': email}
            return render(request, 'landing/signup.html', context)
        
        return render(request, 'landing/signup.html')

class LogIn(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/login.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'landing/login.html')
