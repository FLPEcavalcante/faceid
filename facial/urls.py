from django.urls import path

from . import views


urlpatterns = [
    path('open-door/', views.OpenDoorView.as_view(), name='open-door'),
]
