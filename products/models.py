from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    """Base model for all items in the store"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    stock = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Dog(Product):
    """Specific details for live animals"""
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    SIZE_CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')]

    breed = models.CharField(max_length=100)
    age_weeks = models.PositiveIntegerField(help_text="Age in weeks")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    is_vaccinated = models.BooleanField(default=False)


class PetFood(Product):
    """Specific details for consumables"""
    FLAVOR_CHOICES = [('CH', 'Chicken'), ('BF', 'Beef'), ('FG', 'Fish'), ('VG', 'Vegetarian')]
    LIFE_STAGE = [('P', 'Puppy'), ('A', 'Adult'), ('S', 'Senior')]

    flavor = models.CharField(max_length=2, choices=FLAVOR_CHOICES)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)], help_text="Weight in kg")
    ingredients = models.TextField()
    life_stage = models.CharField(max_length=1, choices=LIFE_STAGE)
    flavour = models.CharField(max_length=50, blank=True, null=True)


class Toy(Product):
    """Specific details for accessories"""
    MATERIAL_CHOICES = [('R', 'Rubber'), ('P', 'Plastic'), ('S', 'Soft'), ('W', 'Wood'), ('M', 'Metal')]
    SIZE_CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]

    material = models.CharField(max_length=1, choices=MATERIAL_CHOICES)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    is_interactive = models.BooleanField(default=False)
    durability_rating = models.IntegerField(help_text="Scale 1-5", default=3)
    suitable_for = models.CharField(max_length=100, help_text="Suitable for which type of pets")

    def __str__(self):
        return self.name
