from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import ShortURL
from .serializers import ShortenSerializer
from .utils import generate_short_url

class ShortenURLAPIView(APIView):
    '''Handle POST requests to create a shortened URL. 
    Validates input, generates a unique short URL, saves it,
    and returns the shortened URL or errors.'''
    def post(self,request):
        serializer = ShortenSerializer(data = request.data)
        if serializer.is_valid():
            original_url = serializer.validated_data['original_url']
            short_url = generate_short_url() #generate shortened url

            while ShortURL.objects.filter(short_url=short_url).exists(): #check if identical url already exists
                short_url = generate_short_url()

            short_url = ShortURL.objects.create(original_url=original_url, short_url=short_url) #create shortened url object
            return Response({
                'short_url': f"http://localhost:8000/api/expand/{short_url}/"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExpandURLAPIView(APIView):
    '''Handle GET request to expand the created shortened URL to the original form'''
    def get(self, request, short_url):
        short_url = get_object_or_404(ShortURL, short_url=short_url) #search for existing URL objects with mathching url
        return Response({
            'original_url': short_url.original_url
        }, status=status.HTTP_200_OK)
