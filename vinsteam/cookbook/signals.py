from django.db.models import F
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from .models import Recipe


@receiver(pre_delete, sender=Recipe)
def recipe_pre_delete(sender, instance, **kwargs):
    print('recipe_pre_delete')
    # Уменьшаем times_used для всех продуктов, связанных с этим рецептом
    instance.products.all().update(times_used=F('times_used') - 1)
