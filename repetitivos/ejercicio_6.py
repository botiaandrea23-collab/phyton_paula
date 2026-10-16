'''
Ejercicio 6: Contar hombres y mujeres de un salón
'''

cantidadPersonas = int(input("Ingrese el total de personas: "))

hombres = 0
mujeres = 0

# Leer el sexo de cada persona
for i in range(1, cantidadPersonas + 1):
    sexo = input(
        f"Ingrese el sexo de la persona {i} (H/M): "
    ).strip().upper()

    # Contar según el sexo ingresado
    if sexo == "H":
        hombres += 1

    elif sexo == "M":
        mujeres += 1

    else:
        print("Dato no válido. Ingrese H o M.")
        
# Mostrar los resultados
print("Cantidad de hombres:", hombres)
print("Cantidad de mujeres:", mujeres)