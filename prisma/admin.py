from django.contrib import admin
from .models import UseCases, BusinessValue, BusinessCalifications, Feasibility, FeasibilityCalifications

def register_models(*models):
    for model in models:
        admin.site.register(model)

register_models(UseCases, 
                BusinessValue, 
                BusinessCalifications, 
                Feasibility, 
                FeasibilityCalifications)