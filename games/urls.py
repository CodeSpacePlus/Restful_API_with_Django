from django.urls import path
# from django.conf.urls import url
from games import views


urlpatterns = [
    path('games/', views.game_list),
    path('games/<int:pk>/', views.game_detail),

    """
    # **Uncomment if you're planning on using Django 1.11 or lower**
    
    url(r'^games/$', views.game_list),
    url(r'^games/(?P<pk>[0-9]+)/$', views.game_detail),
    """
]
