from django import forms

class FormularioFechas(forms.Form):
    fecha_inicio = forms.DateField(widget=forms.SelectDateWidget())
    fecha_final = forms.DateField(widget=forms.SelectDateWidget())