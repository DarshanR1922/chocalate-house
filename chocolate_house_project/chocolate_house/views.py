from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import SeasonalFlavor, IngredientInventory, CustomerSuggestion
from .forms import SeasonalFlavorForm, IngredientInventoryForm, CustomerSuggestionForm

from django.shortcuts import render

def home(request):
    return render(request, 'chocolate_house/home.html')



def flavors(request):
    if request.method == "POST":
        form = SeasonalFlavorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flavors') 
    else:
        form = SeasonalFlavorForm()
    flavors = SeasonalFlavor.objects.all()
    return render(request, 'chocolate_house/flavors.html', {'form': form, 'flavors': flavors})

def inventory(request):
    if request.method == "POST":
        form = IngredientInventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = IngredientInventoryForm()
    inventory_items = IngredientInventory.objects.all()
    return render(request, 'chocolate_house/inventory.html', {'form': form, 'inventory_items': inventory_items})


def suggestions(request):
    if request.method == "POST":
        form = CustomerSuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suggestions')
    else:
        form = CustomerSuggestionForm()
    
    suggestions = CustomerSuggestion.objects.all()
    print(suggestions)  
    return render(request, 'chocolate_house/suggestions.html', {'form': form, 'suggestions': suggestions})
