from django.db import models
from user.models import User
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.PositiveIntegerField(default=0)
    seller=models.ForeignKey(User,on_delete=models.CASCADE,related_name="product")
    stock=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Rating(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rating')
    buyer=models.ForeignKey(User,on_delete=models.CASCADE, related_name='ratin')
    rating=models.PositiveIntegerField(choices=((1,'1 star'),(2,'2 star'), (3,'3 star'), (4, '4 star'), (5, '5 star')))
    review=models.TextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('buyer', 'product') 

    def __str__(self):
        return f'{self.buyer}\'s {self.rating}'