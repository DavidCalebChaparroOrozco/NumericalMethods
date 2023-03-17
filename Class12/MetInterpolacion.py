import numpy as np

def interp_lagrange(x,xdat,ydat):
    """
    Calcula el polinomio de Lagrange que pasa por los puntos (xdat, ydat) y lo evalúa en x.
    Args:
    xdat: Arreglo de números que representan las coordenadas x de un conjunto de datos
    ydat: Arreglo de números que representan las coordenadas y de un conjunto de datos
    x: Arreglo de números a evaluar en el polinomio de Lagrange
    
    Returns:
    y: Arreglo con resultados de la evaluación de x en el polinomio de Lagrange
    """
    y=np.zeros(len(x))
    
    for i in range(len(xdat)):
        den = 1
        num = 1
        for j in range(len(xdat)):            
            if j != i:
                num=num*(x - xdat[j])
                den=den*(xdat[i]-xdat[j])

        y = y + (num/den)*ydat[i]
  
    return y