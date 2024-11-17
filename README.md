# Chocolate House Application

## Overview
This Python-based Django application is designed to manage the operations of a fictional chocolate house. It includes features such as:
- **Seasonal Flavors**: Managing chocolate flavors available in different seasons.
- **Ingredient Inventory**: Tracking ingredients and their quantities.
- **Customer Suggestions and Allergy Concerns**: Collecting feedback and suggestions from customers.

## Setup Instructions

### Local Setup
1. Clone the repository:
   
   ```bash
   git clone https://github.com/DarshanR1922/chocalate-house.git
   cd chocalate-house

2.Set up a virtual environment:

python -m venv venv

**3.Activate the virtual environment:**

On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

**4.pip install django**

**5.python manage.py makemigratiions**

**6.python manage.py migrate**

**7.python manage.py runserver****
API Endpoints
1. Seasonal Flavors
GET /flavors: Get all available seasonal flavors.
http://127.0.0.1:8000/chocolate_house/flavors/
2. Inventory
GET /inventory: Get all inventory items, including ingredients and quantities.
   http://127.0.0.1:8000/chocolate_house/inventory/
POST /inventory: Add a new inventory item, specifying its name, quantity, and unit price.
3. Customer Suggestions
GET /suggestions: Get all customer suggestions, including feedback and allergy concerns.
http://127.0.0.1:8000/chocolate_house/suggestions/
POST /suggestions: flavour suggestion and any allergy concerns.
