from django.db import models

# Create your models here.
def isNameValid(name):
    if len(name) > 20:
        return False
    if not name.isalpha():
        return False
    return True

def isUsernameValid(username):
    if len(username) > 15:
        return False
    return True

def isPasswordValid(password):
    if len(password) < 8:
        return False
    has_number = any(char.isdigit() for char in password)
    if not has_number:
        return False
    return True

def isTelephoneValid(telephone):
    if len(telephone) == 10:
        for digits in telephone:
            if not digits.isdigit():
                return False
        return True
    return False 


