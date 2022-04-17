from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LoginView, RegisterView


# These URLS are not accessible as this is the entry point.
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
