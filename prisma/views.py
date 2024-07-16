from django.shortcuts import render, redirect, get_object_or_404
from .models import UseCases, BusinessValue, BusinessCalifications, Feasibility, FeasibilityCalifications
from .forms import UseCasesForm, RatingForm

import pandas as pd
import os

def use_cases(request):
    if request.method == "POST":
        form = UseCasesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('use_cases')
    else:
        form = UseCasesForm()

    use_cases_qs = UseCases.objects.all()
    use_cases_df = pd.DataFrame.from_records(use_cases_qs.values())    
    use_cases_html = use_cases_df.to_html()
    return render(request, 'use_cases.html', {
        'use_cases': use_cases_html,
        'form': form
    })

def business_value(request):
    business_value_qs = BusinessValue.objects.all()
    business_value_df = pd.DataFrame.from_records(business_value_qs.values())
    business_value_html = business_value_df.to_html()
    return render(request, 'business_value.html', {
        'business_value': business_value_html
    })

def feasibility_value(request):
    feasibility_qs = Feasibility.objects.all()
    feasibility_df = pd.DataFrame.from_records(feasibility_qs.values())
    feasibility_html = feasibility_df.to_html()
    return render(request, 'feasibility.html', {
        'feasibility': feasibility_html
    })

def califications(request):
    business_califications_qs = BusinessCalifications.objects.all()
    business_califications_df = pd.DataFrame.from_records(business_califications_qs.values())
    business_califications_html = business_califications_df.to_html()

    feasibility_califications_qs = FeasibilityCalifications.objects.all()
    feasibility_califications_df = pd.DataFrame.from_records(feasibility_califications_qs.values())
    feasibility_califications_html = feasibility_califications_df.to_html()
    return render(request, 'califications.html', {
        'business_califications': business_califications_html,
        'feasibility_califications': feasibility_califications_html
    })

def artefacto_view(request):
    # Leer datos de archivos CSV o modelos Django
    use_cases_qs = UseCases.objects.all()
    business_values_qs = BusinessValue.objects.all()
    viability_values_qs = Feasibility.objects.all()

    # Crear DataFrames
    use_cases = pd.DataFrame.from_records(use_cases_qs.values())
    business_values = pd.DataFrame.from_records(business_values_qs.values())
    viability_values = pd.DataFrame.from_records(viability_values_qs.values())    

    # Leer o crear el DataFrame
    if os.path.exists('prisma/artefacto/artefacto.csv'):
        table = pd.read_csv('prisma/artefacto/artefacto.csv', index_col=0)
    else:
        table = pd.DataFrame(index=use_cases['use_case'].values)
        for idx in business_values['business_dimension']:
            table[idx] = 0
        for idx in viability_values['feasibility']:
            table[idx] = 0
        table['Negocio (X)'] = 0
        table['Viabilidad (Y)'] = 0

    form = RatingForm(request.POST or None, initial={'columns': business_values['business_dimension'].tolist() + viability_values['feasibility'].tolist()})
    if request.method == 'POST':        
        if form.is_valid():
            case_to_rate = form.cleaned_data['case_to_rate'].use_case           
            ratings = {key.replace('rating_', ''): value for key, value in form.cleaned_data.items() if key.startswith('rating_')}      
            
            for column, rating in ratings.items():                
                table.loc[case_to_rate, column] = rating            
            
            # Calcular sumas ponderadas
            business_dimensions = business_values['business_dimension'].values
            viability_dimensions = viability_values['feasibility'].values
            
            table.loc[case_to_rate, 'Negocio (X)'] = (table.loc[case_to_rate, business_dimensions] * business_values.set_index('business_dimension')['ponderation']).sum()
            table.loc[case_to_rate, 'Viabilidad (Y)'] = (table.loc[case_to_rate, viability_dimensions] * viability_values.set_index('feasibility')['ponderation']).sum()
            print(table)
            table.to_csv('prisma/artefacto/artefacto.csv')
            
            return redirect('artifacts')
    else:
        form = RatingForm()

    return render(request, 'artifacts.html', {'form': form, 'table': table.to_html()})  

def prisma_diagram(request):
    pass