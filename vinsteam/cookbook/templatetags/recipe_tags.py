from cookbook.models import Recipe
from django import template

register = template.Library()

@register.simple_tag
def get_recipe_weight(recipe, product):
    recipeproduct = recipe.recipeproduct_set.filter(product=product).first()
    if recipeproduct:
        return f"{recipeproduct.weight} г"
    else:
        return "Не указано"
