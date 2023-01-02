from django.urls import path, include
from . import views


urlpatterns = [
    # path('facial/', include('facial.urls'))
    # path('open_door/', views.ListUsers.as_view()),
    path('open_door_test/', views.door_test, name='door_test.facial'),
]
