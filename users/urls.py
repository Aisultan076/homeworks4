from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    LogoutView,
    UserListView,
)

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('list/', UserListView.as_view(), name='user_list'),
]
