from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=20)
    uname = models.CharField(max_length=20)
    uemail = models.EmailField()
    ucontact = models.CharField(max_length=20)
    uans = models.CharField(max_length= 100, default="null")


