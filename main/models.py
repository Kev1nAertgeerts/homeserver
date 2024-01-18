from django.db import models

# Create your models here.

####diepvries####
class Diepvries(models.Model):
    pot_nummer = models.IntegerField(unique = True)
    omschrijving = models.CharField(max_length = 50)
    personen = models.CharField(max_length = 2)
    datum = models.DateField(auto_now = True)
