'''
modificacion 
'''

cantidad = int(input("Ingrese la cantidad de cuadernos: "))
precio = float(input("Ingrese el precio de cada cuaderno: "))

total = cantidad * precio

if cantidad >= 10:
    descuento = total * 0.20
elif cantidad >= 5:
    descuento = total * 0.10
else:
    descuento = 0

total_pagar = total - descuento

print("Valor de la compra:", total)
print("Valor del descuento:", descuento)
print("Total a pagar:", total_pagar)