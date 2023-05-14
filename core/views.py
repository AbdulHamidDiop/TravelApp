from django.shortcuts import render
from django.views import View

# Create your views here.\

class DashBoard(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/dashboard.html')
    
class Chats(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/chats.html')

class Posts(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/posts.html')
    
class Explore(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/explore.html')

class Profile(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/profile.html')

