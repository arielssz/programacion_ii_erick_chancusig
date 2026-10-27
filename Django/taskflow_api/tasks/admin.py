from django.contrib import admin
from .models import Project, Empleado


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "apellido",
        "cedula",
        "cargo",
        "departamento",
        "salario",
        "activo",
    )
    search_fields = ("nombre", "apellido", "cedula")
    list_filter = ("departamento", "activo")