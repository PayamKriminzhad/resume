from django.contrib import admin
from .models import post , profile, skill, experience, education
# Register your models here.


admin.site.register(post)
admin.site.register(profile)
admin.site.register(skill)
admin.site.register(experience)
admin.site.register(education)