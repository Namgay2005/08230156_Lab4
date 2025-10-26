from django.shortcuts import render
from .models import LearningJourney, AboutMe  # import your models

def index(request):
    journeys = LearningJourney.objects.all()  # get all entries
    return render(request, 'index.html', {'journeys': journeys})

def about_me(request):
    my_info = AboutMe.objects.first()  # assuming only one AboutMe entry
    return render(request, 'aboutMe.html', {'my_info': my_info})