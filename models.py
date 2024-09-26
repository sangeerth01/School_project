from django.db import models 

# Create your models here.
class Add(models.Model):
   name = models.CharField(max_length=20)
   age = models.IntegerField(max_length=20)
   email = models.EmailField(max_length=20)
   
