from django.db import models

# Create your models here.
class Tour(models.Model):
    orgin_country = models.CharField(max_length=100)
    destination_country = models.CharField(max_length=100)
    nights = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"ID:{self.id}: {self.orgin_country} to {self.destination_country} for {self.nights} nights at ${self.price}"