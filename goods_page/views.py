from rest_framework import viewsets, status, parsers
from rest_framework.decorators import action
from django.utils import timezone
from rest_framework.response import Response
from django_q.tasks import async_task
from django.shortcuts import redirect

from goods_page.pagination import Pagination
from goods_page.models import Product
from goods_page.serializers import (
    ProductSerializer,
    ProductListSerializer,
    ProductDetailSerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Pagination
    parser_classes = [
        parsers.MultiPartParser,
        parsers.FileUploadParser,
        parsers.FormParser,
    ]

    @action(detail=True, methods=["get"])
    def activate_discount(self, request, pk=None):
        product = self.get_object()

        if product.on_discount:
            return Response(
                {"detail": "This product is already on discount"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        product.on_discount = True
        product.discount_start_date = timezone.now()
        product.discount_start_end = timezone.now() + timezone.timedelta(seconds=7)
        product.save()

        async_task(
            "goods_page.tasks.schedule_remove_discount",
            product.pk,
            product.discount_start_end,
        )

        serializer = self.get_serializer(product)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == "list":
            return ProductListSerializer
        if self.action == "update":
            return ProductDetailSerializer
        return ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        name = self.request.query_params.get("name")
        size = self.request.query_params.get("size")

        if name:
            queryset = Product.objects.filter(name__icontains=name)

        if size:
            queryset = Product.objects.filter(size=size)

        return queryset
