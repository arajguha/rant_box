from django.urls import path
from . import views

app_name = 'rant_post'

urlpatterns = [
    path('', views.RantPostListCreateView.as_view(), name='rant-post'),
    path('<int:pk>/', views.RantPostRetrieveUpdateDestroyView.as_view(), name='rant-post-detail'),
    path('my-rants/', views.UserPostsView.as_view(), name='user-posts'),
    path('react/', views.PostReactView.as_view(), name='post-react'),
    path('reaction-status/<int:post_id>/', views.reaction_info_view, name='check-reaction-status'),
    path('feelings/', views.get_feelings_dict, name='feelings-dict'),
    path('categories/', views.get_categories_list, name='category-list')
]
