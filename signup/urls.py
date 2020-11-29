from django.urls import path
from .views import UserRegistrationView
app_name = 'user_signup'

urlpatterns = [
    path('', UserRegistrationView.as_view(), name='user_registration')
]