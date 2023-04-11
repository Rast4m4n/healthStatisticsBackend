from .models import *
from rest_framework import viewsets, permissions
from .serializers import *


class UserHealthViewSet(viewsets.ModelViewSet):
    queryset = UserHealth.objects.all()
    permissions_classess = [
        permissions.AllowAny
    ]
    serializer_class = UserHealthSerializer
