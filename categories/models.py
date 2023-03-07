from django.db import models

from django.shortcuts import reverse, get_object_or_404
# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='categories/images', null=True, blank=True)

    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_all_categories(cls):
        return cls.objects.all()

    @classmethod
    def get_counts(cls):
        print("get_counts ", cls.count())
        return cls.objects.all().count() - 1

    @classmethod
    def get_spesific_category(cls, id):
        try:
            category = cls.objects.get(pk=id)
            print(category)
            return category

        except Exception as e:
            return None

    def get_image_url(self):
        # print("inseife ", self.image.url )
        return f"media/{self.image}"

    def get_cat_name(self):
        return self.name

    def get_delete_url(self):
        return reverse('delete_cat', args={self.id})

    def get_edit_url(self):
        return reverse('edit_cat', args={self.id})

    def get_details_url(self):
        return reverse('show_cat', args={self.id})
