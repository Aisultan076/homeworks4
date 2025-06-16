from django.urls import path
from . import views

urlpatterns = [
    path('', views.basket_list, name='basket_list'),
    path('create/', views.basket_create, name='basket_create'),
    path('update/<int:pk>/', views.basket_update, name='basket_update'),
    path('delete/<int:pk>/', views.basket_delete, name='basket_delete'),
]
