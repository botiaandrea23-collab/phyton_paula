'''
NUMERO DE PULSACIONES
'''
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo (femenino/masculino): ").lower()

if sexo == "femenino":
    pulsaciones = (220 - edad) / 10
elif sexo == "masculino":
    pulsaciones = (210 - edad) / 10
else:
    pulsaciones = None
    print("El sexo ingresado no es válido")

if pulsaciones is not None:
    print("Pulsaciones por cada 10 segundos:", pulsaciones)