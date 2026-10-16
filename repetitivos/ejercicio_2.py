'''
números negativos y convertirlos a positivos
'''

sumaNumeros = 0

# Leer 10 números negativos
for i in range(1, 11):
    numero = float(input(f"Ingrese el número negativo {i}: "))

    # Verificar que el número sea negativo
    while numero >= 0:
        print("El número debe ser negativo.")
        numero = float(input("Ingrese nuevamente el número: "))

    # Convertir el número negativo a positivo
    numeroPositivo = abs(numero)

    # Acumular los números positivos
    sumaNumeros += numeroPositivo

    print("Número convertido a positivo:", numeroPositivo)

# Mostrar la suma total
print("La suma de los números positivos es:", sumaNumeros)