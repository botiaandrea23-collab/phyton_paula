'''
 Ejercicio 4: Tabla de multiplicar de un número
'''

numero = int(input("Ingrese el número para multiplicar: "))

# Generar la tabla del 1 al 10
for multiplicador in range(1, 11):
    producto = numero * multiplicador

    # Mostrar multiplicando, multiplicador y producto
    print(numero, "x", multiplicador, "=", producto)