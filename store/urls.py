from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

# from .views import say_hello
router.register("", views.AllProductApi, basename="all_products")

urlpatterns = router.urls

# router = SimpleRouter()
# router.register("users", UserViewSet, basename="users")
# router.register("", PostViewSet, basename="posts")

# urlpatterns = router.urls
