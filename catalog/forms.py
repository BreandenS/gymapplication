# forms.py
from django import forms
from .models import Exercise

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'category', 'target_muscles', 'equipment', 'video_url', 'image']
