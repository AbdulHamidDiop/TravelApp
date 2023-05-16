from django.db import models

# Create your models here.
def isPasswordValid(password):
    if len(password) < 8:
        return False
    has_number = any(char.isdigit() for char in password)
    if not has_number:
        return False
    return True

#function that verifys that the telephone number is valid and that it is all digits
def isTelephoneValid(telephone):
    if len(telephone) == 10:
        for digits in telephone:
            if not digits.isdigit():
                return False
        return True
    return False 

