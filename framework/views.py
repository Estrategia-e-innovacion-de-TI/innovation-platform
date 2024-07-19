from django.shortcuts import render
import pandas as pd
import numpy as np
from .forms import InnovacionFormularioForm, ResultadosInnovacionForm
from .models import ResultadosInnovacion

def framework_view(request):
    if request.method == 'POST':

        form = InnovacionFormularioForm(request.POST)
        if form.is_valid():
            form_instance = form.save()
            methodologies, first_phase, second_phase, thrid_phase, fourth_phase, fifth_phase, sixth_phase = get_results(form.cleaned_data)
            # Crear instancia de ResultadosInnovacion y guardar en la base de datos

            df_methodologies = pd.DataFrame(methodologies)
            df_first_phase = pd.DataFrame(first_phase)
            df_second_phase = pd.DataFrame(second_phase)
            df_thrid_phase = pd.DataFrame(thrid_phase)
            df_fourth_phase = pd.DataFrame(fourth_phase)    
            df_fifth_phase = pd.DataFrame(fifth_phase)
            df_sixth_phase = pd.DataFrame(sixth_phase)

            df_methodologies['Tipo']  = ['Metodología']*len(df_methodologies)
            df_first_phase['Tipo']  = ['Técnica - Identificar necesidad']*len(df_first_phase)
            df_second_phase['Tipo']  = ['Técnica - Generar ideas']*len(df_second_phase)
            df_thrid_phase['Tipo']  = ['Técnica - Seleccionar ideas']*len(df_thrid_phase)   
            df_fourth_phase['Tipo']  = ['Técnica - Protoripar']*len(df_fourth_phase)
            df_fifth_phase['Tipo']  = ['Técnica - Validar']*len(df_fifth_phase)
            df_sixth_phase['Tipo']  = ['Técnica - Implementar']*len(df_sixth_phase)

            df_results = pd.concat([df_methodologies, df_first_phase, df_second_phase, df_thrid_phase, df_fourth_phase, df_fifth_phase, df_sixth_phase])
            save_complete_dataframe(df_results)

            return render(request,
                           'framework/resultados.html',
                             {'metodologias': methodologies,
                              'fase_uno': first_phase,
                              'fase_dos': second_phase,
                              'fase_tres': thrid_phase,
                              'fase_cuatro': fourth_phase,
                              'fase_cinco': fifth_phase,
                              'fase_seis': sixth_phase})

    else:
        form = InnovacionFormularioForm()
    return render(request, 'framework/formulario.html', {'form': form})

def save_complete_dataframe(dataframe):
    # Convierte el DataFrame a JSON
    json_data = dataframe.to_json(orient='records')

    # Crea una instancia del modelo y guarda los datos
    df_storage = ResultadosInnovacion(data=json_data)
    df_storage.save()

def get_results(data):
    excel_file = 'framework/data/lista_innovacion.xlsx'  # Replace with your Excel file path
    df_lista_innovacion = pd.read_excel(excel_file, skiprows=1)  # Read Excel file into a DataFrame

    choosen_purposes  =  list(data.get('proposito_iniciativa'))
    
     # Función para verificar si alguno de los propósitos está en la lista de propósitos de la fila
    def contains_any_purpose(row):
        row_purposes = row['Propósito'].split(', ')
        return any(purpose in row_purposes for purpose in choosen_purposes)

    
    df_lista_innovacion_filter  = df_lista_innovacion[df_lista_innovacion['En artefacto']=='Si']
    df_lista_innovacion_filter = df_lista_innovacion_filter[df_lista_innovacion_filter.apply(contains_any_purpose, axis=1)]

    return calc_top_methodologies_and_techniques(data, df_innovation_filter=df_lista_innovacion_filter)  
    
def get_dict(list_result):
    result = []
    if isinstance(list_result, str):     
        return [{'nombre': list_result, 'puntuacion': '','url': ''}]
    else:
        for item in list_result:
            if item[1] <= 60:
                result.append({'nombre': 'No tenemos sugerencias para tí', 'puntuacion': '', 'url': ''})
                break
            else:
                result.append({'nombre': item[0], 'puntuacion': str(item[1])+'%', 'url': item[2]})
        return result


