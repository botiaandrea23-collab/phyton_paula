'''
PENSION
'''
promedio = float(input("Ingrese el promedio del alumno: "))
pension = float(input("Ingrese el valor de la pensión: "))

if promedio >= 4.0:
    descuento = pension * 0.30
    total = pension - descuento
    print("Descuento aplicado:", descuento)
else:
    iva = pension * 0.10
    total = pension + iva
    print("IVA:", iva)

print("Total a pagar:", total)