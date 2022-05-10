from django import forms

class FormularioContacto (forms.Form):
    nombre=forms.CharField(label='Nombre',required=True, max_length=20)
    email=forms.EmailField(label='email',required=True, max_length=100)
    asunto=forms.CharField(label='Asunto',required=True, max_length=20)
    consulta=forms.CharField(label='Consulta',widget=forms.Textarea,required=True, max_length=200)
    
    
