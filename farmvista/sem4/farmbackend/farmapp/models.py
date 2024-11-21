from django.db import models

# Create your models here.

class USER(models.Model):
    name=models.CharField(max_length=100)
    ph_number=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    passward=models.CharField(max_length=15)

class ADMIN(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    passward=models.CharField(max_length=15)

class PRODUCT(models.Model):
    name=models.CharField(max_length=100)   
    price=models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')  
    categorie = models.CharField(max_length=100)

class APPOINTMENT(models.Model):
    admin_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    appointment_date = models.DateTimeField()
    address = models.CharField(max_length=100)

class APPOINTMENT_DETAILS(models.Model):
    admin_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    appointment_date = models.DateTimeField()
    soil_condition = models.CharField(max_length=200)
    soil_fertility = models.IntegerField()
    recommended_crop = models.CharField(max_length=200)
    nutrients_needed = models.CharField(max_length=1000)
    other_suggestions = models.CharField(max_length=1000)
    