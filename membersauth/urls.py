from django.urls import path
from .views import Registrationsview


urlpatterns = [
    path("", Registrationsview.as_view(), name="register")


]
