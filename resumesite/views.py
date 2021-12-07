from django.shortcuts import render
from .models import post , profile, skills
import requests
import json


def home(request):
    profile_1 = profile.objects.first()

    skills_1 = skills.objects.first()


    if request.method == "POST":
        post.objects.create(name = request.POST.get('name') ,email=request.POST.get('_replyto') ,subject=request.POST.get('subject') ,message=request.POST.get('message') , )

    response = requests.get('http://worldtimeapi.org/api/timezone/Europe/Amsterdam')
    r = response.json()["datetime"]

    context = {
        'profile' : profile_1,
        'skills' : skills_1,
        'time' : r[11:19],
    }
    return render(request , 'index.html' , context)
