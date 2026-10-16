'''
 Ejercicio 3: Calificaciones de 20 alumnos
 '''

sumaNotas = 0
notaAlta = 0
notaBaja = 0

# Leer las calificaciones de los 20 alumnos
for i in range(1, 21):
    nota = float(input(f"Ingrese la nota del alumno {i}: "))

    # Inicializar la nota mayor y menor con la primera nota
    if i == 1:
        notaAlta = nota
        notaBaja = nota
    else:
        # Comparar para encontrar la nota más alta y más baja
        if nota > notaAlta:
            notaAlta = nota

        if nota < notaBaja:
            notaBaja = nota

    # Acumular las calificaciones
    sumaNotas += nota

# Calcular el promedio del grupo
promedioNotas = sumaNotas / 20

# Mostrar los resultados
print("Promedio del grupo:", promedioNotas)
print("Nota más alta:", notaAlta)
print("Nota más baja:", notaBaja)