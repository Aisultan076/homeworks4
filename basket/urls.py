from django.urls import path
from .views import (
    BasketListView,
    BasketCreateView,
    BasketUpdateView,
    BasketDeleteView,
)

urlpatterns = [
    path('', BasketListView.as_view(), name='basket_list'),
    path('create/', BasketCreateView.as_view(), name='basket_create'),
    path('<int:pk>/update/', BasketUpdateView.as_view(), name='basket_update'),
    path('<int:pk>/delete/', BasketDeleteView.as_view(), name='basket_delete'),
]
