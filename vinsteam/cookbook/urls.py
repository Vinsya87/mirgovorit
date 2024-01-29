from django.urls import path

from . import views

app_name = 'cookbook'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('add_product_to_recipe/<int:recipe_id>/<int:product_id>/<int:weight>/',
         views.add_product_to_recipe,
         name='add_product_to_recipe'),
    path('product/<int:product_id>/',
         views.show_recipes_without_product,
         name='product'),
]
