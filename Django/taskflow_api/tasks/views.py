from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """vISITA DE BIENVENIDA DE LA APP DE TASK."""
    return HttpResponse("Hola, Taskflow")

def register(request):
    """REGISTRO DE USUARIO."""
    return HttpResponse("Registro de usuario")

def about_me(request):
    """INFORMACION DEL DESARROLLADOR."""
    return HttpResponse("Erick Ariel")

def greeting(request, nombre):
    """Registro de usuarios."""
    return HttpResponse(f"Hola, {nombre}, Bienvenido a Taskflow")

def home(request):
    """Vista de bienvenida de la app de Taskflow."""
    return HttpResponse("""
        <html>
            <body>
                <h1>Bienvenido a Taskflow</h1>
                <p>¡Bienvenido al sistema!</p>
            </body>
        </html>
    """)