from django.db import models

# Create your models here.
class Sec(models.Model):
    sec = models.CharField(max_length = 200)
    key = models.CharField(max_length=200)
    crypto_gr_key = models.CharField(max_length=200)