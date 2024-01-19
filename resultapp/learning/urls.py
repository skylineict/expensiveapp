from django.urls import path
from .views import Learn

urlpatterns = [
    path('', Learn.as_view(), name='learn' )
]
