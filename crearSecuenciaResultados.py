from claseOperacionElemental import *
from fractions import Fraction

def writeToFile(text):
    print("Abriendo archivo..." + "\n")
    fileHandle = open("Resultados.txt", "a+")
    fileHandle.write(text + "\n")
    print("Escrito: " + text + "\n")
    fileHandle.close()

def guardarResultados(matriz, operacionElemental):
    tmp = ""
    print("Guardando resultados...\n")
    if(type(operacionElemental) is TipoA):
        tmp += "  ----->\tf"+\
                str(operacionElemental.filaA)+"  <-->  f"+\
                str(operacionElemental.filaB)+"\t----->\n\n\n"+\
                matrizToString(matriz)
    elif(type(operacionElemental) is TipoB):
        tmp += "   ----->\t" + \
               str(operacionElemental.constanteA) + "  *  f" + \
               str(operacionElemental.filaC) + "\t----->\n\n\n" + \
               matrizToString(matriz)
        #tmp += str(matriz) + " Operación elemental del tipo B, se multiplicó la fila " + str(
            #operacionElemental.filaC) + " por constante " + str(operacionElemental.cosntanteA)
        #tmp ="Tipo B"
    elif (type(operacionElemental) is TipoC):
        tmp += "   ----->\tf" + \
               str(operacionElemental.filaD) + "  +  " + \
               str(operacionElemental.constanteB) + " * f" + str(operacionElemental.filaE) + "\t----->\n\n\n" + \
               matrizToString(matriz)
        #tmp += str(matriz) + " Operación elemental del tipo C, se multiplicó la fila " + str(
            #operacionElemental.filaD) + " por fila " + str(operacionElemental.filaE)+" por constante: "+str(
            #operacionElemental.constanteB)
        #tmp="Tipo C"
    else:
        tmp+="[[-1]] Error"
    writeToFile(tmp)

def matrizToString(matriz):
    tmp = "\n"
    for i in range(0,len(matriz)):
        for j in range(0, len(matriz[i])):
            num = Fraction(matriz[i][j])
            print(str(num.numerator) + "\t")
            tmp+=(str(num.numerator) + "\t")
        tmp+="\n"
        for j in range(0, len(matriz[i])):
            tmp+="----\t"
        tmp+="\n"
        for j in range(0, len(matriz[i])):
            num = Fraction(matriz[i][j])
            print(str(num.denominator)+"\t")
            tmp+=(str(num.denominator)+"\t")
        tmp += "\n\n\n"
    print(tmp)
    return tmp