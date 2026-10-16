'''
Ejercicio 1: contar numeros positos,negativos y neutros
'''

positivos = 0
negativos = 0
neutros = 0

# Leer 20 números
for i in range(1, 21):
    numero = float(input(f"Ingrese el número {i}: "))

    # Clasificar cada número
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        neutros += 1

# Mostrar los resultados
print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)
print("Cantidad de neutros:", neutros)