from django.shortcuts import render
from django.http import HttpResponse

# 1
def home(request):
    """Vista de bienvenida de la app tasks."""
    return HttpResponse("""
        <html>
            <body>
                <h1>TaskFlow</h1>
                <p>Bienvenido al sistema</p>
            </body>
        </html>
    """)

# 2
def register(request):
    """Registro de usuarios"""
    return HttpResponse("Registro de Usuarios")

# 3
def perfil(request):
    """Vista del perfil de usuario"""
    return HttpResponse("Bienvenido a tu perfil")

def destination(request, titulo, nombre, cargo):
    """Vista con parámetros de destino"""
    return HttpResponse(f"Bienvenido: {titulo} {nombre}, su cargo es: {cargo}")

def base_triangulo(request, base, altura):
    """Cálculo del área de un triángulo"""
    return HttpResponse(f"El área de un triángulo es: {base * altura / 2}")

def my_first_template(request):
    """Vista que renderiza una plantilla HTML"""
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
    }
    return render(request, "tasks/my-first-template.html", contexto)

def about_me(request):
    return HttpResponse("Acerca de mí")

def greeting(request, nombre):
    """Vista que saluda al usuario por su nombre."""
    return HttpResponse(f"¡Hola, {nombre}! Bienvenido a TaskFlow.")

def leads_like(request):
    return render(request, "tasks/leads-like.html")