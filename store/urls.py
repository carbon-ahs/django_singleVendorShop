from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()

router.register("", views.AllProductApi, basename="all_products")

# product_router = routers.NestedDefaultRouter(router, "", lookup="pr")


urlpatterns = router.urls
