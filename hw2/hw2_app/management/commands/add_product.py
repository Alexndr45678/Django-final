from django.core.management.base import BaseCommand, CommandParser
from hw2_app.models import Product


class Command(BaseCommand):
    help = "Creates new product"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("name", type=str, help="Product name")
        parser.add_argument("description", type=str, help="Product description")
        parser.add_argument("price", type=float, help="Product price")
        parser.add_argument("quantity", type=int, help="Product quantity")

    def handle(self, *args, **kwargs):
        name, description, price, quantity = (
            kwargs["name"],
            kwargs["description"],
            kwargs["price"],
            kwargs["quantity"],
        )
        product = Product(
            name=name, description=description, price=price, quantity=quantity
        )
        product.save()
        self.stdout.write(f"{product}")
