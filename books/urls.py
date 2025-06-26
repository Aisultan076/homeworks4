from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookPostView,
)

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('post/', BookPostView.as_view(), name='book_post'),
]
