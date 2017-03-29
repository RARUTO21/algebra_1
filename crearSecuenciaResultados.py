from claseOperacionElemental import *

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
           tmp += str(matriz)+ " Operación elemental del tipo A, se cambio la fila "+str(
               operacionElemental.filaA)+" por fila "+str(operacionElemental.filaB)
    elif(type(operacionElemental) is TipoB):
        #tmp += str(matriz) + " Operación elemental del tipo B, se multiplicó la fila " + str(
            #operacionElemental.filaC) + " por constante " + str(operacionElemental.cosntanteA)
        tmp ="Tipo B"
    elif (type(operacionElemental) is TipoC):
        #tmp += str(matriz) + " Operación elemental del tipo C, se multiplicó la fila " + str(
            #operacionElemental.filaD) + " por fila " + str(operacionElemental.filaE)+" por constante: "+str(
            #operacionElemental.constanteB)
        tmp="Tipo C"
    else:
        tmp+="[[-1]] Error"
    writeToFile(tmp)

def matrizToString(matriz):
    tmp = str(matriz)
    return tmp