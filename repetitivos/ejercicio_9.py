'''
Ejercicio 9: Promedio de edades por sexo y del grupo
'''

cantidadAlumnos = int(input("Ingrese la cantidad de alumnos: "))

sumaEdadesHombres = 0
sumaEdadesMujeres = 0
sumaEdadesTotal = 0

cantidadHombres = 0
cantidadMujeres = 0
cantidadTotal = 0

# Leer la edad y el sexo de cada alumno
for i in range(1, cantidadAlumnos + 1):
    print("\nAlumno", i)

    sexo = input("Ingrese el sexo (H/M): ").strip().upper()
    edad = int(input("Ingrese la edad: "))

    # Validar la edad
    if edad < 0:
        print("Edad no válida.")
        continue

    # Acumular las edades del grupo
    if sexo == "H":
        sumaEdadesHombres += edad
        cantidadHombres += 1
        sumaEdadesTotal += edad
        cantidadTotal += 1

    elif sexo == "M":
        sumaEdadesMujeres += edad
        cantidadMujeres += 1
        sumaEdadesTotal += edad
        cantidadTotal += 1

    else:
        print("Sexo no válido. No se contabilizó el alumno.")

# Calcular los promedios y mostrar los resultados
if cantidadHombres > 0:
    print("Promedio de edad de hombres:",
          sumaEdadesHombres / cantidadHombres)
else:
    print("No hay hombres registrados.")

if cantidadMujeres > 0:
    print("Promedio de edad de mujeres:",
          sumaEdadesMujeres / cantidadMujeres)
else:
    print("No hay mujeres registradas.")

if cantidadTotal > 0:
    print("Promedio de edad de todo el grupo:",
          sumaEdadesTotal / cantidadTotal)
else:
    print("No hay alumnos registrados.")