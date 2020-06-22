from django.db import models


# Create your models here.
class user(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=12, null=False)


class details(models.Model):
    username = models.ForeignKey(user, on_delete=models.CASCADE)
    password = models.CharField(max_length=12)
    gender = models.CharField(max_length=6)
    email = models.EmailField(max_length=30)
    bdate = models.DateField()
    mono = models.CharField(max_length=13)


class folder(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200)