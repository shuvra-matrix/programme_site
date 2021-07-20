from django.db import models

# Create your models here.
class Python(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500,unique=False)
    options1 = models.CharField(max_length=100,unique=False)
    options2 = models.CharField(max_length=100,unique=False)
    options3 = models.CharField(max_length=100,unique=False)
    options4 = models.CharField(unique=False, max_length=100)
    ans = models.CharField(unique=False,max_length=50)


class User(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=60,unique=False)
    email = models.EmailField(max_length=254,unique=False)
    password = models.CharField(max_length=50,unique=False)
    otp = models.IntegerField(max_length=10,unique=False)
    validation = models.CharField(max_length=4,unique=False)

    
