from django.contrib import admin

# Register your models here.
from .models import Pet

# @admin.register is a decorator for registering your ModelAdmin classes
@admin.register(Pet)
class pet_Admin(admin.ModelAdmin):
    list_display = ['name','species','breed','age','sex']
    