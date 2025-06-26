from django.urls import path
from .views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('tag/<int:tag_id>/', ProductListView.as_view(), name='product_list_by_tag'),
]
