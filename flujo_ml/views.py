from django.shortcuts import render, redirect

FLUJO_DECISIONES = {
    'pregunta_problema_especifico': {
        'pregunta': '¿Tiene un problema específico que quiera resolver?',
        'opciones': {
            'Sí': 'definicion_problema',
            'No': 'no_necesita_ml',
        },
    },
    'definicion_problema': {
        'pregunta': 'Se recomienda hacer un ejercicio de definición de problemas. ¿Ya lo realizó?',
        'opciones': {
            'Sí': 'problema_nuevo',
            'No': 'invita_definir_problema',
        },
    },
    'problema_nuevo': {
        'pregunta': '¿Es un problema nuevo?',
        'opciones': {
            'Sí': 'problema_resolver_reglas_simples',
            'No': 'acceso_datos_relevantes',
        },
    },
    'problema_resolver_reglas_simples': {
        'pregunta': '¿El problema planteado se puede resolver con reglas simples?',
        'opciones': {
            'Sí': 'experiencia_suficiente',
            'No': 'uso_IA',
        },
    },
    'experiencia_suficiente': {
        'pregunta': '¿Tiene experiencia suficiente para resolver el problema sin ML?',
        'opciones': {
            'Sí': 'uso_RPA',
            'No': 'descubrir_reglas_RPA',
        },
    },
    'uso_RPA': {
        'pregunta': 'No necesitas ML, te invitamos a hacer uso de RPAs.',
        'opciones': {},
    },
    'descubrir_reglas_RPA': {
        'pregunta': 'No necesitas ML, te invitamos a descubrir las reglas y usar RPAs.',
        'opciones': {},
    },
    'uso_IA': {
        'pregunta': 'Se recomienda el uso de Inteligencia Artificial.',
        'opciones': {},
    },
    'acceso_datos_relevantes': {
        'pregunta': '¿Tiene acceso a datos relevantes y suficientes?',
        'opciones': {
            'Sí': 'datos_estructurados',
            'No': 'recoleccion_datos',
        },
    },
    'datos_estructurados': {
        'pregunta': '¿Cuentas con datos estructurados?',
        'opciones': {
            'Sí': 'limpieza_calidad_datos',
            'No': 'datos_no_estructurados',
        },
    },
    'limpieza_calidad_datos': {
        'pregunta': '¿Tus datos están en condiciones de limpieza y calidad?',
        'opciones': {
            'Sí': 'consideracion_datos',
            'No': 'limpieza_preprocesamiento',
        },
    },
    'limpieza_preprocesamiento': {
        'pregunta': 'Se recomienda un proceso de limpieza y preprocesamiento de datos.',
        'opciones': {},
    },
    'datos_no_estructurados': {
        'pregunta': '¿Los datos son NO estructurados?',
        'opciones': {
            'Sí': 'considerar_IA',
            'No': 'consideracion_datos',
        },
    },
    'considerar_IA': {
        'pregunta': 'Se recomienda considerar el uso de Inteligencia Artificial. ¿De qué tipo son tus datos?',
        'opciones': {
            'Imágenes': 'imagenes',
            'Vídeos': 'videos',
            'Texto': 'texto',
        },
    },
    'imagenes': {
        'pregunta': 'Se recomienda usar modelos de Visión por Computadora como CNNs (Redes Neuronales Convolucionales).',
        'opciones': {},
    },
    'videos': {
        'pregunta': 'Se recomienda usar modelos de Análisis de Video como RNNs (Redes Neuronales Recurrentes) o Modelos 3D-CNN.',
        'opciones': {},
    },
    'texto': {
        'pregunta': 'Se recomienda usar modelos de Procesamiento de Lenguaje Natural (NLP) como Transformers (por ejemplo, BERT, GPT).',
        'opciones': {},
    },
    'consideracion_datos': {
        'pregunta': '¿Qué estás considerando hacer con tus datos?',
        'opciones': {
            'Quieres predecir un número o categoría': 'prediccion_numero_categoria',
            'Quieres identificar patrones y relaciones': 'identificar_patrones',
        },
    },
    'prediccion_numero_categoria': {
        'pregunta': '¿Qué resume mejor tu problema?',
        'opciones': {
            'Clasificar en categorías': 'clasificar_categorias',
            'Predecir un valor numérico': 'tiempo_importante',
        },
    },
    'clasificar_categorias': {
        'pregunta': '¿Quieres clasificar en dos categorías?',
        'opciones': {
            'Sí': 'clasificacion_binaria',
            'No': 'clasificacion_multiple',
        },
    },
    'clasificacion_binaria': {
        'pregunta': 'Tu problema podría beneficiarse de un algoritmo de clasificación binaria.',
        'opciones': {},
    },
    'clasificacion_multiple': {
        'pregunta': 'Tu problema podría beneficiarse de un algoritmo de clasificación múltiple.',
        'opciones': {},
    },
    'tiempo_importante': {
        'pregunta': '¿El tiempo es una parte importante de tu información?',
        'opciones': {
            'Sí': 'series_tiempo',
            'No': 'algoritmo_regresion',
        },
    },
    'series_tiempo': {
        'pregunta': 'Tu problema podría beneficiarse de un algoritmo de series de tiempo.',
        'opciones': {},
    },
    'algoritmo_regresion': {
        'pregunta': 'Tu problema podría beneficiarse de un algoritmo de regresión.',
        'opciones': {},
    },
    'identificar_patrones': {
        'pregunta': '¿Qué tipo de patrones esperas encontrar?',
        'opciones': {
            'Pequeños grupos': 'clustering',
            'Temas en documentos': 'modelo_topicos',
            'Recomendaciones': 'motor_recomendaciones',
            'Asociaciones': 'analisis_asociacion',
        },
    },
    'clustering': {
        'pregunta': 'Tu problema podría beneficiarse de un algoritmo de clustering.',
        'opciones': {},
    },
    'modelo_topicos': {
        'pregunta': 'Tu problema podría beneficiarse de un modelo de tópicos.',
        'opciones': {},
    },
    'motor_recomendaciones': {
        'pregunta': 'Tu problema podría beneficiarse de un motor de recomendaciones.',
        'opciones': {},
    },
    'analisis_asociacion': {
        'pregunta': 'Tu problema podría beneficiarse de un análisis de reglas de asociación.',
        'opciones': {},
    },
    'no_necesita_ml': {
        'pregunta': 'No necesitas Machine Learning.',
        'opciones': {},
    },
    'invita_definir_problema': {
        'pregunta': 'Te invitamos a definir bien tu problema. Puedes hacer uso del ARTEFACTO DE IDENTIFICACIÓN',
        'opciones': {},
    },
    'recoleccion_datos': {
        'pregunta': 'Se recomienda la recolección o generación de datos.',
        'opciones': {},
    },
}

