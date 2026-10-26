'''
COMPRA DE ZAPATILLAS
'''
cantidad = int (input("Ingrese la cantidad de zapatillas: "))
precio = float (input("Ingrese el precio de cada zapatilla: "))

total = cantidad * precio

if cantidad >= 3:
    descuento = total * 0.20
else:
    descuento = total * 0.10

total_pagar = total - descuento

print("Valor de la compra:", total)
print("Valor del descuento:", descuento)
print("Total a pagar:", total_pagar)