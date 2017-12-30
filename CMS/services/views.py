from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Service

class ServicePage(DetailView):
    template_name = 'services/service.html'
    model = Service
