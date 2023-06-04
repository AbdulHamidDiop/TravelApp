from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from user.models import Traveller
# Create your views here.\

class Profile(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, pk, *args, **kwargs):
        profileUser = User.objects.get(username=pk)
        traveller = Traveller.objects.get(user=profileUser)
        trips = traveller.trips.all()

        context = {'traveller': traveller, 'trips': trips}
        return render(request, 'userprofile/profile.html', context)
    
    def post(self, request, pk, *args, **kwargs):
        return render(request, 'userprofile/profile.html')