from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.Products_List.as_view()),
    path('<int:pk>/', views.Products_Detail.as_view()),
    ]    