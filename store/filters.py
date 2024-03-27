from django_filters.rest_framework import FilterSet
from .models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            "model": ["exact"],
            "specification": ["contains"],
            "selling_price": ["gt", "lt"],
        }
