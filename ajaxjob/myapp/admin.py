from django.contrib import admin
from django.db import models
from .models import Register

# Register your models here.
@admin.register(Register)
class AdminRegister(admin.ModelAdmin):
    pass