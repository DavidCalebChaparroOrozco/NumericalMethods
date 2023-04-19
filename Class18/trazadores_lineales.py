import numpy as np
import sympy as sym

def trazador_lineal(xi,fi):
    n = len(xi)
    x = sym.Symbol('x')
    px_table = []

    tramo = 1
    while not(tramo>=n):
        numerador = fi[tramo]-fi[tramo-1]
        denominador = xi[tramo]-xi[tramo-1]
        m = numerador/denominador
        pxtramo = fi[tramo-1] + m*(x-xi[tramo-1])
        px_table.append(pxtramo)
        tramo = tramo + 1
    return(px_table)