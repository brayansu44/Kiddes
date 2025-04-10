from django import forms
from .models import *

class TelaForm(forms.ModelForm):
    class Meta:
        model = Tela
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['proveedor'].empty_label = "Seleccione un proveedor"
        self.fields['proveedor'].widget.attrs.update({'class': 'form-select'}) 

class RolloTelaForm(forms.ModelForm):
    fecha_registro = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local', 'class': 'form-control'}
        ),
        required=True 
    )

    class Meta:
        model = RolloTela
        fields = [
            'numero_rollo', 'numero_referencia', 'referencia', 
            'tela', 'metros_solicitados', 'largo_inicial', 
            'kilos', 'fecha_registro'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

            if field.required:
                field.label = f"<strong>{field.label if field.label else field_name}</strong>"

        self.fields['tela'].empty_label = "Seleccione una tela"
        self.fields['tela'].widget.attrs.update({'class': 'form-select'})

from django import forms
from .models import OrdenProduccion

class OrdenProduccionForm(forms.ModelForm):
    class Meta:
        model = OrdenProduccion
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

            if field.required:
                field.label = f"<strong>{field.label if field.label else field_name}</strong>"

        self.fields['producto'].empty_label = "Seleccione una referencia"
        self.fields['producto'].widget.attrs.update({'class': 'form-select'})

        self.fields['cortador'].empty_label = "Seleccione un cortador"
        self.fields['cortador'].widget.attrs.update({'class': 'form-select'})            

        if 'observaciones' in self.fields:
            observaciones_field = self.fields.pop('observaciones')  
            self.fields['observaciones'] = observaciones_field 

