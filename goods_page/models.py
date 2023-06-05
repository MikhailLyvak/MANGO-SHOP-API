from django.db import models
from enum import Enum


class SizeEnum(Enum):
    S_SMALL = "S"
    M_MEDIUM = "M"
    L_LARGE = "L"
    XL_SUPER_LARGE = "XL"


class SexEnum(Enum):
    FEMALE = "Female"
    MALE = "Male"


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    size = models.CharField(
        max_length=2, choices=[(choice.value, choice.name) for choice in SizeEnum]
    )
    sex = models.CharField(
        max_length=6, choices=[(choice.value, choice.name) for choice in SexEnum]
    )
    price = models.FloatField()
    inventory = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True)
    on_discount = models.BooleanField(default=False)
    discount = models.PositiveIntegerField(default=17)
    discount_start_date = models.DateTimeField(null=True)
    discount_start_end = models.DateTimeField(null=True)

    class Meta:
        ordering = ["-on_discount", "name"]
        unique_together = ("name", "size")

    @property
    def price_with_discount(self) -> float:
        if self.on_discount is True:
            return round(self.price * (1 - self.discount / 100), 2)

    def __str__(self) -> str:
        if self.on_discount is True:
            return f"Name: {self.name}, Price: {self.price}, PWD: {self.price_with_discount}, Size: {self.size}"
        return f"Name: {self.name}, Price: {self.price}, Size: {self.size}"
