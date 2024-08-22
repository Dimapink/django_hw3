import csv
from django.utils.text import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            with open('phones.csv', 'r') as file:
                phones = list(csv.DictReader(file, delimiter=';'))
            for phone in phones:
                name = phone.get("name")
                entity = Phone(name=name, price=phone.get("price"),
                               image=phone.get("image"), release_date=phone.get("release_date"),
                               lte_exists=phone.get("lte_exists"), slug=slugify(name))
                entity.save()

        except Exception as e:
            self.stdout.write(self.style.ERROR("Возникла проблема:"))
            self.stdout.write(repr(e))
        else:
            self.stdout.write(self.style.SUCCESS("Импорт из csv файла успешно завершен"))


