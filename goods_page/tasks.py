from celery import shared_task
from .models import Product


@shared_task
def remove_discount(product_id):
    try:
        product = Product.objects.get(pk=product_id)
        if product.on_discount:
            product.on_discount = False
            product.discount_start_date = None
            product.discount_start_end = None
            product.save()
    except Product.DoesNotExist:
        pass
