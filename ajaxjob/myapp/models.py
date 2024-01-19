from django.db import models

# Create your models here.


class Register(models.Model):
    uplaod_img = models.ImageField(upload_to="uplaods")
    email = models.CharField(max_length=40)
    username = models.CharField(max_length=30)
    full_name = models.CharField(max_length=30)
    joindate = models.DateField(auto_now_add=True)
