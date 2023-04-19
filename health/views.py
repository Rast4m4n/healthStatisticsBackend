from rest_framework import permissions, viewsets

from .models import *
from .serializers import *


class HealthViewSet(viewsets.ModelViewSet):
    queryset = Health.objects.all()
    permissions_classess = [
        permissions.AllowAny
    ]
    serializer_class = HealthSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions_classess = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
