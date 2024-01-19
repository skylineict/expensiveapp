from django.contrib import admin
from .models import Register

# Register your models here.

# Register your models here.


@admin.register(Register)
class AdminRegister(admin.ModelAdmin):
    list_display = ['full_name', 'username', 'email']
    
