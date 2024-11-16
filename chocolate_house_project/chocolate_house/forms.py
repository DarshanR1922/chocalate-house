from django import forms
from .models import SeasonalFlavor, IngredientInventory, CustomerSuggestion


class SeasonalFlavorForm(forms.ModelForm):
    class Meta:
        model = SeasonalFlavor
        fields = ['name', 'description']


class IngredientInventoryForm(forms.ModelForm):
    class Meta:
        model = IngredientInventory
        fields = ['name', 'quantity','unit_price']

class CustomerSuggestionForm(forms.ModelForm):
    class Meta:
        model = CustomerSuggestion
        fields = ['flavor_suggestion', 'allergy_concern']
