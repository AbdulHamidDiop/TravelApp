from django.shortcuts import render
from django.views import View

# Create your views here.\

class SignUp(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/signup.html')

class LogIn(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/login.html')