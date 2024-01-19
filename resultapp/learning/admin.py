from django.contrib import admin
from .models import Reporter, Article

# Register your models here.
@admin.register(Reporter)
class Admin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']




@admin.register(Article)
class Admin(admin.ModelAdmin):
    list_display = ['publisher', 'headline', 'pub_date']