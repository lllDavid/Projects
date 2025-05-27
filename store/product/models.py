from django.db import models
from django.contrib.postgres.fields import ArrayField


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categories = ArrayField(models.CharField(max_length=50), default=list)
    metadata = models.JSONField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
    
