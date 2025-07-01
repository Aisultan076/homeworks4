from django.contrib import admin
from django.urls import path, include
from .views import *
from .views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('users.urls')),
    path('', MovieListView.as_view(), name='movie-list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movie/add/', MovieCreateView.as_view(), name='movie-add'),
    path('movie/<int:pk>/edit/', MovieUpdateView.as_view(), name='movie-edit'),
    path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie-delete'),
    path('movie/<int:pk>/comment/', CommentCreateView.as_view(), name='movie-comment'),
]
