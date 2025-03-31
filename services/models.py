from django.db import models
from datetime import datetime

# Create your models here.

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Service Categories"

class ServiceProvider(models.Model):
    DISTRICT_CHOICES = [
    ("Islands", "Islands"),
    ("Kwai Tsing", "Kwai Tsing"),
    ("Sai Kung", "Sai Kung"),
    ("Tsuen Wan", "Tsuen Wan"),
    ("Tuen Mun", "Tuen Mun"),
    ("Yuen Long", "Yuen Long"),
    ("Wong Tai Sin", "Wong Tai Sin"),
    ("Sha Tin", "Sha Tin"),
    ("Tai Po", "Tai Po"),
    ("Kowloon City", "Kowloon City"),
    ("Kwun Tong", "Kwun Tong"),
    ("Sham Shui Po", "Sham Shui Po"),
    ("Yau Tsim Mong", "Yau Tsim Mong"),
    ("Central & Western", "Central & Western"),
    ("Eastern", "Eastern"),
    ("Southern", "Southern"),
    ("Wan Chai", "Wan Chai"),
    ("North", "North")
    ]

    category = models.ForeignKey(ServiceCategory, on_delete=models.DO_NOTHING, related_name='providers')
    shop_name = models.CharField(max_length=200)
    address = models.TextField()
    district = models.CharField(max_length=20, choices=DISTRICT_CHOICES)
    description = models.TextField()
    telephone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    services_offered = models.TextField(help_text="List of services offered, separated by commas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    
    def __str__(self):
        return f"{self.shop_name} - {self.get_district_display()}"

    class Meta:
        ordering = ['shop_name']
