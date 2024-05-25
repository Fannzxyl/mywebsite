from django.db import models

# Create your models here.
from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='food_images')

    def __str__(self):
        return self.name