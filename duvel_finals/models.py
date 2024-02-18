from django.db import models

# Create your models here.
class DuvelCollection(models.Model):
    name = models.CharField(max_length = 20)
    year = models.IntegerField()
    photo = models.CharField(max_length = 50)
    price = models.CharField(max_length = 10)