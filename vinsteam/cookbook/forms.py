from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProductForm(forms.Form):
    product_name = forms.CharField(
        max_length=255,
        label='Продукт',
        widget=forms.TextInput(attrs={
            'required': True,
            'class': 'form-control'}),
    )
    product_weight = forms.IntegerField(
        label='Укажите количество (g)',
        widget=forms.NumberInput(attrs={
            'required': True,
            'class': 'form-control'}),
    )


ProductFormSet = forms.formset_factory(ProductForm, extra=1)
