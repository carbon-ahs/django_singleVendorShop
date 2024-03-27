from django.shortcuts import render
from rest_framework import viewsets

from django_filters import rest_framework as filters

from store.filters import ProductFilter
from store.models import Product
from store.serializers import ProductSerializer

# Create your views here.


class AllProductApi(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.DjangoFilterBackend]
    # filterset_fields = (
    #     "title",
    #     "selling_price",
    #     "specification",
    # )
    filterset_class = ProductFilter
