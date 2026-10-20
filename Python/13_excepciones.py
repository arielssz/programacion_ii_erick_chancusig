print("========CONTROL DE ENERGIA==========")
energia_texto="ochenta"
try:
    energia=int(energia_texto)
    print(energia)
except ValueError:
    print("Error:debe ser numerico")


print("Fin del sistema")

"""
ValueError
typeError
KeyError
IndexError
ZeroDivison 
"""


def calcular_energia(total, cantidad):
    try:
        resultado=total/cantidad
    except ZeroDivisionError as Error:
        print("Error:division entre cero", Error)
        return None

    except TypeError:
        print("Error:valores numericos")
        return None

print ("Caso 1:", calcular_energia (100,4))
print ("Caso 2:", calcular_energia (100,0))
print ("Caso 3:", calcular_energia (100,"cuatro"))

print ("========DIAGNOSTICO R2-D2==========")
try:
    energia=int(90)
    print("energia", energia)
except ValueError:
    print ("Error de lectura")
else:
    print("diagnostico completado")
finally:
    print("Cerrando diagnostico")
    