from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BrandModel(models.Model):
    name = models.CharField(max_length = 15)
    
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
class CarModel(models.Model):
    car_name = models.CharField(max_length=30)
    car_price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/')
    user = models.ManyToManyField(User, blank=True)
    
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.car_name


class Comment(models.Model):
    nam = models.CharField(max_length=30)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    cars = models.ForeignKey(CarModel, on_delete=models.CASCADE, blank=True, null=True, related_name='comments')
    
    def __str__(self) -> str:
        return self.nam