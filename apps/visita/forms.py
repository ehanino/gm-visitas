
from django.forms import ModelForm
from django import forms

from .models import Visita

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        exclude = ('id',)
        widgets = {
            'visitante': forms.TextInput(attrs={'class': 'input no-focus width-150 for-username', 'placeholder': 'Visitante'}),
            'visitante_doc': forms.TextInput(attrs={'class': 'input no-focus width-150', 'placeholder': 'Nro. documento'}),
            'entidad': forms.TextInput(attrs={'class': 'input no-focus width-150', 'placeholder': 'Entidad'}),
            'motivo': forms.Textarea(attrs={'class': 'input width-950 no-focus for-username', 'placeholder': 'Motivo de visita', 'rows': 4, 'cols': 0}),
            'funcionario': forms.TextInput(attrs={'class': 'input no-focus width-150', 'placeholder': 'Funcionario'}),
            'funcionario_doc': forms.TextInput(attrs={'class': 'input no-focus width-150', 'placeholder': 'Nro. documento'}),
            'area': forms.TextInput(attrs={'class': 'input no-focus width-150', 'placeholder': 'Área'}),
            'sucursal': forms.TextInput(attrs={'class': 'input no-focus width-150', 'placeholder': 'Sucursal'}),
            'fecha': forms.TextInput(attrs={'class': 'input no-focus width-150', 'placeholder': 'Fecha'}),
            'hora_ing': forms.TextInput(attrs={'class': 'input no-focus width-150', 'placeholder': 'Hora ing.'}),
            'hora_salida': forms.TextInput(attrs={'class': 'input no-focus width-150', 'placeholder': 'Hora sal.'}),
        }

    def __init__(self, *args, **kwargs):
        super(VisitaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False

    def clean(self):
        cleaned_data = super().clean()
        # Aquí puedes agregar validaciones personalizadas
        return cleaned_data

class UploadExcelForm(forms.Form):
    archivo = forms.FileField(label='Selecciona el archivo Excel')