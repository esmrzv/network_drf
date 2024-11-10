from django.shortcuts import render
from rest_framework import viewsets

from retail_network.models import Network, Product
from retail_network.serializers import NetworkSerializer, ProductSerializer


# Create your views here.

class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
