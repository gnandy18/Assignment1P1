from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class Request(models.Model):
    bag_type = (
        ('Chicken', 'Chicken Bag'),
        ('Tuna', 'Tuna Bag'),
        ('Veg', 'Veg Bag'),

    )
    approval_type = (
        ('New', 'New'),
        ('Ready', 'Ready'),
        ('Delivered', 'Delivered'),
    )
    # nuid = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, )
    username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, )
    food_allergy = models.TextField()
    request_date = models.DateField(default=timezone.now)
    additional_request = models.TextField()
    bag = models.CharField(max_length=20,
                           choices=bag_type,
                           default='Chicken')
    status = models.CharField(max_length=10,
                              choices=approval_type,
                              default='New')

    def __str__(self):
        return f"{self.username} - {self.status} - {self.request_date}"


class Item(models.Model):
    item_name = models.CharField(max_length=150, blank=False, null=False, default=' ', unique=True)
    item_quantity = models.IntegerField(blank=False, null=False)
    item_description = models.TextField()


    def __str__(self):
        return self.item_name
