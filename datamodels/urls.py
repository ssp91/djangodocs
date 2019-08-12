from datamodels.views import UserListView, UserActios
from django.urls import path

app_name = 'data_models'

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserActios.as_view(), name='user-list')
    
]