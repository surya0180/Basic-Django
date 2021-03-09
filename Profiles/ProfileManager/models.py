from django.db import models

# Create your models here.

class Stu(models.Model):
    firstname =  models.CharField(max_length=150)
    lastname =  models.CharField(max_length=150)
    image = models.ImageField(upload_to='pics')