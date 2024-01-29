from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductFormSet, RecipeForm
from .models import Product, Recipe, RecipeProduct


def index(request):
    recipe_form = RecipeForm()
    product_formset = ProductFormSet(prefix='products')
    products = Product.objects.filter(recipe__isnull=False).distinct()
    # обнулял times_used
    # prod = Product.objects.all()
    # prod.all().update(times_used=0)
    context = {
        'recipe_form': recipe_form,
        'product_formset': product_formset,
        'products': products,
    }

    return render(request, 'index.html', context)


def add_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        product_formset = ProductFormSet(request.POST, prefix='products')
        if recipe_form.is_valid() and product_formset.is_valid():
            recipe, _ = Recipe.objects.get_or_create(**recipe_form.cleaned_data)
            for form in product_formset:
                product_name = form.cleaned_data['product_name']
                product_weight = form.cleaned_data['product_weight']
                product, _ = Product.objects.get_or_create(name=product_name)
                add_product_to_recipe(recipe.id, product.id, product_weight)

            return redirect('cookbook:index')
    return redirect('cookbook:index')


def add_product_to_recipe(recipe_id, product_id, product_weight):
    recipe_product, created = RecipeProduct.objects.update_or_create(
        recipe_id=recipe_id,
        product_id=product_id,
        defaults={'weight': product_weight},
    )
    if not created:
        recipe_product.weight = product_weight
        recipe_product.save()

    return recipe_product, created


def show_recipes_without_product(request, product_id):
    """Получаем продукт по ID"""
    product = get_object_or_404(Product, pk=product_id)
    recipes = Recipe.objects.filter(
        Q(recipeproduct__product=product,
          recipeproduct__weight__lt=10) | Q(recipeproduct__isnull=True)).distinct()
    context = {
        'product': product,
        'recipes': recipes,
    }
    return render(request, 'product.html', context)
