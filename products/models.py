from django.db import models
from django.shortcuts import reverse, get_object_or_404

# Create your models here.

from djmoney.models.fields import MoneyField
from categories.models import Categories
from django.utils.text import slugify


class Products(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default="", null=False)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to='products/images', null=True, blank=True)

    rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    price = MoneyField(max_digits=14, decimal_places=2,
                       default_currency='USD', default=213)

    num_stars = models.IntegerField(default=1, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    stock = models.IntegerField(default=10, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True,
                                 related_name='category_posts')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_image_url(self):
        # print("inseife ", self.image.url )
        print("inseife ", self.image)
        return f"media/{self.image}"

    def get_title(self):
        return self.title

    def get_delete_url(self):
        return reverse('delete_product', args={self.id})

    def get_edit_url(self):
        return reverse('edit_product', args={self.id})

    def get_spefic_product_by_slug(self):

        try:
            return reverse('productDetails', args={self.slug})
        except Exception as e:
            return None

    def get_spefic_product(self):
        try:
            return reverse('productDetails', args={self.id})
        except Exception as e:
            return None

    @classmethod
    def get_product(cls, id):
        try:
            return get_object_or_404(cls, pk=id)
        except Exception as e:
            return None

    @classmethod
    def get_all_products(cls):
        return cls.objects.all()

    @classmethod
    def get_products_count(cls):
        return cls.objects.all().count()

    @classmethod
    def filter_products(cls, title):
        try:
            res = Products.objects.filter(title == title)
            return res
        except Exception as e:
            return None
