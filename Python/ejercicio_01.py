peso = float(input("Ingresa el peso del paquete en kg: "))
zona = input("Ingresa la zona de destino (1-3): ")

precios_por_zona = {
    "1": 5.0,   # América
    "2": 7.5,   # Europa
    "3": 10.0,  # Resto del mundo
}

if zona in precios_por_zona:
    costo_total = peso * precios_por_zona[zona]
    print(f"El costo final del envío es: ${costo_total:.2f}")
else:
    print("Error: la zona ingresada no es válida. Debe ser 1, 2 o 3.")