from rest_framework import serializers
from .models import *


class UserHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHealth
        fields = '__all__'