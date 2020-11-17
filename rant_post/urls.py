from django.urls import path
from . import views

urlpatterns = [
    path('', views.RantPostListCreateView.as_view(), name='rant-post'),
    path('<int:pk>', views.RantPostRetrieveUpdateDestroyView.as_view(), name='rant-post-retrieve')
]
