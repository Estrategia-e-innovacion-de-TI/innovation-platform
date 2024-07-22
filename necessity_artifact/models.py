from django.db import models
from multiselectfield import MultiSelectField


class InnovacionFormulario(models.Model):


    FASE_INNOVACION_CHOICES = [
        ('1. Identificación de la necesidad o problema', '1. Identificación de la necesidad o problema'),
        ('2. Generación de ideas', '2. Generación de ideas'),
        ('3. Selección de ideas', '3. Selección de ideas'),
        ('4. Desarrollo del prototipo', '4. Desarrollo del prototipo'),
        ('5. Pruebas y validación', '5. Pruebas y validación'),
        ('6. Implementación', '6. Implementación')
    ]
    PROPOSITO_INICIATIVA_CHOICES = [
        ('Análisis de tendencias', 'Análisis de tendencias'),
        ('Comprender necesidades de usuarios', 'Comprender necesidades de usuarios'),
        ('Generación de ideas', 'Generación de ideas'),
        ('Identificación de oportunidades de mercado', 'Identificación de oportunidades de mercado'),
        ('Evaluación de competencia', 'Evaluación de competencia'),
        ('Innovación tecnológica', 'Innovación tecnológica'),
        ('Conocimiento del usuario', 'Conocimiento del usuario'),
        ('Segmentación de nichos de mercado', 'Segmentación de nichos de mercado'),
        ('Innovación disruptiva', 'Innovación disruptiva')
    ]


    URGENCY_CHOICES = [
        ('1', '1 - Muy bajo: No hay presión para implementar la solución rápidamente.'),
        ('2', '2 - Bajo: La implementación puede esperar un poco más, no es una prioridad inmediata.'),
        ('3', '3 - Moderado: Existe cierta presión para implementar la solución en un plazo razonable.'),
        ('4', '4 - Alto: Se necesita una implementación relativamente rápida para abordar el problema.'),
        ('5', '5 - Muy Alto: La situación es urgente y se necesita una solución inmediata.'),
    ]

    COMPLEXITY_CHOICES = [
        ('1', '1 - Muy bajo: El problema es simple y bien definido.'),
        ('2', '2 - Bajo: La complejidad en mínima y se entiende claramente.'),
        ('3', '3 - Moderado: Hay algunas áreas de complejidad, pero en su mayoría está bien definido.'),
        ('4', '4 - Alto: El problema es complejo y requiere una comprensión detallada para abordarlo.'),
        ('5', '5 - Muy Alto: La complejidad es extremadamente alta y el problema es difícil de definir.'),
    ]

    UNCERTAINTY_CHOICES = [
        ('1', '1 - Muy bajo: Hay una comprensión completa del problema y las soluciones posibles.'),
        ('2', '2 - Bajo: Se tiene una idea general, pero hay cierta incertidumbre sobre las soluciones.'),
        ('3', '3 - Moderado: Existen algunas áreas de incertidumbre, pero en su mayoría se tiene una comprensión razonable del problema.'),
        ('4', '4 - Alto: Hay una cantidad significativa de incertidumbre sobre el problema y las soluciones.'),
        ('5', '5 - Muy Alto: La incertidumbre es extremadamente alta y no se comprende completamente el problema o las posibles soluciones.'),
    ]

    COLLABORATION_CHOICES = [
        ('1', '1 - Muy bajo: No se requiere colaboración significativa, el proyecto es manejable por un solo equipo.'),
        ('2', '2 - Bajo: Se necesitará alguna colaboración, pero los equipos pueden trabajar de forma independiente en su mayoría.'),
        ('3', '3 - Moderado: La colaboración entre equipos es importante, pero no es crítica para el éxito.'),
        ('4', '4 - Alto: La colaboración es esencial y varios equipos deben trabajar estrechamente juntos.'),
        ('5', '5 - Muy Alto: La colaboración entre múltiples equipos es absolutamente crucial para el éxito del proyecto.'),
    ]

    RESOURCES_CHOICES = [
        ('1', '1 - Muy bajo: Recursos muy limitados, es difícil obtener lo que se necesita.'),
        ('2', '2 - Bajo: Los recursos son escasos, pero se pueden obtener con esfuerzo.'),
        ('3', '3 - Moderado: Los recursos están disponibles, pero con algunas restricciones.'),
        ('4', '4 - Alto: Hay suficientes recursos disponibles para llevar a cabo el proyecto.'),
        ('5', '5 - Muy Alto: Recursos abundantes y fácilmente accesibles para apoyar el proyecto.'),
    ]

    FLEXIBILITY_CHOICES = [
        ('1', '1 - Muy bajo: Se espera que el alcance del proyecto permanezca relativamente constante.'),
        ('2', '2 - Bajo: Puede haber algunos cambios menores, pero el alcance general se mantendrá.'),
        ('3', '3 - Moderado: Se esperan algunos cambios significativos, pero el alcance general permanecerá similar.'),
        ('4', '4 - Alto: Se anticipan cambios importantes en el alcance del proyecto.'),
        ('5', '5 - Muy Alto: La flexibilidad es fundamental, se esperan cambios drásticos en el alcance del proyecto.'),
    ]

    SPEED_CHOICES = [
        ('1', '1 - Muy bajo: La velocidad de implementación no es una prioridad.'),
        ('2', '2 - Bajo: Se prefiere una implementación más rápida, pero no es crítica.'),
        ('3', '3 - Moderado: La implementación oportuna es importante para el éxito del proyecto.'),
        ('4', '4 - Alto: Se necesita una implementación rápida para obtener beneficios rápidos.'),
        ('5', '5 - Muy Alto: La velocidad de implementación es esencial y se espera que sea lo más rápido posible.'),
    ]

    RISK_CHOICES = [
        ('1', '1 - Muy bajo: Riesgo mínimo, el fracaso no tendría un gran impacto.'),
        ('2', '2 - Bajo: Algunos riesgos, pero manejables y el impacto de un fracaso sería moderado.'),
        ('3', '3 - Moderado: Riesgos significativos, un fracaso tendría un impacto considerable.'),
        ('4', '4 - Alto: Riesgo alto, un fracaso tendría un impacto importante en el proyecto.'),
        ('5', '5 - Muy Alto: Riesgo extremadamente alto, un fracaso tendría consecuencias catastróficas.'),
    ]

    USER_CHOICES = [
        ('1', '1 - Muy bajo: No se tiene información alguna sobre los usuarios.'),
        ('2', '2 - Bajo: Hay una comprensión superficial de los usuarios, pero se requiere más investigación.'),
        ('3', '3 - Moderado: Se dispone de alguna información sobre los usuarios, pero se necesitan más detalles para comprender completamente sus necesidades.'),
        ('4', '4 - Alto: Existe una comprensión significativa de los usuarios y sus necesidades, pero aún se pueden requerir ajustes adicionales.'),
        ('5', '5 - Muy Alto: Se posee un conocimiento profundo y detallado de los usuarios, incluyendo sus necesidades, deseos y comportamientos.'),
    ]


    descripcion_iniciativa = models.TextField()
    objetivos_clave = models.TextField()
    fase_innovacion = MultiSelectField(choices=FASE_INNOVACION_CHOICES)
    proposito_iniciativa = MultiSelectField(choices=PROPOSITO_INICIATIVA_CHOICES)

    urgencia = models.CharField(max_length=1, choices=URGENCY_CHOICES)
    complejidad = models.CharField(max_length=1, choices=COMPLEXITY_CHOICES)
    incertidumbre = models.CharField(max_length=1, choices=UNCERTAINTY_CHOICES)
    colaboracion = models.CharField(max_length=1, choices=COLLABORATION_CHOICES)
    recursos = models.CharField(max_length=1, choices=RESOURCES_CHOICES)
    flexibilidad = models.CharField(max_length=1, choices=FLEXIBILITY_CHOICES)
    velocidad = models.CharField(max_length=1, choices=SPEED_CHOICES)
    riesgo = models.CharField(max_length=1, choices=RISK_CHOICES)
    usuario = models.CharField(max_length=1, choices=USER_CHOICES)



class ResultadosInnovacion(models.Model):
    data= models.TextField(default = ' ', null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    

