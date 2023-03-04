from django.urls import path, include
from . import views

url_patterns_user = [
    path('create/', views.create_user),
    path('login/', views.login),
    path('list/', views.list_user),
]

urlpatterns = [
    path('user/', include(url_patterns_user)),
]