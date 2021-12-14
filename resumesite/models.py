from django.db import models

# Create your models here.
class post(models.Model): 
    name = models.CharField( max_length = 50 , null= True)
    email = models.CharField( max_length = 80 , null= True)
    subject = models.CharField( max_length = 50 , null= True)
    message = models.TextField( null= True)


class profile(models.Model):
    name = models.CharField(max_length = 50 , null= True)


class skill(models.Model):
    title = models.CharField(max_length = 50)
    percent = models.IntegerField()

class experience(models.Model):
    title1 = models.CharField(max_length = 50)
    title2 = models.CharField(max_length = 50)
    discribtion = models.CharField(max_length = 200)


class education(models.Model):
    title1 = models.CharField(max_length = 50)
    title2 = models.CharField(max_length = 50)
    title3 = models.CharField(max_length = 50)
    discribtion = models.CharField(max_length = 200)
