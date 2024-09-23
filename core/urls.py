from django.urls import path
from .views import HomeView, AboutView, ApplicationView, FeesView, ResultView, FacultiesView, SraView


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('about', AboutView.as_view(), name= 'about'),
    path('applications', ApplicationView.as_view(), name= 'applications'),
    path('fees', FeesView.as_view(), name= 'fees'),
    path('results', ResultView.as_view(), name= 'results'),
    path('faculties', FacultiesView.as_view(), name= 'faculties'),
    path('sra', SraView.as_view(), name= 'sra'),
   ]