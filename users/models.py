from django.db import models
from django.contrib.auth.models import User

class MemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)  # Nullable field
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female')))
    phone_number = models.CharField(max_length=15)
    bank_account_number = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

    
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MemberProfile

@receiver(post_save, sender=User)
def handle_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a new MemberProfile when a User is created
        MemberProfile.objects.create(user=instance)
        print(f'Created profile for new user: {instance.username}')
    else:
        # Update the MemberProfile if it already exists
        try:
            profile = instance.memberprofile
            profile.save()  # Save any updates to the MemberProfile
            print(f'Updated profile for existing user: {instance.username}')
        except MemberProfile.DoesNotExist:
            # Create the profile if it does not exist
            MemberProfile.objects.create(user=instance)
            print(f'Created profile for existing user: {instance.username}')

