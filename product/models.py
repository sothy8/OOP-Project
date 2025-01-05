from django.db import models

class Product(models.Model):
    # Auto-incrementing primary key
    product_id = models.BigAutoField(primary_key=True)

    # Category Choices
    class Category(models.TextChoices):
        JACKETS_COATS = ("JACKETS | COATS", "JACKETS | COATS")
        SWEATSHIRTS_KNITWEAR = ("SWEATSHIRTS | KNITWEAR", "SWEATSHIRTS | KNITWEAR")
        SHIRTS = ("SHIRTS", "SHIRTS")
        SHOES = ("SHOES", "SHOES")
        TSHIRTS_POLO_SHIRTS = ("T-SHIRTS | POLO SHIRTS", "T-SHIRTS | POLO SHIRTS")
        DRESSES = ("DRESSES", "DRESSES")
        TOPS = ("TOPS", "TOPS")
        BOTTOMS = ("BOTTOMS", "BOTTOMS")
        SKIRTS = ("SKIRTS", "SKIRTS")
        PANTS = ("PANTS", "PANTS")
        JEANS = ("JEANS", "JEANS")
        OTHER = ("OTHER", "OTHER")

    product_category = models.CharField(
        max_length=50,
        choices=Category.choices,
        default=Category.OTHER,
    )
    
    product_item = models.TextField(max_length=100)
    
    # Size Choices
    class Size(models.TextChoices):
        Extra_Large = ("XL", "Extra Large")
        Large = ("L", "Large")
        Medium = ("M", "Medium")
        Small = ("S", "Small")
        Extra_Small = ("XS", "Extra Small")

    product_size = models.CharField(
        max_length=5,
        choices=Size.choices,
        default=Size.Medium,
    )
    
    product_color = models.TextField(max_length=30)
    product_brand = models.TextField(max_length=30)
    product_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )
    product_releasing_year = models.PositiveIntegerField(default=2023)
    
    def __str__(self):
        return f"{self.product_id} - {self.product_item} | {self.product_category} | {self.product_size} | ${self.product_price:.2f}"
