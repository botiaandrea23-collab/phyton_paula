'''
APRUEBA O DESAPRUEBA
'''
Nota1 = float(input("Ingrese la primera calificación: "))
Nota2 = float(input("Ingrese la segunda calificación: "))
Nota3 = float(input("Ingrese la tercera calificación: "))

promedio = (Nota1 + Nota2 + Nota3) / 3

print("El promedio es:", promedio)

if promedio >= 70:
    print("El aprendiz APRUEBA la materia")
else:
    print("El aprendiz DESAPRUEBA la materia")