from rest_framework import serializers
from store.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "title", "model", "selling_price", "specification", "image")
