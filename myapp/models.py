from django.db import models

# Create your models here.
from django.db import models

class UserCredentials(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class StudentInfo(models.Model):
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.IntegerField()
    dep = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    adress = models.CharField(max_length=2550)
    nationality = models.CharField(max_length=255)
    rel = models.CharField(max_length=255)
    # Add more fields as per your requirements

    def __str__(self):
        return self.name


