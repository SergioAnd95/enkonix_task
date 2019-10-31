from django.db import models
from django.db.models import Subquery, OuterRef


class StockRecord(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)

    price = models.DecimalField(decimal_places=3, max_digits=15)

    quantity = models.PositiveIntegerField(default=0)
    has_infinite_quantity = models.BooleanField(default=False)

    on_sale = models.BooleanField(default=False)


class ProductQuerySet(models.QuerySet):

    def annotate_lowest_price(self):
        stock_records = StockRecord.objects.filter(
            product=OuterRef("pk"),
            quantity__gte=5,
        ).order_by("id")

        return self.annotate(
            lowest_price=Subquery(stock_records.values("price")[:1]))


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def annotate_lowest_price(self):
        return self.get_queryset().annotate_lowest_price()


class Product(models.Model):
    name = models.CharField(max_length=255, blank=True)

    objects = ProductManager()


# В модели StockRecord хранятся данные о цене продукта.
# quantity / has_infinite_quantity - позволяет задать кол-во товара на складе.
#
# Задание: средствами ORM для каждого продукта посчитать самую
# последнюю (по айди) включенную цену при условии покупки 5 единиц продукта
#
# Ожидаемый результат
#
# print(products.values_list('name', 'lowest_price'))
# >>> [('Milk', Decimal('5.000')), ('Tomato', Decimal('8.000'))]
