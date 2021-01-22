from django.db import models

# Create your models here.


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    email = models.CharField(max_length=500)
    phone = models.IntegerField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)


class Donor(models.Model):
  
    BLOOD_CHOICES = (
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        )
    GENDER_CHOICES = (('MALE', 'Male'), ('FEMALE', 'Female'))
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=70,choices=GENDER_CHOICES)
    dob = models.DateField()
    bloodgroup = models.CharField(max_length=50 ,choices=BLOOD_CHOICES)

    def __str__(self):
        return self.name 
