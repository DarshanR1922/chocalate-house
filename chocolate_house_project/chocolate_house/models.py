from django.db import models


class SeasonalFlavor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class IngredientInventory(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00) 

    def __str__(self):
        return f"{self.name} - {self.quantity}"


class CustomerSuggestion(models.Model):
    customer_name = models.CharField(max_length=255) 
    flavor_suggestion = models.CharField(max_length=255, blank=True, null=True)  # New field for flavor suggestion
    allergy_concern = models.TextField(blank=True, null=True)  # New field for allergy concern

    def __str__(self):
        return self.customer_name