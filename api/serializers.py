from rest_framework import serializers
from .models import ClassEntity

class ClassSerializer(serializers.Serializer):
    classname = serializers.CharField(max_length=255)
    details = serializers.CharField(max_length=None)
    time = serializers.DateTimeField()
    status = serializers.BooleanField()

    def create(self, validated_data):
        return ClassEntity(**validated_data)