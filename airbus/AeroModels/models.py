from django.db import models
from django.utils import timezone
# Create your models here.

class Societe(models.Model):
    address = models.CharField(max_length=300)

    def __str__(self):
        return str(self.id) + ' ' + self.address

class ModelAvion(models.Model):
    Avion_CHOICES = [
        ('melitairie', 'Melitairie'),
        ('airplane', 'Airplane'),
    ]
    name = models.CharField(max_length=150)
    typeAir = models.CharField(max_length=150, choices=Avion_CHOICES, default='airplane')
    created_at = models.DateField(default=timezone.now)
    typeOfFuel = models.CharField(max_length=150)
    capacityOfFuel = models.PositiveIntegerField()
    Altitude = models.PositiveIntegerField()
    societe = models.ForeignKey(Societe, on_delete=models.CASCADE, related_name='societe_avion')

    def __str__(self):
        return self.name