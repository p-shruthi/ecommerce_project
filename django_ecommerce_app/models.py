from django.db import models

# Create your models here.
class Product(models.Model):

    Pr_id = models.CharField(max_length=20)
    Pr_name = models.CharField(max_length=20)
    Pr_price = models.FloatField()
    Pr_image = models.ImageField()