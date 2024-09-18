# views.py
from django.shortcuts import render
from .models import Exercise

def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'catalogue/exercise_list.html', {'exercises': exercises})

def exercise_detail(request, pk):
    exercise = Exercise.objects.get(pk=pk)
    return render(request, 'catalogue/exercise_detail.html', {'exercise': exercise})
