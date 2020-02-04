from django.core.management.base import BaseCommand
from shoestore.shoeapp.models import ShoeColor, ShoeType

# Prepopulates the ShoeType and ShoeColor tables:


class Command(BaseCommand):
    help = 'Prepopulate ShoeType and ShoeColor tables'

    def handle(self, *args, **options):
        shoe_types = ['sneaker', 'boot', 'sandal', 'dress', 'other']
        shoe_colors = ['Red', 'Orange', 'Yellow', 'Green',
                       'Blue', 'Indigo', 'Violet', 'White', 'Black']

        for style in shoe_types:
            ShoeType.objects.create(style=style)

        self.stdout.write(self.style.SUCCESS('Shoe types successfully initialized.'))

        for color in shoe_colors:
            ShoeColor.objects.create(color_name=color)

        self.stdout.write(self.style.SUCCESS('Shoe colors successfully initialized.'))