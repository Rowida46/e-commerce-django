from django.db import models

# Create your models here.

from djmoney.models.fields import MoneyField


class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    # images = models.ImageField(upload_to='images/', default=None)
    rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', default=213)
    num_stars = models.IntegerField(default=1, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    stock = models.IntegerField(default=10 , blank=True)

    def __str__(self):
        return self.title

