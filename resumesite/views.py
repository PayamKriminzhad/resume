from django.shortcuts import render
from .models import post, profile, skill, experience, education
# from kavenegar import *
# import requests
# import json


def home(request):
    profile_1 = profile.objects.first()

    skill_1 = skill.objects.all()

    experience_1 = experience.objects.all()

    education_1 = education.objects.all()



#send message by kavenegar api - start
    if request.method == "POST":
        post.objects.create(name = request.POST.get('name'), email=request.POST.get('_replyto'), subject=request.POST.get('subject') ,message=request.POST.get('message') , )

        # api = KavenegarAPI('6C746E59647348796A59584731516C4F6C6B7A36734D6A6D394769574B365A7467565148374D59494E35453D')
        # params = { 'sender' : '1000596446', 'receptor': '09336522009', 'message' :'name:%s \n' % request.POST.get('name') + 'message:%s' % request.POST.get('message') } 

        # response = api.sms_send(params) 
#send message by kavenegar api - end

    # response = requests.get('http://worldtimeapi.org/api/timezone/Europe/Amsterdam')
    # r = response.json()["datetime"]

    context = {
        'profile' : profile_1,
        'skill' : skill_1,
        'experience' : experience_1,
        'education' : education_1,
        # 'time' : r[11:19],
    }
    return render(request, 'index.html', context)
