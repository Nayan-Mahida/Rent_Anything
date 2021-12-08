from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import admin

PRODUCT_CATEGORY = (
    ('Electronic', 'Electronic'),
    ('Car', 'Car'),
    ('Outdoor', 'Outdoor'),
    ('Maintenance', 'Maintenance'),
    ('Book', 'Book'),
    ('Other', 'Other'),
)

class items(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    img = models.ImageField(default='img0.png', blank=True, null=True)
    rate = models.DecimalField(max_digits=9, decimal_places=2)
    phone = models.DecimalField(max_digits=10, decimal_places=0)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zip = models.DecimalField(max_digits=5, decimal_places=0)
    quantity = models.IntegerField()
    category = models.CharField(max_length=20, blank=True, choices=PRODUCT_CATEGORY)

    def __str__(self):
        return self.description

    def __set_name__(self, owner, name):
        return self.name

    def __iadd__(self, other):
        return self.address


