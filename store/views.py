from django.shortcuts import render
from rest_framework import viewsets

from store.models import Product
from store.serializers import ProductSerializer

# Create your views here.


class AllProductApi(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



