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

class Address(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    address1=models.CharField(max_length=200,blank=True)
    address2=models.CharField(max_length=200,blank=True)
    city=models.CharField(max_length=200,blank=True)
    state=models.CharField(max_length=200,blank=True)
    zipcode=models.CharField(max_length=200,blank=True)
    country=models.CharField(max_length=200,blank=True)
    

class BankDetail(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=20)
    routing_number = models.CharField(max_length=20)
    account_type = models.CharField(max_length=20)

class BioDetail(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    fitness_level = models.CharField(max_length=50)
    goals = models.TextField()
    medical_conditions = models.TextField()

class Membership(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    membership_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20)

class Workout(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    workout_date = models.DateField()
    workout_type = models.CharField(max_length=50)
    duration = models.DurationField()
    calories_burned = models.FloatField()

class Payment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
