from django.urls import path
from . import views

urlpatterns = [
    path('artwork', views.ArtworkListCreate.as_view(), name='artwork-list-create'),
    path('artwork/<int:id>/', views.ArtworkDetailUpdateDelete.as_view(), name='artwork-detail-update-delete'),
]