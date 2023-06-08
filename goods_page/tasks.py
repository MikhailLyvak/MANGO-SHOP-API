from .models import Product
from django_q.tasks import schedule


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


def schedule_remove_discount(product_id, end_time):
    schedule(
        "goods_page.tasks.remove_discount",
        product_id,
        schedule_type="O",
        next_run=end_time,
    )


def remove_discount_bulk(product_ids: list):
    for product_id in product_ids:
        try:
            product = Product.objects.get(pk=product_id)
            if product.on_discount:
                product.on_discount = False
                product.discount_start_date = None
                product.discount_start_end = None
                product.save()
        except Product.DoesNotExist:
            pass


def schedule_remove_discount_bulk(product_ids: list, end_time):
    schedule(
        "goods_page.tasks.remove_discount_bulk",
        product_ids,
        schedule_type="O",
        next_run=end_time,
    )
