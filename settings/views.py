from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from user.models import Traveller, TravellerPreferences
from django.contrib.auth.models import User
from django.contrib import messages
from landing.models import isNameValid, isUsernameValid
# Create your views here.

class Settings(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        traveller = Traveller.objects.get(user=request.user)
        context = {'firstname': traveller.firstName, 
                   'lastname': traveller.lastName, 
                   'bio': traveller.bio, 
                   'username': traveller.user.username, 
                   'partySize': traveller.preferences.partySize, 
                   'distance': traveller.preferences.distance, 
                   'interests': traveller.preferences.interests}
        return render(request, 'settings/settings.html', context)
    
    def post(self, request, *args, **kwargs):
        traveller = Traveller.objects.get(user=request.user)
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        bio = request.POST['bio']
        username = request.POST['username']

        partySize = request.POST['partySizeSelect']
        distance = request.POST['travelDistanceSelect']
        interests = request.POST['travellersSelect']
        context = {'firstname': traveller.firstName, 
                   'lastname': traveller.lastName, 
                   'bio': traveller.bio, 
                   'username': traveller.user.username, 
                   'partySize': traveller.preferences.partySize, 
                   'distance': traveller.preferences.distance, 
                   'interests': traveller.preferences.interests}

        if username != traveller.user.username:
            if User.objects.filter(username=username).exists():
                traveller.user.username = username
                traveller.user.save()
            else:
                messages.info(request, 'Username already taken')

        if firstname != traveller.firstName:
            if isNameValid(firstname):
                traveller.firstname = firstname
                traveller.save()
            else:
                messages.info(request, 'First name invalid')

        if lastname != traveller.lastName:
            if isNameValid(lastname):
                traveller.lastname = lastname
                traveller.save()
            else:
                messages.info(request, 'Last name invalid')
        
        if bio != traveller.bio:
            traveller.bio = bio
            traveller.save()
        
        if partySize != traveller.preferences.partySize:
            traveller.preferences.partySize = partySize
            traveller.preferences.save()
            traveller.save()
        
        if distance != traveller.preferences.distance:
            traveller.preferences.distance = distance
            traveller.preferences.save()
            traveller.save()

        if interests != traveller.preferences.interests:
            traveller.preferences.interests = interests
            traveller.preferences.save()
            traveller.save()
            context['interests'] = interests
        
        return render(request, 'settings/settings.html', context)    
     
class ProfileSettings(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        return render(request, 'settings/profile.html')