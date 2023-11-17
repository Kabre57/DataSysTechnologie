from django.contrib import admin
from .models import products
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'actif', 'slug')
    
admin.site.register(products, AdminProduct)