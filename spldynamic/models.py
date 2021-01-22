from django.db import models
from django.contrib import admin

# Create your models here.
class product(models.Model):
    name= models.CharField(max_length=200)
    price= models.IntegerField()
    image= models.ImageField(upload_to='img/')

class productadmin(admin.ModelAdmin):
    list_display= ('name','price','image')

class people(models.Model):
    name= models.CharField(max_length=200)
    designation= models.CharField(max_length=50)
    image= models.ImageField(upload_to='img1/')

class peopleadmin(admin.ModelAdmin):
    list_display= ('name','designation','image')

