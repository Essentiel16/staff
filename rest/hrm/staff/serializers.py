from rest_framework import serializers
from .models import Users, Department


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
