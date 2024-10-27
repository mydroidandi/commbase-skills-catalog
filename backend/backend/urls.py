# Imports
from django.contrib import admin
from django.urls import path, include  # 'include' is to add another URLconf
from api.views import CreateUserView  # View in app api/views.py
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  # JWT token views

# URL configuration for backend project
# The 'url patterns' list routes URLs to views. For more information visit: https://docs.djangoproject.com/en/5.1/topics/http/urls/
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),  # Link the URLs in backend/api/urls.py into this file
]
