from django.contrib import admin
from .import models
from django.contrib.auth.models import User

admin.site.register(models.Profile)
admin.site.register(models.Address)
admin.site.register(models.Payment)
admin.site.register(models.Membership)
admin.site.register(models.BankDetail)
admin.site.register(models.BioDetail)
admin.site.register(models.Workout)
# Mix profile and user info
class ProfileInline(admin.StackedInline):
    model= models.Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model= User
    field =['username','first_name','last_name','email']
    inlines=[ProfileInline]

# Unregister the old     
admin.site.unregister(User)

# register 
admin.site.register(User,UserAdmin)