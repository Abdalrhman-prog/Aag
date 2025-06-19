from django.contrib import admin
from .models import Product, Category  # تأكد أنك أنشأت هذه النماذج في models.py

admin.site.register(Product)
admin.site.register(Category)
