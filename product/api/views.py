from rest_framework.response import Response
from rest_framework.generics import (
    GenericAPIView,
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView
)
from .serializer import RatingSerializer,ProductCreateSerializer,ProductSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from ..models import Product,Rating
from .pagination import ListProductPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# from rest_framework.exceptions import PermissionDenied
# Create your views here.
##Product
class ProductCreateView(CreateAPIView):
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAuthenticated]  # Use IsAuthenticated to ensure the user is logged in
    authentication_classes = [TokenAuthentication]  # Use TokenAuthentication for token-based auth

    
        
class ProductListView(ListAPIView):
    serializer_class=ProductSerializer
    permission_classes=[TokenAuthentication]
    authentication_classes=[IsAuthenticated]
    pagination_class=ListProductPagination
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    search_fields=['name','seller__username']
    queryset=Product.objects.all()