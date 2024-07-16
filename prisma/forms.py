from django import forms
from .models import UseCases, BusinessValue, BusinessCalifications, Feasibility, FeasibilityCalifications

class UseCasesForm(forms.ModelForm):
    class Meta:
        model = UseCases
        fields = '__all__'

class RatingForm(forms.Form):
    case_to_rate = forms.ModelChoiceField(queryset=UseCases.objects.all(), label='Selecciona un caso de uso')

    def __init__(self, *args, **kwargs):
        super(RatingForm, self).__init__(*args, **kwargs)
        initial_args = kwargs.get('initial', {})
        columns = initial_args.get('columns', [])
        for column in columns:
            if column not in ['Negocio (X)', 'Viabilidad (Y)']:
                self.fields[f'rating_{column}'] = forms.IntegerField(label=f'Calificación para {column}', min_value=0, max_value=4)