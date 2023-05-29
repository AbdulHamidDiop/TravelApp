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
        context = {'traveller': traveller}
        return render(request, 'settings/settings.html', context)
    
    def post(self, request, *args, **kwargs):
        traveller = Traveller.objects.get(user=request.user)
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        bio = request.POST['bio']
        username = request.POST['username']
        profilepicture = request.FILES.get('profilepicture')

        partySize = request.POST['partySizeSelect']
        distance = request.POST['travelDistanceSelect']
        interests = request.POST['travellersSelect']
        context = {'traveller': traveller}

        if profilepicture != traveller.profilePic:
            if request.FILES.get('profilepicture') == None:
                profilepicture = traveller.profilePic
            traveller.profilePic = profilepicture
            traveller.save()
            
        if username != traveller.user.username:
            if not User.objects.filter(username=username).exists() and isUsernameValid(username):
                traveller.user.username = username
                traveller.user.save()
            else:
                messages.info(request, 'Username invalid')
                return render(request, 'settings/settings.html', context)

        if firstname != traveller.firstName:
            if isNameValid(firstname):
                traveller.firstName = firstname
                traveller.save()
            else:
                messages.info(request, 'First name invalid')
                return render(request, 'settings/settings.html', context)

        if lastname != traveller.lastName:
            if isNameValid(lastname):
                traveller.lastName = lastname
                traveller.save()
            else:
                messages.info(request, 'Last name invalid')
                return render(request, 'settings/settings.html', context)
        
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
        
        return render(request, 'settings/settings.html', context)    
     
class ProfileSettings(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        traveller = Traveller.objects.get(user=request.user)
        context = {'traveller': traveller}
        return render(request, 'settings/profilesettings.html', context)
    
    def post(self, request, *args, **kwargs):
        traveller = Traveller.objects.get(user=request.user)
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        bio = request.POST['bio']
        username = request.POST['username']
        profilepicture = request.FILES.get('profilepicture')

        partySize = request.POST['partySizeSelect']
        distance = request.POST['travelDistanceSelect']
        interests = request.POST['travellersSelect']
        context = {'traveller': traveller}

        if profilepicture != traveller.profilePic:
            if request.FILES.get('profilepicture') == None:
                profilepicture = traveller.profilePic
            traveller.profilePic = profilepicture
            traveller.save()
            
        if username != traveller.user.username:
            if not User.objects.filter(username=username).exists() and isUsernameValid(username):
                traveller.user.username = username
                traveller.user.save()
            else:
                messages.info(request, 'Username invalid')
                return render(request, 'settings/profilesettings.html', context)

        if firstname != traveller.firstName:
            if isNameValid(firstname):
                traveller.firstName = firstname
                traveller.save()
            else:
                messages.info(request, 'First name invalid')
                return render(request, 'settings/profilesettings.html', context)

        if lastname != traveller.lastName:
            if isNameValid(lastname):
                traveller.lastName = lastname
                traveller.save()
            else:
                messages.info(request, 'Last name invalid')
                return render(request, 'settings/profilesettings.html', context)
        
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
        
        return render(request, 'settings/profilesettings.html', context)