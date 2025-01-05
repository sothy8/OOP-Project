from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        labels = {
            "product_id": "ID",   
            "product_category": "Category",
            "product_item": "Item",
            "product_size": "Size",
            "product_color": "Color",
            "product_brand": "Brand",
            "product_price": "Price",
            "product_releasing_year": "Releasing year",
        }
        widgets = {
            "product_id": forms.TextInput(
                attrs={
                    "placeholder": "e.g. CH00000",
                    "class": "form-control",
                }
            ),
            "product_category": forms.Select(
                choices=Product.Category.choices,
                attrs={
                    "class": "form-control",
                }
            ),
            "product_item": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Chanel Jacket",
                    "class": "form-control",
                },
            ),
            "product_size": forms.Select(
                choices=Product.Size.choices,
                attrs={
                    "class": "form-control",
                },
            ),
            "product_color": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "product_brand": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            # Adding a widget for price
            "price": forms.NumberInput(
                attrs={
                    "placeholder": "e.g. 99.99",
                    "class": "form-control",
                    "step": "0.01",  # Allows for decimal precision
                },
            ),
            # Adding a widget for releasing year
            "product_releasing_year": forms.NumberInput(
                attrs={
                    "placeholder": "e.g. 2023",
                    "class": "form-control",
                },
            ),
        }
