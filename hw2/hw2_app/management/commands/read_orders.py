from django.core.management.base import BaseCommand
from hw2_app.models import Order


class Command(BaseCommand):
    help = "Reads all orders"

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        self.stdout.write(f"{orders}")
