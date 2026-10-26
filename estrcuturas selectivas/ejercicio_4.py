'''
SUPERMERCADO
'''
compra = float(input("Ingrese el valor de la compra: "))
color = input("Ingrese el color de la balota: ").lower()

if color == "rojo":
    descuento = compra * 0.15
elif color == "verde":
    descuento = compra * 0.20
else:
    descuento = 0

total_pagar = compra - descuento

print("Valor de la compra:", compra)
print("Color de la balota:", color)
print("Descuento:", descuento)
print("Total a pagar:", total_pagar)