from django.contrib import admin
from .models import Category, Product

admin.site.register([Category, Product])

