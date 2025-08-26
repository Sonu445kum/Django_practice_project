from django.db import models

# Create your models here.
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Create Models for the Product 
class Product(models.Model):
    name=models.CharField(max_length=100)
    descriptions=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - ${self.price}"