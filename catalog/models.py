# models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MuscleGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # e.g., Strength, Cardio, Flexibility
    target_muscles = models.ManyToManyField(MuscleGroup)
    equipment = models.CharField(max_length=100, blank=True, null=True)  # Optional, if equipment is required
    video_url = models.URLField(blank=True, null=True)  # Link to instructional video
    image = models.ImageField(upload_to='exercise_images/', blank=True, null=True)  # Exercise image

    def __str__(self):
        return self.name



