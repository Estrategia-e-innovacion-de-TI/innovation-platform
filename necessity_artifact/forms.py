from django import forms
from .models import InnovacionFormulario
from .models import ResultadosInnovacion

class ResultadosInnovacionForm(forms.ModelForm):
    class Meta:
        model = ResultadosInnovacion
        fields = ['data']
        
        

class InnovacionFormularioForm(forms.ModelForm):

    urgencia = forms.ChoiceField(choices=InnovacionFormulario.URGENCY_CHOICES)
    complejidad = forms.ChoiceField(choices=InnovacionFormulario.COMPLEXITY_CHOICES)#widget=forms.RadioSelect
    incertidumbre = forms.ChoiceField(choices=InnovacionFormulario.UNCERTAINTY_CHOICES)
    usuario = forms.ChoiceField(choices=InnovacionFormulario.USER_CHOICES)
    riesgo = forms.ChoiceField(choices=InnovacionFormulario.RISK_CHOICES)
    velocidad = forms.ChoiceField(choices=InnovacionFormulario.SPEED_CHOICES)
    flexibilidad = forms.ChoiceField(choices=InnovacionFormulario.FLEXIBILITY_CHOICES)
    recursos = forms.ChoiceField(choices=InnovacionFormulario.RESOURCES_CHOICES)
    colaboracion = forms.ChoiceField(choices=InnovacionFormulario.COLLABORATION_CHOICES)


    class Meta:
        model = InnovacionFormulario
        fields = [
            'descripcion_iniciativa', 'objetivos_clave', 'fase_innovacion',
            'proposito_iniciativa', 'urgencia', 'complejidad', 'incertidumbre',
            'colaboracion', 'recursos', 'flexibilidad',
            'velocidad', 'riesgo', 'usuario'
        ]

        widgets = {
            'descripcion_iniciativa': forms.TextInput(attrs={'class': 'form-control'}),
            'objetivos_clave': forms.TextInput(attrs={'class': 'form-control'}),
            'fase_innovacion': forms.CheckboxSelectMultiple,
            'proposito_iniciativa': forms.CheckboxSelectMultiple,
            'urgencia': forms.RadioSelect,
            'complejidad': forms.RadioSelect,
            'incertidumbre': forms.RadioSelect,
            'colaboracion': forms.RadioSelect,
            'recursos': forms.RadioSelect,
            'flexibilidad': forms.RadioSelect,
            'velocidad': forms.RadioSelect,
            'riesgo': forms.RadioSelect,
            'usuario': forms.RadioSelect,
        }
