flota = [
    {"N1-001": {"nombre": "caza N-1", "combustible": 80}},
    {"N2-002": {"nombre": "Nave Real", "combustible": 35}},
]


def create_nave(nueva_nave):
    flota.append(nueva_nave)
    return nueva_nave


def read_nave(index):
    return flota[index]


def update_nave(index, nave_actualizada):
    if 0 <= index < len(flota):
        flota[index].update(nave_actualizada)
        return flota[index]
    return None


def delete_nave(index):
    if 0 <= index < len(flota):
        return flota.pop(index)
    return None


print("Flota inicial:")
print(flota)
print("Primera nave:", read_nave(0))

nueva_nave = {"NR-003": {"nombre": "Nave real 2", "combustible": 80}}
create_nave(nueva_nave)
print("Después de crear:")
print(flota)

nave_actualizada = {"NR-006": {"nombre": "Nave Real NR6", "combustible": 85}}
update_nave(2, nave_actualizada)
print("Después de actualizar:")
print(flota)

print("Nave leída:", read_nave(2))
print("Nave eliminada:", delete_nave(2))
print("Flota final:")
print(flota)


