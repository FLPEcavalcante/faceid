from django.urls import path, include
from . import views


urlpatterns = [
    # path('facial/', include('facial.urls'))
    path('open_door/', views.ListUsers.as_view())
]
