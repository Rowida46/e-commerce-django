from django.db import models

# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=100, null=True,  blank=True)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    num_stars = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
