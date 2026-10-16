'''
 Ejercicio 11: Registrar datos de los alumnos
'''

hombres = 0
mujeres = 0
sumaAlturas = 0
cantidadAlumnos = 0
alturasMayores170 = 0
alturasMenoresIguales150 = 0

# Registrar alumnos hasta que se ingrese la edad 0
while True:
    edad = int(input("Ingrese la edad (0 para finalizar): "))

    # Finalizar el programa cuando la edad sea 0
    if edad == 0:
        break

    # Validar que la edad no sea negativa
    if edad < 0:
        print("La edad no es válida.")
        continue

    sexo = input("Ingrese el sexo (H/M): ").strip().upper()
    altura = float(input("Ingrese la altura en metros: "))

    # Contar hombres y mujeres
    if sexo == "H":
        hombres += 1
    elif sexo == "M":
        mujeres += 1
    else:
        print("Sexo no válido.")

    # Acumular las alturas
    sumaAlturas += altura
    cantidadAlumnos += 1

    # Contar alumnos según su altura
    if altura > 1.70:
        alturasMayores170 += 1

    if altura <= 1.50:
        alturasMenoresIguales150 += 1

# Mostrar los resultados finales
print("\nResultados:")
print("Cantidad de hombres:", hombres)
print("Cantidad de mujeres:", mujeres)

# Calcular la altura promedio
if cantidadAlumnos > 0:
    promedioAltura = sumaAlturas / cantidadAlumnos
    print("Altura promedio:", promedioAltura, "metros")
else:
    print("No se registraron alumnos.")

print("Alumnos con altura mayor a 1.70 m:",
      alturasMayores170)
print("Alumnos con altura menor o igual a 1.50 m:",
      alturasMenoresIguales150)