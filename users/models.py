from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified=models.DateTimeField(User,auto_now=True)
    phone_number = models.CharField(max_length=15,blank=True)
    date_of_birth=models.DateField(null=True, blank=True)  # Allow null values
    gender = models.CharField(max_length=10,blank=True)
    
    def __str__(self):
        return self.user.username

# Create member profile automatically that can be updated later.

def create_profile(sender,instance,created,**kwargs):
    if created:
        user_profile=Profile(user=instance)
        user_profile.save()
# Automate profile 

post_save.connect(create_profile,sender=User)

