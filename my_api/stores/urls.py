from django.urls import path
from .views import StoreAPIView, ProductAPIView, StoreProductAPIView

urlpatterns = [
    path('stores/', StoreAPIView.as_view()),
    path('stores/<int:pk>/', StoreAPIView.as_view()),
    path('stores/<int:pk>/products/', StoreProductAPIView.as_view()),
    path('products/', ProductAPIView.as_view()),
    path('products/<int:pk>/', ProductAPIView.as_view()),
]