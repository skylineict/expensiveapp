from django.db import models
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, TemplateView, ListView
from dashapp.models import Post

# Create your views here.


class Registrationsview(ListView):
    model = Post
    template_name = "authapp/signup.html"
