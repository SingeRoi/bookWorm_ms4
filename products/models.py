from django.db import models
from django.db.models import Avg
from profiles.models import UserProfile

# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    isbn = models.CharField(max_length=254, null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=254, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    format = models.CharField(max_length=254, null=True)
    currency = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    book = models.ForeignKey('Product', null=True, blank=True, on_delete=models.SET_NULL)
    chapter = models.CharField(max_length=254)
    name = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.CharField(max_length=254, null=True)
    translator = models.CharField(max_length=254, null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    context = models.TextField(null=True, blank=True)
    modalcode = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.sku

class UserRatings(models.Model):
    book = models.ForeignKey('Product', null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.SET_NULL, related_name='user_rating')
    user_rating = models.DecimalField(max_digits=6, decimal_places=2, default=0)


    def __str__(self):
        return self.user_rating
