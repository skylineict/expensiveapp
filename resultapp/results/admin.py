
from django.contrib import admin
from .models import Resultstudent,Pinverification, Allstudent,Schoolstudent
# Register your models here.
@admin.register(Resultstudent)
class Adminmod(admin.ModelAdmin):
    list_display = ['Grade','mystudentname','school','examyear','Subject']
    fieldsets = (
       ('Create Result', {
           "fields": ('Grade','mystudentname','school','examyear','Subject')
       })

       
   ),

@admin.register(Pinverification)
class Adminmodel(admin.ModelAdmin):
    list_display = ('Pin'),






@admin.register(Allstudent)
class Adminmod(admin.ModelAdmin):
    list_display = ('sitnumber','first_name','last_name')





@admin.register(Schoolstudent)
class Adminmodels(admin.ModelAdmin):
    list_display = ('schoolexam'),
