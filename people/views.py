from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, serializers, status
from rest_framework.generics import GenericAPIView

# Create your views here.
from rest_framework.response import Response
import client

class PeopleDetectSerializer(serializers.Serializer):
    image = serializers.ImageField()

class PeopleDetectURLSerializer(serializers.Serializer):
    url = serializers.CharField(default='')

class PeopleDetectClassify(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PeopleDetectSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image = serializer.validated_data.get('image')
        response = client.people_detect_classify(image)
        return Response(response, status=status.HTTP_200_OK)


class PeopleDetectURLClassify(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PeopleDetectURLSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url = serializer.validated_data.get('url')
        response = client.people_detect_url(url)
        return Response(response, status=status.HTTP_200_OK)