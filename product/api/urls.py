from django.urls import path
from .views import (
    ProductCreateView,
    ProductListView
) 

urlpatterns = [
    path('create/',ProductCreateView.as_view()),
    path('',ProductListView.as_view())
]
