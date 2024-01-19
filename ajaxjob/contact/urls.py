from django.urls import path
from .views import contactus


urlpatterns = [
    path('register', contactus, name="inex")



]
