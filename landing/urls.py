from django.urls import path
from landing.views import SignUp, LogIn, GuideSignup ,LogOut

urlpatterns = [
    path('signup/', SignUp.as_view(), name = 'signup'),
    path('login/', LogIn.as_view(), name = 'login'),
    path('logout/', LogOut.as_view(), name = 'logout'),
    path('guidesignup/', GuideSignup.as_view(), name = 'guidesignup'),
]