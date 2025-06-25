import random

from product.models import Product

from django.core.management.base import BaseCommand

# Django management command to create a specified number of dummy Product instances with random attributes
# Usage: python manage.py create_products 50
class Command(BaseCommand):
    help = 'Create dummy products'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of products to create')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(count):
            Product.objects.create(
                name=f"Product {i+1}",
                description=f"Description for Product {i+1}",
                price=round(random.uniform(10.0, 500.0), 2),
                stock=random.randint(0, 100),
                categories=random.sample(['Electronics', 'Clothing', 'Books', 'Home', 'Toys'], k=random.randint(1, 3)),
                metadata={
                    "color": random.choice(['red', 'blue', 'green', 'black']),
                    "size": random.choice(['S', 'M', 'L', 'XL']),
                    "weight": round(random.uniform(0.5, 5.0), 2)
                }
            )
        self.stdout.write(self.style.SUCCESS(f'{count} products created.'))
