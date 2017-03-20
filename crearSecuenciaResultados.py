from claseOperacionElemental import *

def writeToFile(text):
    fileHandle = open("Resultados.txt", "a+")
    fileHandle.write(text + "\n")
    fileHandle.close()

def guardarResultados(matriz, operacionElemental):
    tmp = ""
    if(type(operacionElemental) is TipoA):
           tmp += str(matriz)+ " Operación elemental del tipo A, se cambio la fila "+str(
               operacionElemental.filaA)+" por fila "+str(operacionElemental.filaA)
    elif(type(operacionElemental) is TipoB):
        tmp += str(matriz) + " Operación elemental del tipo B, se multiplicó la fila " + str(
            operacionElemental.filaC) + " por constante " + str(operacionElemental.cosntanteA)
    elif (type(operacionElemental) is TipoC):
        tmp += str(matriz) + " Operación elemental del tipo C, se multiplicó la fila " + str(
            operacionElemental.filaD) + " por fila " + str(operacionElemental.filaE)+" por constante: "+str(
            operacionElemental.constanteB)
    else:
        tmp+="[[-1]] Error"
    writeToFile(tmp)
