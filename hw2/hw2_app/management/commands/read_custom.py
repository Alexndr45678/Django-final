from django.core.management.base import BaseCommand
from hw2_app.models import Customer


class Command(BaseCommand):
    help = "Reads all customers"

    def handle(self, *args, **kwargs):
        customers = Customer.objects.all()
        self.stdout.write(f"{customers}")
