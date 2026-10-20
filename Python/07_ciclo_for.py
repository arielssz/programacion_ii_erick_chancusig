#ciclo for 
#
naves = [
    "Caza N-1",
    "Nave real de Naboo", 
    "transporte"
]
for nave in naves:
    print("Inspeccionando", nave)


rondas = ["Primera", "Segunda", "Tercera"]

print("tipo de rondas:", type(rondas))  
for ronda in rondas:
    print(f"Ronda de vigilancia: {ronda}")
    print(f"Tipo de dato ronda: {type(ronda)}")  

droides = range(1, 17, 2)

print("tipo de droides:", type(droides))
for droide in droides:
    print(f"Reparar: droide B1-{droide}")
    print(f"Tipo de dato droide: {type(droide)}")

planetas=[ 
    "Naboo",
    "Tatooine",
    "Coruscant"
]

recorrido =enumerate (planetas, start=1)

for posicion, planeta in recorrido:
    print(f"Planeta {posicion}: {planeta}")
    print(f"Tipo de dato planeta: {type(posicion)}: {type(planeta)}")

paises= [
    "Ecuador",
    "Venezuela",
    "Chile",
    "Colombia",
    "Brasil",
    "Estados Unidos"
]

for pais in paises:
    if pais== "Chile":
        continue
    if pais== "Brasil":
        break
    print(f"Pais visitado: {pais}")

jedi_activo = {
    "nombre": "Obiwan",
    "fuerza": 120,
    "estilo_pelea": "samurai",
    "misiones": ["guerra alderan", "secuestro palpatine", "escolta de leia"],
    "descripcion": {
        "estatura": 1.80,
        "especie": "humana"
    }
}

print(jedi_activo["nombre"])
print(jedi_activo["descripcion"]["especie"])

jedi_activo["nombre"] = "Luck"
jedi_activo["fuerza"] = 150
print(jedi_activo)

for clave, valor in jedi_activo.items():
    print(f"{clave} - {valor}")
