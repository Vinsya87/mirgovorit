import csv
import logging

from cookbook.models import Product
from django.core.management.base import BaseCommand
from django.db import IntegrityError

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **options):
        path = options['path']
        with open(path, 'rt', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                ingredient_name = row[0]
                try:
                    ingredient, created = Product.objects.get_or_create(
                        name=ingredient_name
                    )
                    if created:
                        logger.info(
                            f'Ингредиент ({ingredient_name}, '
                        )
                    else:
                        logger.info(
                            f'Ингредиент ({ingredient_name}, '
                        )
                except IntegrityError:
                    logger.error(
                        f'Ошибка при добавлении ингредиента '
                        f'({ingredient_name}).'
                    )
