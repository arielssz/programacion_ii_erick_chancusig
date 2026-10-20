##FUNCIONES  
# funciones sin parametros o simples   
def activar_sistema():
    print("SISTEMA DE NABOO/////")
    print("sistema de control activado")

activar_sistema()

#funciones con parametros 

def saludar_jedi(nombre):
    print(f"Que la fuerza te acompañe:{nombre}")

saludar_jedi("Qui-gon Jim")
saludar_jedi("Obi-Wan Kenobi")

def mostrar_nave (nombre, combustible ):
    print(f"nave:{nombre}")
    print(f"cantidad de combustible :{combustible}")
mostrar_nave("Caza-N1", 80)


#Funciones que devuelven dato o informacion 
#return

def calcular_combustible(inicial, consumo):
    restante=inicial-consumo
    return restante
def calcular_combustible2(inicial, consumo):
    return inicial-consumo

resultado =calcular_combustible(100,25)
print (f"combustible:{resultado}")

resultado = calcular_combustible2(100,35)
print (f"combustible:{resultado}")

print (f"combustible:{calcular_combustible2(100,15)}")


def nave_preparada(combustible):
    return combustible>=50

if nave_preparada (80):
    print("Nave autorizada para despegar")
else:
    print("Nave necesita recargar")
    