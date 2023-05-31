from django.urls import path, include
from rest_framework import routers
from goods_page.views import ProductViewSet

router = routers.DefaultRouter()
router.register("products", ProductViewSet, basename="product")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "goods_page"
