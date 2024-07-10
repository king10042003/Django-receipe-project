from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)  # Fixed typo: 'max_lenght' to 'max_length'
    age = models.IntegerField()  # Fixed typo: 'IntegerFieldO' to 'IntegerField'
    email = models.EmailField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    image = models.ImageField()  # ImageField should have 'upload_to' parameter
    file = models.FileField()



class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)


    def __str__(self) -> str:
        return self.car_name