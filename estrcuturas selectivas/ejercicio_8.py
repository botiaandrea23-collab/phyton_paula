'''
HEMOGLOBINA
'''

Genero = input("Genero F/M ")
CantidadHemoglobina = float(input("Ingrese nivel de hemoglobina"))
print("OPCIONES DE EDAD")
print("1. 0 - 1 mes")
print("2. > 1 y < = 6 meses ")
print("3. > 6 y < = 12 meses")
print("4. > 1 y < = 5 años")
print("5. > 5 y < = 10 años")
print("6. > 10 y < = 15 años ")
print("7. mujeres > 15 años")
print("8. hombres > 15 años")
opcion= int(input("Ingrese numero 1-8 "))
match opcion:
    case 1:
        if CantidadHemoglobina < 13:
                print("Tienes Anemia")
        else:
                print("No tiene Anemia")
    case 2:
        if CantidadHemoglobina < 10:
                 print("Tienes Anemia")
        else:
                print("No tiene Anemia")
    case 3:
        if CantidadHemoglobina < 11:
                print("Tienes Anemia")
        else:
                 print("No tiene Anemia")
    case 4:
        if CantidadHemoglobina < 11.5:
                print("Tienes Anemia")
        else:
                print("No tiene Anemia")
    case 5:
        if CantidadHemoglobina < 12.6:
                print("Tienes Anemia")
        else:
                print("No tiene Anemia")
    case 6:
        if CantidadHemoglobina < 13:
                print("Tienes Anemia")
        else:
                print("No tiene Anemia")
    case 7:
        if CantidadHemoglobina < 12:
                print("Tienes Anemia")
        else:
                print("No tiene Anemia")
    case 8:
        if CantidadHemoglobina < 14:
                print("positivo para anemia")
        else:
                print("negativo para anemia")