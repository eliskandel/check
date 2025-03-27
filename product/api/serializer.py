from rest_framework import serializers
from ..models import Product,Rating
from user.models import User
from rest_framework.exceptions import PermissionDenied

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username']
class ProductSerializer(serializers.ModelSerializer):
    seller=UserSerializer()
    class Meta:
        model=Product
        fields='__all__'

class RatingSerializer(serializers.ModelSerializer):
    product=ProductSerializer()
    class Meta:
        model=Rating
        fields='__all__'




class ProductCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Product
        fields=['name','price','stock']
        
    def create(self, validated_data):
        request=self.context['request']
        if request.user.category == 'seller':
            product=Product.objects.create(**validated_data, seller=request.user)
            return product
        else:
            raise PermissionDenied("Seller can only make product")
        
