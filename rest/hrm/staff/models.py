from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    department = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Users(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    qualification = models.CharField(max_length=200)
    DOB = models.DateTimeField
    state_of_origin = models.CharField(max_length=200)
    MARITAL_STATUS_CHOICES = (
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
    )
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, default='Single')
    BLOOD_GROUP_CHOICES = (
        ('apos', 'A+'),
        ('aneg', 'A-'),
        ('bpos', 'B+'),
        ('bneg', 'B-'),
        ('opos', 'O+'),
        ('oneg', 'O-'),
        ('abpos', 'AB+'),
        ('abneg', 'AB-'),
        ('unspecified', '-'),
    )
    blood_group = models.CharField(max_length=15, choices=BLOOD_GROUP_CHOICES, default='A+')
    BVN = models.CharField(max_length=15)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstName



