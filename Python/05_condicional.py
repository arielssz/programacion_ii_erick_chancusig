# Condicional if
# Simple

combustible = 5
if combustible >= 10:
    print("Puedes despegar")

# Condicional if-else

creditos = int(input("Ingresa la cantidad de créditos que tienes: "))
precio_repuesto = int(input("Ingresa el precio del repuesto: "))
if creditos >= precio_repuesto:
    print("Puedes comprar el repuesto")
else:
    print("No tienes suficientes créditos para comprar el repuesto")

# if anidado
if creditos >= precio_repuesto:
    print("Puedes comprar el repuesto")
    if creditos > precio_repuesto:
        print("Te sobran créditos")
    else:
        print("Te quedas justo con los créditos necesarios")
else:
    print("No tienes suficientes créditos para comprar el repuesto")

# Condicional if-elif-else

if creditos > precio_repuesto:
    print("Puedes comprar el repuesto y te sobran créditos")
elif creditos == precio_repuesto:
    print("Puedes comprar el repuesto y te quedas justo con los créditos necesarios")
else:
    print("No tienes suficientes créditos para comprar el repuesto")


tipo_repuesto = input("Ingresa el tipo de repuesto (motor, ala, escudo): ")
if tipo_repuesto in ("motor", "ala", "escudo"):
    if creditos > precio_repuesto:
        print("Puedes comprar el repuesto y te sobran créditos")
    elif creditos == precio_repuesto:
        print("Puedes comprar el repuesto y te quedas justo con los créditos necesarios")
    else:
        print("No tienes suficientes créditos para comprar el repuesto")
else:
    print("Tipo de repuesto no válido")