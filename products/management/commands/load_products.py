from django.core.management.base import BaseCommand

from products.models import Product, StockRecord


class Command(BaseCommand):

    def handle(self, *args, **options):
        tomato = Product.objects.create(name="Tomato")
        milk = Product.objects.create(name="Milk")

        StockRecord.objects.bulk_create(
            StockRecord(**params)
            for params in [
                dict(price=5, quantity=10,
                     has_infinite_quantity=True,
                     on_sale=False, product=tomato),
                dict(price=10, quantity=10,
                     has_infinite_quantity=False,
                     on_sale=True, product=tomato),
                dict(price=8, quantity=2,
                     has_infinite_quantity=True,
                     on_sale=True, product=tomato),
                dict(price=10, quantity=2,
                     has_infinite_quantity=False,
                     on_sale=True, product=tomato),

                dict(price=10, quantity=1,
                     has_infinite_quantity=False,
                     on_sale=True, product=milk),
                dict(price=8, quantity=5,
                     has_infinite_quantity=False,
                     on_sale=True, product=milk),
                dict(price=5, quantity=1,
                     has_infinite_quantity=True,
                     on_sale=True, product=milk),
                dict(price=3, quantity=10,
                     has_infinite_quantity=False,
                     on_sale=False, product=milk),
            ]
        )

        print("Data was loaded")


required_quantity = 5
