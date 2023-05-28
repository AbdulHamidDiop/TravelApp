from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import isNameValid, isUsernameValid, isPasswordValid, isTelephoneValid
from user.models import Traveller, Guide, TravellerPreferences

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
            'password': password,
            'password2': password2
        }

        if username == ""  or email == "" or password == "":
            messages.info(request, 'All fields must be filled')
            return render(request, 'landing/signup.html', context)
        
        if not isPasswordValid(password):
            messages.info(request, 'Password must have at least 8 caracters including at least 1 number')
            context['password'] = ''
            context['password2'] = ''
            return render(request, 'landing/signup.html', context)
        
        if not isUsernameValid(username):
            messages.info(request, 'Username must have at most 15 caracters')
            context['username'] = ''
            return render(request, 'landing/signup.html', context)

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use')
                context['email'] = ''
                return render(request, 'landing/signup.html', context)
            
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                context['username'] = ''
                return render(request, 'landing/signup.html', context)
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # Log the user in and redirect to the initial setup page
                userLogin = auth.authenticate(username=username, password=password)
                auth.login(request, userLogin)

                # Create a Traveller object for the new user
                newTravellerPreferences = TravellerPreferences.objects.create()
                newTravellerPreferences.save()
                newTraveller = Traveller.objects.create(user=user, preferences=newTravellerPreferences)
                newTraveller.save()
                return redirect('settings')
        else:
            messages.info(request, "Passwords don't match, please retry")
            context['password2'] = ''
            return render(request, 'landing/signup.html', context)
        
class LogIn(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        user2 = User.objects.filter(email = username).first()
        if user2 is not None:
            user2 = auth.authenticate(username = user2.username, password = password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        elif user2 is not None:
            auth.login(request, user2)
            return redirect('profile')
        else:
            messages.info(request, "Incorrect username or password, please retry")
            return redirect('login')

class GuideSignup(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        return render(request, 'landing/guidesignup.html')
    
    def post(self, request, *args, **kwargs):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        telephone = request.POST['telephone']
        context = { 'firstname': firstname, 'lastname': lastname, 'telephone': telephone}

        if firstname == "" or lastname == "" or telephone == "":
            messages.info(request, 'All fields must be filled')
            return render(request, 'landing/guidesignup.html', context)
        
        if not isTelephoneValid(telephone):
            messages.info(request, 'Invalid phone number')
            context = {'firstname': firstname, 'lastname': lastname, 'telephone': ''}
            return render(request, 'landing/guidesignup.html', context)

        if not isNameValid(firstname) or not isNameValid(lastname):
            messages.info(request, 'Invalid legal name')
            context = {'firstname': '', 'lastname': '', 'telephone': telephone}
            return render(request, 'landing/guidesignup.html', context)
        
        #create a Guide object for the user only if he doe not have one already
        try:
            userModel = User.objects.get(username=request.user.username)
            guide = Guide.objects.get(user=userModel) 
            messages.info(request, 'You are already registered as a guide')
            context = {'firstname': '', 'lastname': '', 'telephone': ''}
            return render(request, 'landing/guidesignup.html', context)
        except ObjectDoesNotExist:
            traveller = Traveller.objects.get(user=userModel)
            traveller.isGuide = True
            traveller.save()
            newGuide = Guide.objects.create(user=userModel, userID=userModel.id, firstName=firstname, lastName=lastname, telephone=telephone)
            newGuide.save()
            return redirect('profile')

class LogOut(LoginRequiredMixin,View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect('login')
