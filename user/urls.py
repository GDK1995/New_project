from django.urls import path, include
from . import views

url_patterns_user = [
    path('create/', views.create_user),
    path('login/', views.login),
]

urlpatterns = [
    path('user/', include(url_patterns_user)),
]