from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('facial/', include(('facial.urls', 'facial'), namespace='facial'))
]
