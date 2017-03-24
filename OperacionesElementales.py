from claseOperacionElemental import *

from crearSecuenciaResultados import *

def intercambiarFilas(matriz, fila1, fila2):
    op = TipoA(fila1,fila2)
    tmp1 = matriz[fila1]
    matriz[fila1]=matriz[fila2]
    matriz[fila2]=tmp1
    guardarResultados(matriz, op)
    return matriz

def multiplicarPorConstante(matriz, filaC, constante):
    op = TipoB(filaC, constante)
    fila = matriz[filaC]
    for i in range(0,len(fila)):
        fila[i] = fila[i]*constante
    matriz[filaC] = fila
    guardarResultados(matriz, op)
    return matriz

def sumaDeFilas(matriz, filaS, filaC, constante):
    op = TipoC(filaS,filaC, constante)
    fila1 = matriz[filaS]
    fila2 = matriz[filaC]
    for i in range(0, len(matriz[0])):
        fila1[i] += fila2[i]*constante
    matriz[filaS]=fila1
    guardarResultados(matriz, op)
    return matriz

#FIX ME: no se si es necesario ajustar al numero de filas por iniciar en 0 <--- LOL

