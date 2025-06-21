from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='all_products'),
    path('tag/<int:tag_id>/', views.product_list, name='product_by_tag'),
]
