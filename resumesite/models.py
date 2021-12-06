from django.db import models

# Create your models here.
class post(models.Model): 
    name = models.CharField( max_length = 50 , null= True)
    email = models.CharField( max_length = 80 , null= True)
    subject = models.CharField( max_length = 50 , null= True)
    message = models.TextField( null= True)


class profile(models.Model):
    name = models.CharField(max_length = 50 , null= True)


class skills(models.Model):
    html = models.IntegerField()
    js = models.IntegerField()
    css = models.IntegerField()
    react = models.IntegerField()
    python = models.IntegerField()
    django = models.IntegerField()
    ps = models.IntegerField()
    bootstrap = models.IntegerField()

    