from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from .serializers import LeaveSerializer
from ..models import 

class LeaveListView(ListAPIView):
    serializer_class=LeaveSerializer
    queryset=