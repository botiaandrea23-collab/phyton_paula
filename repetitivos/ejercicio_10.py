'''
 Ejercicio 10: Multiplicar los primeros 20 números naturales
'''
productoTotal = 1

# Multiplicar los números del 1 al 20
for numero in range(1, 21):
    productoTotal *= numero

    # Mostrar la multiplicación que se va realizando
    if numero == 1:
        print(numero, end="")
    else:
        print("*", numero, end="")

# Mostrar el resultado final
print("\nEl producto de los primeros 20 números naturales es:")
print(productoTotal)