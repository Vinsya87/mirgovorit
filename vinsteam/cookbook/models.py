from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    times_used = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(
        'Название',
        max_length=255)
    products = models.ManyToManyField(Product, through='RecipeProduct')

    def __str__(self):
        return self.name


class RecipeProduct(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.IntegerField()

    def __str__(self):
        return f"{self.recipe.name} - {self.product.name} ({self.weight}g)"

    def save(self, *args, **kwargs):        
        is_new_recipe_product = not self.id
        super().save(*args, **kwargs)
        if is_new_recipe_product:
            self.cook_recipe()

    def cook_recipe(self):
        self.product.times_used += 1
        self.product.save()
