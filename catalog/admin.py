# admin.py
from django.contrib import admin
from .models import Exercise, Category, MuscleGroup

admin.site.register(Exercise)
admin.site.register(Category)
admin.site.register(MuscleGroup)