def calc_top_methodologies_and_techniques(data, **kwargs):

    if 'df_innovation_filter' in kwargs:
        df_innovation_filter = kwargs['df_innovation_filter']
    
    urgency = int(data.get('urgencia'))
    complexity = int(data.get('complejidad'))
    uncertainty = int(data.get('incertidumbre'))
    collaboration = int(data.get('colaboracion'))
    resources = int(data.get('recursos'))
    flexibility = int(data.get('flexibilidad'))
    velocity = int(data.get('velocidad'))
    risk  = int(data.get('riesgo'))
    user = int(data.get('usuario'))

    df_innovation_filter['calc_urgencia']  = (5 -  (df_innovation_filter['Urgencia']-urgency).abs())
    df_innovation_filter['calc_complejidad'] = (5 - (df_innovation_filter['Complejidad']-complexity).abs())
    df_innovation_filter['calc_incertidumbre'] = (5 - (df_innovation_filter['Incertidumbre']-uncertainty).abs())
    df_innovation_filter['calc_colaboracion'] = (5 - (df_innovation_filter['Colaboración']-collaboration).abs())
    df_innovation_filter['calc_recursos'] = (5 - (df_innovation_filter['Recursos Disponibles']-resources).abs())
    df_innovation_filter['calc_flexibilidad'] = (5 - (df_innovation_filter['Flexibilidad']-flexibility).abs())
    df_innovation_filter['calc_velocidad'] = (5 - (df_innovation_filter['Velocidad de implementación']-velocity).abs())
    df_innovation_filter['calc_riesgo'] = (5 - (df_innovation_filter['Factor de Riesgo']-risk).abs())
    df_innovation_filter['calc_usuario'] = (5 - (df_innovation_filter['Conocimiento del usuario']-user).abs())

    df_innovation_filter['total'] = round((df_innovation_filter.filter(regex='^calc_').sum(axis=1)/45)*100,1)

    #Top 3 metodologias
    df_methodologies = df_innovation_filter[df_innovation_filter['Tipo'] == 'Metodología']
    methodologies = df_methodologies[["Nombre", "total", "Plantilla"]].sort_values(by='total', ascending=False).head(3).values

    df_techniques = df_innovation_filter[df_innovation_filter['Tipo'] == 'Técnica']
    #Top 3 tecnicas por fase de innovacion 
    selected_phases = list(data.get('fase_innovacion'))
    phases = [
    '1. Identificación de la necesidad o problema',
    '2. Generación de ideas',
    '3. Selección de ideas',
    '4. Desarrollo del prototipo',
    '5. Pruebas y validación',
    '6. Implementación']

    for phase in phases:
        if phase in selected_phases:
            df_techniques[f"calc_{phase}"] = df_techniques[phase]*df_techniques['total']
        else:
            df_techniques[f"calc_{phase}"] = [0]*len(df_techniques)

    first_phase = df_techniques[["Nombre", f"calc_{phases[0]}","Plantilla"]].sort_values(by=f"calc_{phases[0]}",
                                                                              ascending=False).head(3).values if df_techniques[f"calc_{phases[0]}"].sum() > 0 else "No Seleccionado"
    second_phase = df_techniques[["Nombre", f"calc_{phases[1]}","Plantilla"]].sort_values(by=f"calc_{phases[1]}",
                                                                                ascending=False).head(3).values if df_techniques[f"calc_{phases[1]}"].sum() > 0 else "No Seleccionado"
    thrid_phase = df_techniques[["Nombre", f"calc_{phases[2]}","Plantilla"]].sort_values(by=f"calc_{phases[2]}",
                                                                                ascending=False).head(3).values if df_techniques[f"calc_{phases[2]}"].sum() > 0 else "No Seleccionado"
    fourth_phase = df_techniques[["Nombre", f"calc_{phases[3]}","Plantilla"]].sort_values(by=f"calc_{phases[3]}", 
                                                                                ascending=False).head(3).values if df_techniques[f"calc_{phases[3]}"].sum() > 0 else "No Seleccionado"
    fifth_phase = df_techniques[["Nombre", f"calc_{phases[4]}","Plantilla"]].sort_values(by=f"calc_{phases[4]}",
                                                                                ascending=False).head(3).values if df_techniques[f"calc_{phases[4]}"].sum() > 0 else "No Seleccionado"
    sixth_phase = df_techniques[["Nombre", f"calc_{phases[5]}","Plantilla"]].sort_values(by=f"calc_{phases[5]}",
                                                                                ascending=False).head(3).values if df_techniques[f"calc_{phases[5]}"].sum() > 0 else "No Seleccionado"

    return get_dict(methodologies), get_dict(first_phase), get_dict(second_phase),get_dict(thrid_phase), get_dict(fourth_phase), get_dict(fifth_phase), get_dict(sixth_phase)




