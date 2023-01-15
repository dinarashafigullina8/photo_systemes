from rest_framework import serializers
from core.models import Photo
from rest_framework.views import APIView
from rest_framework.response import Response



class PhotoSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    people = serializers.CharField()
    photo = serializers.CharField()
    location = serializers.CharField(max_length=255)
    description = serializers.CharField()
    date = serializers.DateField(read_only=True)

    def create(self, validated_data):
        return Photo.objects.create(**validated_data)