def flujo_decision(request, paso):
    preguntas_resueltas = request.session.get('preguntas_resueltas', [])
    pregunta_actual = FLUJO_DECISIONES.get(paso)

    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        if respuesta in pregunta_actual['opciones']:
            siguiente_paso = pregunta_actual['opciones'][respuesta]
            # Actualizar la respuesta en preguntas_resueltas
            preguntas_resueltas = {p[0]: p[1] for p in preguntas_resueltas}  # Convertir a dict
            preguntas_resueltas[pregunta_actual['pregunta']] = respuesta  # Actualizar o agregar
            preguntas_resueltas = list(preguntas_resueltas.items())  # Convertir de vuelta a lista
            request.session['preguntas_resueltas'] = preguntas_resueltas
            return redirect('flujo_decision', paso=siguiente_paso)

    # Determinar si hay más preguntas
    hay_mas_preguntas = bool(pregunta_actual['opciones'])

    return render(request, 'flujo_ml/flujo_decision.html', {
        'pregunta_actual': pregunta_actual['pregunta'],
        'opciones': pregunta_actual['opciones'],
        'preguntas_resueltas': preguntas_resueltas,
        'hay_mas_preguntas': hay_mas_preguntas,
    })

def inicio_flujo_view(request):
    # Reiniciar el flujo y las preguntas previas
    request.session['preguntas_resueltas'] = []
    return redirect('flujo_decision', paso='pregunta_problema_especifico')

