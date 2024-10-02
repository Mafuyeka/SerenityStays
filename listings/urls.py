from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listing/', views.property_list, name='property_list'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('property/<int:pk>/book/', views.book_property, name='book_property'),
]
