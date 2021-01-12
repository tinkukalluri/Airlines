from django.db import models
from django.db.models.fields import CharField
# Create your models here.

# class flights(models.Model):
#     origin=models.CharField(max_length=64)
#     destination=models.CharField(max_length=64)
#     duration=models.IntegerField()
#     def __str__(self):
#         return f"{self.id}:{self.origin} to {self.destination} in duration {self.duration}"

class airports(models.Model):
   
    city=models.CharField(max_length=64)
    code=models.CharField(max_length=64)
    def __str__(self):
        return f"{self.city} ({self.code})"
        

class flights(models.Model):
    origin=models.ForeignKey(airports,on_delete=models.CASCADE,related_name="departures")
    destination=models.ForeignKey(airports,on_delete=models.CASCADE,related_name="arrivals")
    duration=models.IntegerField()
    def __str__(self):
        return f"{self.origin} to {self.destination} in {self.duration}min"


class passengers(models.Model):
    first=models.CharField(max_length=64)
    last=models.CharField(max_length=64)
    flights6=models.ManyToManyField(flights,blank=True,related_name="passenger")
    def __str__(self):
        return f"{self.first} {self.last} "




