from django.urls import path
from . import views

app_name = 'rant_post'

urlpatterns = [
    path('', views.RantPostListCreateView.as_view(), name='rant-post'),
    path('<int:pk>/', views.RantPostRetrieveUpdateDestroyView.as_view(), name='rant-post-detail'),
    path('my-rants/', views.UserPostsView.as_view(), name='user-posts'),
]
