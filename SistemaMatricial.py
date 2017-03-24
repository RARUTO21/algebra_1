# Ejecutar el comando "pip install sympy"
from sympy import *
from fractions import Fraction

# La formula a calcular en esta funciones AX+B=C, si es
# A es invertible, multiplica por (A^-1)AX+B=(A^-1)C y
# luego sabiendo que la matriz por su inversa es la
# identidad y que la identidad por cualquier matriz
# se mantiene la matriz entonces es solo de pasar el B
# a restar, quedaría así: X=(A^-1)C-B
orden = 0


def sistemaMatricial(matrizA, matrizB, matrizC):
    global orden
    # Estas son matrices solo de prueba, porque ya vendrian como parametro
    matrizA = [[Fraction(3, 2), Fraction(4, 5)], [Fraction(0, 1), Fraction(1, 1)]]
    matrizB = [[Fraction(3, 1), Fraction(2, 3)], [Fraction(6, 1), Fraction(4, 1)]]
    matrizC = [[Fraction(3, 1), Fraction(2, 1)], [Fraction(6, 1), Fraction(4, 1)]]
    # ---------------------------------------------------------------------#
    orden = len(matrizA)
    a = Matrix(matrizA)
    b = Matrix(matrizB)
    c = Matrix(matrizC)
    if (len(a) == len(b) and len(b) == len(c)):
        try:
            x = convertMatrixToList((a.inv() * c) - b)
            imprimir(x)
            return x
        except:
            print("La matriz A es singular por lo que no se puede despejar X")
    else:
        print("Las matrices no tienen el mismo orden")


def convertMatrixToList(matriz):
    global orden
    result = []
    cont = 0
    for i in range(0, orden):
        result.append([])
        for j in range(0, orden):
            result[i].append(Fraction(str(matriz[cont])))
            cont += 1
    return result


def imprimir(m):
    for i in range(0, len(m)):
        print("Fila: ", i, " valor: ", m[i])

