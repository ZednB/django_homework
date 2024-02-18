from django.core.management import BaseCommand
from catalog.models import Category, Product
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('fixtures/category.json', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
        with open('fixtures/product.json', encoding='utf-8') as file:
            return json.load(file)

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(
                    pk=category['pk'],
                    name=category['fields']['name'],
                    description=category['fields']['description']
                )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                    pk=product['pk'],
                    name=product['fields']['name'],
                    description=product['fields']['description'],
                    photo=product['fields']['photo'],
                    category=Category.objects.get(pk=product['fields']['category']),
                    price=product['fields']['price']
                )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
