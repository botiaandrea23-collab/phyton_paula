'''
Ejercicio 8: Clasificar las notas de 23 estudiantes
'''

menores50 = 0
desde50Hasta69 = 0
desde70Hasta79 = 0
desde80 = 0

# Leer las notas de los 23 estudiantes
for i in range(1, 24):

    # Validar que la nota esté entre 1 y 100
    while True:
        nota = float(input(
            f"Ingrese la nota del estudiante {i} (1-100): "
        ))

        if nota >= 1 and nota <= 100:
            break
        else:
            print("Error: la nota debe estar entre 1 y 100.")

    # Clasificar la nota según el intervalo
    if nota < 50:
        menores50 += 1

    elif nota < 70:
        desde50Hasta69 += 1

    elif nota < 80:
        desde70Hasta79 += 1

    else:
        desde80 += 1

# Mostrar los resultados finales
print("\nResultados del examen:")
print("Notas menores de 50:", menores50)
print("Notas de 50 a menos de 70:", desde50Hasta69)
print("Notas de 70 a menos de 80:", desde70Hasta79)
print("Notas de 80 o más:", desde80)