"""rant_box URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from .views import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rant-posts/', include('rant_post.urls')),
    path('login/', CustomAuthToken.as_view()),
    path('signup/', include('signup.urls')),
    path('generate-report/', include('reportapp.urls'))
]
