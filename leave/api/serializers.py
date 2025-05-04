from rest_framework import serializers
from ..models import Leave

from user.api.serializers import UserSerializer

class LeaveSerializer(serializers.ModelSerializer):
    user=UserSerializer(many=True)
    class Meta:
        model=Leave
        fields='__all__'

    
    