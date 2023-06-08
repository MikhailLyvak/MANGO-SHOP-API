from django.urls import path, include
from rest_framework import routers
from goods_page.views import ProductViewSet, activate_discount_bulk

router = routers.DefaultRouter()
router.register("products", ProductViewSet, basename="product")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "activate-discount-bulk/", activate_discount_bulk, name="activate-discount-bulk"
    ),
]

app_name = "goods_page"
