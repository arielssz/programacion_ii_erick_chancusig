# Operadores
"""
Operadores aritméticos:
+ Suma
- Resta
* Multiplicación
/ División
% Módulo (resto de la división)
** (Potencia) 
"""
valor1 = 10
valor2 = 3
suma = valor1 + valor2
resta = valor1 - valor2
multiplicacion = valor1 * valor2
division = valor1 / valor2
modulo = valor1 % valor2
potencia = valor1 ** valor2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Módulo:", modulo)
print("Potencia:", potencia)

print("tabla de multiplicar del 5:")
multiplicador = 5
print(multiplicador, "x 1 =", multiplicador * 1)
print(multiplicador, "x 2 =", multiplicador * 2)
print(multiplicador, "x 3 =", multiplicador * 3)
print(multiplicador, "x 4 =", multiplicador * 4)
print(multiplicador, "x 5 =", multiplicador * 5)
print(multiplicador, "x 6 =", multiplicador * 6)
print(multiplicador, "x 7 =", multiplicador * 7)
print(multiplicador, "x 8 =", multiplicador * 8)
print(multiplicador, "x 9 =", multiplicador * 9)
print(multiplicador, "x 10 =", multiplicador * 10)


print("Area de un triangulo de base 5 y altura 10:", (5 * 10) / 2)


# Operadores de comparación:
"""
- == (igual)
- != (distinto)
- < (menor)
- > (mayor)
- <= (menor o igual)
- >= (mayor o igual)
"""

velocidad_anakin = 950
velocidad_sebulba = 900

print("¿Anakin es más rápido que Sebulba?", velocidad_anakin > velocidad_sebulba)
print("¿Anakin es más lento que Sebulba?", velocidad_anakin < velocidad_sebulba)
print("¿Anakin es igual de rápido que Sebulba?", velocidad_anakin == velocidad_sebulba)
print("¿Anakin es distinto de Sebulba?", velocidad_anakin != velocidad_sebulba)
print("¿Anakin es más rápido o igual que Sebulba?", velocidad_anakin >= velocidad_sebulba)
print("¿Anakin es más lento o igual que Sebulba?", velocidad_anakin <= velocidad_sebulba)

resultado = velocidad_anakin > velocidad_sebulba
print("Resultado de la comparación:", resultado)
print("Tipo de resultado:", type(resultado))

# Operadores lógicos:
"""
- and (y)
- or (o)
- not (no)
"""

motores_funcioando = True
escudos_activados = False
combustible = 80

print("¿Todos los sistemas estan funcionando?", motores_funcioando and escudos_activados)
print("¿Alguno de los sistemas estan fallando?", not motores_funcioando or escudos_activados)
print("¿Los motores no estan funcionando?", not motores_funcioando)

cantidad_motores = 2
cantidad_alas = 4
combustible = 80

print("¿La nave tiene al menos 2 motores y 4 alas?")
print(cantidad_motores >= 2 and cantidad_alas >= 4 and combustible >= 50)
print("¿La nave tiene al menos 2 motores o 4 alas?")
print(cantidad_motores >= 2 or cantidad_alas >= 4 or combustible >= 50)
print("¿La nave no tiene al menos 2 motores?")
print(not cantidad_motores >= 2 and combustible >= 50 and cantidad_alas >= 4)

# Operadores de asignacion
"""
=  (asignación)
+= (suma y asignación)
-= (resta y asignación)
*= (multiplicación y asignación)
/= (división y asignación)
%= (módulo y asignación)
**= (potencia y asignación)
"""
velocidad = 100
print("Velocidad inicial:", velocidad)
velocidad += 50
print("Velocidad después de acelerar:", velocidad)
velocidad -= 30
print("Velocidad después de frenar:", velocidad)
multiplicador = 2
velocidad *= multiplicador
print("Velocidad después de multiplicar:", velocidad)
divisor = 4
velocidad /= divisor
print("Velocidad después de dividir:", velocidad)
modulo = 7
velocidad %= modulo
print("Velocidad después de aplicar módulo:", velocidad)
velocidad **= 2
print("Velocidad después de aplicar potencia:", velocidad)

# PRECEDENCIA DE OPERADORES
"""
1. ()  (paréntesis)
2. **  (potencia)
3. *, /, %, //  (multiplicación, división, módulo, división entera)
4. +, -  (suma, resta)
"""


resultado_1 = 10 + 5 * 2
print("Resultado 1:", resultado_1)
resultado_2 = (10 + 5) * 2
print("Resultado 2:", resultado_2)
resultado_3 = 10 + 5 * 2 ** 2
print("Resultado 3:", resultado_3)