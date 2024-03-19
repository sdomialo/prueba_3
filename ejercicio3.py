class NaveEspacial:
    def __init__(self, nombre, longitud, tripulantes, pasajeros):
        self.nombre = nombre
        self.longitud = longitud
        self.tripulantes = tripulantes
        self.pasajeros = pasajeros

    def __str__(self):
        return f"Nave: {self.nombre}, Longitud: {self.longitud}, Tripulantes: {self.tripulantes}, Pasajeros: {self.pasajeros}"


naves = [
    NaveEspacial("Estrella de la Aurora", 50, 10, 100),
    NaveEspacial("Sombra del Alba", 70, 8, 120),
    NaveEspacial("Viento Estelar", 90, 15, 150),
    NaveEspacial("Serenidad Celestial", 60, 5, 80),
    NaveEspacial("Galaxia Errante", 40, 4, 60),
    NaveEspacial("Llamarada Cósmica", 80, 12, 200),
    NaveEspacial("Ocaso Interplanetario", 55, 9, 130),
]

naves_ordenadas = sorted(naves, key=lambda x: (x.nombre, -x.longitud))
print("Naves ordenadas:")
for nave in naves_ordenadas:
    print(nave)


print("\nInformación de las naves 'Sombra del Alba' y 'Viento Estelar':")
for nave in naves:
    if nave.nombre == "Sombra del Alba" or nave.nombre == "Viento Estelar":
        print(nave)


top_pasajeros = sorted(naves, key=lambda x: x.pasajeros, reverse=True)[:5]
print("\nLas cinco naves con mayor cantidad de pasajeros:")
for nave in top_pasajeros:
    print(nave)


nave_mayor_tripulacion = max(naves, key=lambda x: x.tripulantes)
print("\nLa nave que requiere la mayor cantidad de tripulación:")
print(nave_mayor_tripulacion)


naves_con_gx = [nave for nave in naves if nave.nombre.startswith("Serenidad Celestial")]
print("\nNaves cuyo nombre comienza con 'Srenidad Celestial':")
for nave in naves_con_gx:
    print(nave)


naves_seis_pasajeros = [nave for nave in naves if nave.pasajeros >= 6]
print("\nNaves que pueden llevar seis o más pasajeros:")
for nave in naves_seis_pasajeros:
    print(nave)


nave_mas_pequena = min(naves, key=lambda x: x.longitud)
nave_mas_grande = max(naves, key=lambda x: x.longitud)
print("\nLa nave más pequeña:")
print(nave_mas_pequena)
print("\nLa nave más grande:")
print(nave_mas_grande)

if __name__ == "__main__":
    class NaveEspacial:
        def __init__(self, nombre, longitud, tripulantes, pasajeros):
            self.nombre = nombre
            self.longitud = longitud
            self.tripulantes = tripulantes
            self.pasajeros = pasajeros
        def __str__(self):
            return f"Nave: {self.nombre}, Longitud: {self.longitud}, Tripulantes: {self.tripulantes}, Pasajeros: {self.pasajeros}"
    naves = [
     NaveEspacial("Estrella de la Aurora", 50, 10, 100),
     NaveEspacial("Sombra del Alba", 70, 8, 120),
     NaveEspacial("Viento Estelar", 90, 15, 150),
     NaveEspacial("Serenidad Celestial", 60, 5, 80),
     NaveEspacial("Galaxia Errante", 40, 4, 60),
     NaveEspacial("Llamarada Cósmica", 80, 12, 200),
     NaveEspacial("Ocaso Interplanetario", 55, 9, 130),
    ]
   
    naves_ordenadas = sorted(naves, key=lambda x: (x.nombre, -x.longitud))
    print("Naves ordenadas:")
    for nave in naves_ordenadas:
        print(nave)
  
    print("\nInformación de las naves 'Sombra del Alba' y 'Viento Estelar':")
    for nave in naves:
        if nave.nombre == "Sombra del Alba" or nave.nombre == "Viento Estelar":
            print(nave)
   
    top_pasajeros = sorted(naves, key=lambda x: x.pasajeros, reverse=True)[:5]
    print("\nLas cinco naves con mayor cantidad de pasajeros:")
    for nave in top_pasajeros:
        print(nave)
    
    nave_mayor_tripulacion = max(naves, key=lambda x: x.tripulantes)
    print("\nLa nave que requiere la mayor cantidad de tripulación:")
    print(nave_mayor_tripulacion)
 
    naves_con_gx = [nave for nave in naves if nave.nombre.startswith("Serenidad Celestial")]
    print("\nNaves cuyo nombre comienza con 'Serenidad Celestial':")
    for nave in naves_con_gx:
        print(nave)
   
    naves_seis_pasajeros = [nave for nave in naves if nave.pasajeros >= 6]
    print("\nNaves que pueden llevar seis o más pasajeros:")
    for nave in naves_seis_pasajeros:
        print(nave)
  
    nave_mas_pequena = min(naves, key=lambda x: x.longitud)
    nave_mas_grande = max(naves, key=lambda x: x.longitud)
    print("\nLa nave más pequeña:")
    print(nave_mas_pequena)
    print("\nLa nave más grande:")
    print(nave_mas_grande)