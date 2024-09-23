from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import DashboardView, NewProfile, UserRegistration
app_name = 'account'

urlpatterns = [
    path('accounts/', LoginView.as_view(template_name='accounts.html'), name='accounts'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('update_profile/<pk>', NewProfile.as_view(), name='update_profile'), 
    path('newaccount/', UserRegistration.as_view(), name='newaccount'),   
]

# dont forget pk
