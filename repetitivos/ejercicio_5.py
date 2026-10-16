'''
Ejercicio 5: Promedio de peso de 50 personas
'''

pesoNinos = 0
pesoJovenes = 0
pesoAdultos = 0
pesoAncianos = 0

cantidadNinos = 0
cantidadJovenes = 0
cantidadAdultos = 0
cantidadAncianos = 0

# Leer la edad y el peso de 50 personas
for i in range(1, 51):
    print("\nPersona", i)
    edad = int(input("Ingrese la edad: "))
    peso = float(input("Ingrese el peso en kilogramos: "))

    # Clasificar a la persona según la tabla del taller
    if edad >= 0 and edad <= 12:
        pesoNinos += peso
        cantidadNinos += 1

    elif edad >= 13 and edad <= 29:
        pesoJovenes += peso
        cantidadJovenes += 1

    elif edad >= 30 and edad <= 59:
        pesoAdultos += peso
        cantidadAdultos += 1

    elif edad >= 60:
        pesoAncianos += peso
        cantidadAncianos += 1

    else:
        print("Edad no válida.")

# Calcular y mostrar el promedio de cada categoría
if cantidadNinos > 0:
    print("Promedio de peso de niños:", pesoNinos / cantidadNinos)
else:
    print("No se registraron niños.")

if cantidadJovenes > 0:
    print("Promedio de peso de jóvenes:", pesoJovenes / cantidadJovenes)
else:
    print("No se registraron jóvenes.")

if cantidadAdultos > 0:
    print("Promedio de peso de adultos:", pesoAdultos / cantidadAdultos)
else:
    print("No se registraron adultos.")

if cantidadAncianos > 0:
    print("Promedio de peso de ancianos:", pesoAncianos / cantidadAncianos)
else:
    print("No se registraron ancianos.")