'''
VENTA DE LLANTAS
'''
cantidad = int(input("Ingrese la cantidad de llantas: "))

if cantidad < 5:
    precio = 300000
elif cantidad <= 10:
    precio = 250000
else:
    precio = 200000

total = cantidad * precio

print("Cantidad de llantas:", cantidad)
print("Precio por llanta:", precio)
print("Total a pagar:", total)