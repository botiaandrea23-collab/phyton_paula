'''
FABRICA DE BOLSOS
'''
compra = float(input("Ingrese el monto total de la compra: "))

if compra > 500000:
    propio = compra * 0.55
    banco = compra * 0.30
    fabricante = compra * 0.15
    print("Dinero propio:", propio)
    print("Préstamo del banco:", banco)
    print("Crédito del fabricante:", fabricante)
else:
    propio = compra * 0.70
    fabricante = compra * 0.30
    intereses = fabricante * 0.20
    total_credito = fabricante + intereses
    print("Dinero propio:", propio)
    print("Crédito del fabricante:", fabricante)
    print("Intereses del fabricante:", intereses)
    print("Crédito con intereses:", total_credito)