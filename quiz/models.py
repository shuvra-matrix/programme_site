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

    
