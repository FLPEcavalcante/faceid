from django.urls import path

from . import views


urlpatterns = [
    path('open-door/', views.OpenDoorView.as_view(), name='open-door'),
    # path('delete-data/<int:pk>/delete/', views.ModelDelete.as_view(), name='delete'),
    path('delete_all/', views.OpenDoorView.as_view(), name='delete_all_data'),
]
