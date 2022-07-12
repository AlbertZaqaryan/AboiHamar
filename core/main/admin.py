from django.contrib import admin
from .models import Category, Prod, Brand

# Register your models here.

admin.site.register(Category)
admin.site.register(Prod)
admin.site.register(Brand)


