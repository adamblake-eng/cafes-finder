from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Cafe(models.Model):

    class BarrioChoices(models.TextChoices):
          PALERMO = 'PAL', 'Palermo'
          SAN_TELMO = 'STL', 'San Telmo'
          RECOLETA = 'REC', 'Recoleta'
          LA_BOCA = 'BOC', 'La Boca'
          BELGRANO = 'BLG', 'Belgrano'
          NUÑEZ = 'NUZ', 'Nuñez'
          COLEGIALES = 'CLG', 'Colegiales'

    class Meta:
          ordering = ['-rating', 'name']  # Order by highest rating first, then by name
          
    barrio = models.CharField(
          max_length=3,
          choices=BarrioChoices.choices,
          default=BarrioChoices.PALERMO
      )
    rating = models.IntegerField(
          validators=[MinValueValidator(1), MaxValueValidator(5)]
      )
    
    has_good_medialunas = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.name} ({self.barrio}) ({self.rating})"
    
class Barrio(models.Model):
    name = models.CharField(max_length=50, unique=True)
    comuna = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} (Comuna {self.comuna})"
    
class Review(models.Model):
     cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
     comment = models.TextField()
     reviewer_name = models.CharField(max_length=100, default="Anonymous")

     def __str__(self):
        return f"{self.name.cafe}: {self.comment}, by {self,self.reviewer_name}"


