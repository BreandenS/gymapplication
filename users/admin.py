from django.contrib import admin
from .import models
from django.contrib.auth.models import User

admin.site.register(models.Profile)

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