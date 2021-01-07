from django.urls import path
from . import views

urlpatterns = [
    path('', views.export_rants),
    path('json/', views.export_rants_as_json)
]