from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This commands inserts post data"

    def handle(self, *args: Any, **options: Any):
       
        #  delete existing data
        Category.objects.all().delete()

        Categories=["sport","technology","science","art","food"]
        
        for category_name in Categories:
            Category.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))