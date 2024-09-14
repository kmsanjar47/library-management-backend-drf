from django.urls import path
from .views import UserRegistrationView, CustomAuthToken

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', CustomAuthToken.as_view(), name='user_login'),
]
