from django.urls import path
from . import views

urlpatterns  = [
    path('', views.SnackListView.as_view(), name='snack_list'),
    path('<int:pk>/', views.SnackDetailView.as_view(), name='snack_detail'),
]
