from django.urls import path
from .views import (
    ProductCreateView,
    ProductListView,
    ProductRetrieveView,
    ProductUpdateView,
    ProductDeleteView
) 

urlpatterns = [
    path('create/',ProductCreateView.as_view()),
    path('',ProductListView.as_view()),
    path('<int:pk>/',ProductRetrieveView.as_view()),
    path('update/<int:pk>/',ProductUpdateView.as_view()),
    path('delete/<int:pk>/',ProductDeleteView.as_view())
]
