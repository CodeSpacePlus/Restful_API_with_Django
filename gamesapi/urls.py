from django.contrib import admin
from django.urls import path
from django.conf.urls import include

app_name = 'gamesapi'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('games.urls')),
]
