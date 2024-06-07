from django.utils import timezone
from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    created_ad = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=300)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_ad = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.title
