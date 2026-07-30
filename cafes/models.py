from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.



class Barrio(models.Model):
    name = models.CharField(max_length=50, unique=True)
    comuna = models.IntegerField()

    slug = models.SlugField(max_length=100, unique=True, null=True)
    
    def __str__(self):
        return f"{self.name} (Comuna {self.comuna})"

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    
class Cafe(models.Model):

    class Meta:
          ordering = ['name']
          
    
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE, related_name='cafes')
    
    
    has_good_medialunas = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    recommendation_count = models.IntegerField(default = 0)

    tags = models.ManyToManyField(Tag, related_name='cafes')


    def __str__(self):
        return f"{self.name} ({self.barrio})"
    
    @property
    def review_count(self) -> int:   
        return self.reviews.count()
        

class Reviewer(models.Model):
    name = models.CharField(max_length=100)
    join_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.name} ({self.join_date})"
     
class Review(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    rating = models.IntegerField(
          validators=[MinValueValidator(1), MaxValueValidator(5)]
      )

    def __str__(self):
        return f"Review for {self.cafe.name} by {self.reviewer.name}"
    
class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    is_vegan = models.BooleanField(default=False)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name='dishes')

    def __str__(self):
        return f"{self.name} £{self.price} ({self.cafe.name})"
    
     

