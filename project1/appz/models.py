from django.db import models

# Create your models here.
class register(models.Model):
    schlname=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.IntegerField()
    password=models.CharField(max_length=50)
    file=models.FileField()
    
     
    def __str__(self):
        return self.schlname
    
class formpage(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    phone_no=models.IntegerField()
    
    
class form21(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=150)
    phone=models.IntegerField()
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    
class form3(models.Model):
    hosp_name=models.CharField(max_length=100)
    hosp_dict=models.CharField(max_length=100)
    hosp_phone=models.IntegerField()
    hosp_address=models.CharField(max_length=100)
    
    
class modelss(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    
    
    
    
    