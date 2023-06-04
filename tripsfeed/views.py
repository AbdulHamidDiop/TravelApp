from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from user.models import Traveller
from tripsfeed.models import Trip, PinTrip
from django.contrib.auth.models import User
import datetime
from tripsfeed.templatetags.filters import register
from tripsfeed.templatetags.filters import getItem
# Create your views here.\

class TripsFeed(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        traveller = Traveller.objects.filter(user=user).first()
        if traveller==None:
            return redirect('login')
        trips = Trip.objects.all()
        profilePics = {}

        for trip in trips:
            username = trip.user
            user = User.objects.get(username=username)
            traveller = Traveller.objects.get(user=user)
            profilePics[username] = traveller.profilePic.url

        context = {'traveller': traveller, 'trips': trips, 'profilePics': profilePics, 'register': register, 'getItem': getItem}
        return render(request, 'tripsfeed/tripsfeed.html', context)

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        traveller = Traveller.objects.get(user=user)
        formtype = request.POST.get('formtype')

        if formtype == 'newtrip':
            
            image = request.FILES.get('postpicture')
            city = request.POST['city']
            country = request.POST['country']
            startDate = datetime.date(2023, 5, 17)
            endDate =  datetime.date(2023, 5, 17)
            partySize = request.POST['partysize']
            description = request.POST['description']

            trip = Trip.objects.create(user=user.username, image=image, city=city, country=country, startDate=startDate, endDate=endDate, partySize=partySize, description=description)
            if city != "" and country != "":
                trip.isReady = True
            trip.save()
            traveller.trips.add(trip)
            traveller.save()
            return redirect('tripsfeed')

        return redirect('tripsfeed')

class PinTripView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        username = request.user.username
        tripID = request.GET.get('tripID')
        trip = Trip.objects.get(id=tripID)

        tripFilter = PinTrip.objects.filter(username=username, tripID=tripID).first()

        if tripFilter == None:
            pinTrip = PinTrip.objects.create(username=username, tripID=tripID)
            pinTrip.save()
            trip.pins += 1
            trip.save()
        else:
            tripFilter.delete()
            trip.pins -= 1
            trip.save()

        return redirect('tripsfeed')
    def post(self, request, *args, **kwargs):
        return redirect('tripsfeed')

