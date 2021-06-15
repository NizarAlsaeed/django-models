from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models
# Create your views here.

class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = models.Snack

class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = models.Snack
