from django.db import models
from django.contrib.auth.models import AbstractUser

class Gender(models.Model):
    class Meta:
        db_table = 'tbl_genders'

    gender_id = models.BigAutoField(primary_key=True)
    gender = models.CharField(blank=False, max_length=55)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.gender

class User(AbstractUser):
    class Meta:
        db_table = 'tbl_users'

    user_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(blank=False, max_length=55)
    middle_name = models.CharField(blank=True, max_length=55)
    last_name = models.CharField(blank=False, max_length=55)
    age = models.IntegerField(blank=False)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    birthdate = models.DateField(blank=False)
    username = models.CharField(blank=False, max_length=55, unique=True)
    password = models.CharField(blank=False, max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)