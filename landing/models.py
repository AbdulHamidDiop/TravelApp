from django.db import models

# Create your models here.
def isPasswordValid(password):
    if len(password) < 8:
        return False
    has_number = any(char.isdigit() for char in password)
    if not has_number:
        return False
    return True

#for loop that iterates through a loop 



