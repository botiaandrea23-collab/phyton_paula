'''
Ejercicio 7: Calcular la cantidad de calcomanías por color
'''

cantidadAutos = int(input("Ingrese la cantidad de autos: "))

amarilla = 0
rosa = 0
roja = 0
verde = 0
azul = 0

# Leer el último dígito de la placa de cada auto
for i in range(1, cantidadAutos + 1):
    digito = int(input(
        f"Ingrese el último dígito de la placa del auto {i}: "
    ))

    # Determinar el color según la tabla del taller
    if digito == 1 or digito == 2:
        amarilla += 1

    elif digito == 3 or digito == 4:
        rosa += 1

    elif digito == 5 or digito == 6:
        roja += 1

    elif digito == 7 or digito == 8:
        verde += 1

    elif digito == 9 or digito == 0:
        azul += 1

    else:
        print("Dígito no válido.")

# Mostrar la cantidad de autos por color
print("\nResultados:")
print("Calcomanías amarillas:", amarilla)
print("Calcomanías rosas:", rosa)
print("Calcomanías rojas:", roja)
print("Calcomanías verdes:", verde)
print("Calcomanías azules:", azul)