from django.contrib import admin
from django.db import models
from .models import ServiceCategory, ServiceProvider

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('name',)
    list_per_page = 20

@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ('shop_name', 'category', 'district', 'telephone')
    list_filter = ('category', 'district')
    search_fields = ('shop_name', 'address', 'description', 'services_offered')
    ordering = ('shop_name',)
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 20

