# Programa para realizar los operadores, usando diferentes formulas

print("---------------------------------------")
print("--EL RESULTADO DE LAS OPERACIONES SON--")
print("---------------------------------------")
# input
nc = int(input("Digite el valor de la nota prosedimental: "))
cp = int(input("Digite el valor de cognitivo: "))
na = int(input("Digite el valor de actitudinal: "))
au = int(input("Digite el valor de autoevaluacion: "))
bi = int(input("Digite el valor de bimestral: "))
# processing
nd =(0.3*nc) + (0.3*cp) + (0.1*na) + (0.1*au) + (0.2*bi)
# output
print("-----------------------")
print("------RESULTADOS-------")
print("-----------------------")
print("NOTA DEFINITIVA " + str(nd))
