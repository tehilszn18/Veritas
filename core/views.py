#from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ApplicationView(TemplateView):
    template_name= 'applications.html'

class FeesView(TemplateView):
    template_name= 'fees.html'

class ResultView(TemplateView):
    template_name= 'results.html'

class FacultiesView(TemplateView):
    template_name= 'faculties.html'

class SraView(TemplateView):
    template_name= 'sra.html'
