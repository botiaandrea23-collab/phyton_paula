# Clasificar el rendimiento académico de los estudiantes

for i in range(1, 6):
    nota = float(input(f"Ingrese la nota del estudiante {i} (0 a 100): "))

    # Verificar que la nota esté dentro del rango permitido
    if nota < 0 or nota > 100:
        print("Nota no válida.")
    
    # Clasificar el rendimiento según la nota
    elif nota < 60:
        print("Rendimiento bajo.")

    elif nota < 80:
        print("Rendimiento básico.")

    elif nota < 90:
        print("Rendimiento alto.")

    else:
        print("Rendimiento superior.")