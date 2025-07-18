from django.urls import path
from .views import ShortenURLAPIView, ExpandURLAPIView

urlpatterns = [
    path('shorten/', ShortenURLAPIView.as_view(), name='shorten-url'),
    path('expand/<str:short_url>/', ExpandURLAPIView.as_view(), name='expand-url'),
]
