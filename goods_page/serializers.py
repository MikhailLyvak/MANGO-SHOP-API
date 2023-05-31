from rest_framework import serializers
from goods_page.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "size",
            "sex",
            "price",
            "price_with_discount",
            "on_discount",
            "discount",
            "discount_start_date",
            "discount_start_end"
        ]
        read_only_fields = [
            "discount_start_date",
            "discount_start_end",
            "on_discount",
            "discount"
        ]

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "size",
            "sex",
            "price",
            "price_with_discount",
            "on_discount",
            "discount",
            "discount_start_date",
            "discount_start_end"
        ]
        read_only_fields = ["on_discount"]

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "size",
            "sex",
            "price",
            "price_with_discount",
            "on_discount",
            "discount",
            "discount_start_date",
            "discount_start_end"
        ]
        read_only_fields = [
            "on_discount",
            "discount_start_date",
            "discount_start_end"
        ]
