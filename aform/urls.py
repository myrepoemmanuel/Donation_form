from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('sendDonation/', views.processDonation, name='sendDonation'),
    # path('register', views.registerPage, name='register'),
    # path('login', views.loginPage, name='login'),
]