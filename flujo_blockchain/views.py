from django.shortcuts import render

from django.shortcuts import render, redirect


FLUJO_BLOCKCHAIN = {
    'necesita_datos_consistentes': {
        'pregunta': '¿Necesita datos consistentes en múltiples entidades?',
        'opciones': {
            'Sí': 'registro_a_prueba_manipulaciones',
            'No': 'no_necesita_dlt_blockchain',
        },
    },
    'registro_a_prueba_manipulaciones': {
        'pregunta': '¿Quiere un registro a prueba de manipulaciones de todas las escrituras en el almacén de datos?',
        'opciones': {
            'Sí': 'registros_no_modificables',
            'No': 'no_manipulaciones',
        },
    },
    'no_manipulaciones': {
        'pregunta': 'Si no necesita auditar lo que sucedió y cuándo sucedió, no necesita tecnología DLT o Blockchain. Considere: Base de datos.',
        'opciones': {},
    },
    'registros_no_modificables': {
        'pregunta': '¿Los registros de datos, una vez escritos, nunca se modifican ni eliminan?',
        'opciones': {
            'Sí': 'mas_de_una_entidad',
            'No': 'tecnologia_dlt_historicos',
        },
    },
    'mas_de_una_entidad': {
        'pregunta': '¿Más de una entidad aporta datos?',
        'opciones': {
            'Sí': 'dificultad_control_datos',
            'No': 'no_mas_de_una_entidad',
        },
    },
    'no_mas_de_una_entidad': {
        'pregunta': 'Usted es solo un contribuyente de datos, DLT se usa normalmente cuando varias entidades aportan datos. Considere: Base de datos a menos que desee DLT para auditoría.',
        'opciones': {},
    },
    'dificultad_control_datos': {
        'pregunta': '¿Las entidades con acceso de escritura tienen dificultades para decidir quién debe tener el control del almacén de datos?',
        'opciones': {
            'Sí': 'necesita_visibilidad_compartida',
            'No': 'no_problemas_confianza',
        },
    },
    'no_problemas_confianza': {
        'pregunta': 'Si no hay problema de confianza, una entidad tiene el control, los datos no necesitan ser distribuidos. Considere: DLT Centralizado.',
        'opciones': {},
    },
    'necesita_visibilidad_compartida': {
        'pregunta': '¿Necesita visibilidad compartida, historial, alta disponibilidad para datos compartidos?',
        'opciones': {
            'Sí': 'usar_dlt_distribuida_blockchain',
            'No': 'no_visibilidad_compartida',
        },
    },
    'no_visibilidad_compartida': {
        'pregunta': 'DLT admite copias del libro mayor verificables de forma independiente si no es necesario, utilice DLT central. Considere: DLT central o Blockchain.',
        'opciones': {},
    },
    'usar_dlt_distribuida_blockchain': {
        'pregunta': 'Se recomienda utilizar tecnologías DLT distribuidas o Blockchain.',
        'opciones': {},
    },
    'no_necesita_dlt_blockchain': {
        'pregunta': 'No necesita tecnología de DLT o Blockchain. Considere: correo electrónico, hojas de cálculo.',
        'opciones': {},
    },
    'no_utilice_dlt_blockchain': {
        'pregunta': 'No utilice tecnologías DLT o Blockchain.',
        'opciones': {},
    },
    'tecnologia_dlt_historicos': {
        'pregunta': 'Tecnología DLT no permite cambios a datos históricos. Considere: registro a prueba de manipulaciones con tecnología de base de datos.',
        'opciones': {},
    },
    'dlt_centralizada': {
        'pregunta': 'Se recomienda utilizar tecnologías DLT centralizadas.',
        'opciones': {},
    },
}


def flujo_decision_blockchain(request, paso):
    preguntas_resueltas = request.session.get('preguntas_resueltas', [])
    pregunta_actual = FLUJO_BLOCKCHAIN.get(paso)

    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        if respuesta in pregunta_actual['opciones']:
            siguiente_paso = pregunta_actual['opciones'][respuesta]
            
            # Actualizar la respuesta en preguntas_resueltas
            preguntas_resueltas = {p[0]: p[1] for p in preguntas_resueltas}  # Convertir a dict
            preguntas_resueltas[pregunta_actual['pregunta']] = respuesta  # Actualizar o agregar
            preguntas_resueltas = list(preguntas_resueltas.items())  # Convertir de vuelta a lista
            request.session['preguntas_resueltas'] = preguntas_resueltas
            return redirect('flujo_decision_blockchain', paso=siguiente_paso)

    hay_mas_preguntas = bool(pregunta_actual['opciones'])

    return render(request, 'flujo_blockchain/flujo_decision_blockchain.html', {
        'pregunta_actual': pregunta_actual['pregunta'],
        'opciones': pregunta_actual['opciones'],
        'preguntas_resueltas': preguntas_resueltas,
        'hay_mas_preguntas': hay_mas_preguntas,
    })

def inicio_flujo_blockchain_view(request):
    # Reiniciar el flujo y las preguntas previas
    request.session['preguntas_resueltas'] = []
    return redirect('flujo_decision_blockchain', paso='necesita_datos_consistentes')


