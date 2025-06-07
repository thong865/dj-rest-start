from django.urls import path
from .views import auth_jwt_urls_views

urlpatterns = [
    path('auth_jwt/', auth_jwt_urls_views, name='auth_jwt_urls_views'),
]