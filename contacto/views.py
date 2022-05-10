import re
from django.shortcuts import redirect, render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    formulario_contacto=FormularioContacto()

    if request.method == 'POST':
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get('nombre')
            email=request.POST.get('email')
            asunto=request.POST.get('asunto')
            consulta=request.POST.get('consulta')
            
            email=EmailMessage('Mensaje usuario',
                    'El usuario con nombre {} y email {} ha realizado una consulta con asunto{} y con el siguiente contenido:\n\n {}'.format(nombre, email,asunto,consulta),
                    '',
                    ['prilom1984@gmail.com'],
                    reply_to=[email],
                    )
            #try: 
            email.send()
            return redirect("/contacto/?valido")

            """except:
                return redirect("/contacto/?novalido")"""
            
    return render(request, 'contacto/contacto.html', {'miFormulario': FormularioContacto})
 