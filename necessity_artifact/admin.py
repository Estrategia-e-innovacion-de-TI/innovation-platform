from django.contrib import admin
from .models import InnovacionFormulario, ResultadosInnovacion
from .forms import InnovacionFormularioForm, ResultadosInnovacionForm

class InnovacionFormularioAdmin(admin.ModelAdmin):
    form = InnovacionFormularioForm  # Use the custom form in the admin
    list_filter = ('fase_innovacion',)
    search_fields = ('descripcion_iniciativa', 'objetivos_clave')

admin.site.register(InnovacionFormulario, InnovacionFormularioAdmin)


class ResultadosInnovacionAdmin(admin.ModelAdmin):
    results = ResultadosInnovacionForm
    list_filter = ('created_at',)

admin.site.register(ResultadosInnovacion, ResultadosInnovacionAdmin)