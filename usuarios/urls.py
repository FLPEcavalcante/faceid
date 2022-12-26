from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),  # não funciona
    path('register/', views.register, name='register'),  # não funciona
    path('validate_register/', views.validate_register, name='validate_register'),
    path('validate_login/', views.validate_login, name='validate_login'),
    path('out/', views.out, name='out')
]
