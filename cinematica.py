'''
Este modulo contiene diversas constantes y funciones de interes relacionadas con la cinemática
'''
#---------------------------------
from unidadessi import *
import numpy as np
#CONSTANTES
g = g_terrestre
#-----------------------
#FUNCIONES 
def modulo (x, y, z=0):
    '''
    Esta funcion calcula el modulo de un vector tridimensional pero cuya tercera componente es 0 por defecto
    '''
    modulo = np.sqrt(x**2+y**2+z**2)
    return modulo
    
def resta_vectores (x,y,x0,y0, z = 0, z0 = 0):
    '''
    Esta funcion calcula el vector (x-x0, y-y0, z-z0), donde por defecto la tercera coordenada es 0
    '''
    xprima = x -x0
    yprima = y - y0
    zprima = z -z0
    return xprima, yprima, zprima

def distancia (x, y, x0, y0, z = 0, z0 = 0):
    '''
    Esta función calcula la distancia entre un punto de coordenadas (x,y,z) y otro (x0,y0,z0) donde por defecto la tercera coordenada es 0
    '''
    resta = resta_vectores(x,y,x0,y0, z = z, z0 = z0)
    distancia = modulo(resta[0], resta[1], z = resta[2])
    return distancia
    
def unitario (r1x, r1y, r2x, r2y, r1z = 0, r2z = 0):
    '''
    Esta funcion coje dos vectores posición tridimensionales (r1x,r1y, r1z) y (r2x,r2y, r2z) y calcula el vector unitario en la dirección r2-r1
    '''
    resta = resta_vectores(r2x,r2y, r1x, r1y, z = r2z, z0 = r1z)
    distancia_vectores = distancia(r2x,r2y,r1x,r1y, z = r2z, z0 = r1z)
    ux, uy, uz = (resta[0],resta[1],resta[2])/distancia_vectores
    return ux, uy, uz

def polares_a_cartesianas (r, theta):
    '''
    Esta función pasa unas cordenadas polares en funcion de r, theta a cordenadas cartesianas
    '''
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return (x, y)

def cartesianas_a_polares (x,y):
    '''
    Esta funcion pasa unas coordenadas cartesianas en funcion de x,y a cordenadas polares
    '''
    r = modulo(x,y)
    theta = np.arctan(y/x)
    return (r, theta)
def posicion_MRUA(x0,v0,a,t):
    '''
    Esta función calcula la distancia que alcanza un cuerpo en un MRUA en funcion de su posicion inicial, su velocidad inicial,
    su aceleracion y el tiempo que dura el movimiento
    '''
    x = x0 + v0*t + 0.5*a*(t**2)
    return x
    
    
def velocidad_MRUA(v0, a, t):
    '''
    Esta funcion devuelve la velocidad final de un MRUA a partir de su velocidad inicial,
    la aceleracion y el tiempo
    '''
    v = v0 +a*t
    return v


    
    
def tiempo_al_suelo (vy, a = g):
    '''
    Esta función calcula el tiempo que tarda un cuerpo en un movimiento vertical en caer al suelo
    según su velocidad inicial y la aceleración a en m/s², por defecto g
    '''
    t = 2*vy*metros/a
    
    return t
    
def ajuste_lineal(x,y, incertidumbre = False, R2 = False):
    '''
    Esta funcion devuelve un ajuste lineal dados x, y = f(x), así como
    el coeficiente de correlación y el error de a,b
    '''
    #Se convierten en arrays si no lo eran ya
    x = np.asarray(x)
    y = np.asarray(y)
    
    #Se realizan los sumatorios necesarios
    sx = x.sum()
    sy = y.sum()
    xx = x*x
    sxx = xx.sum()
    xy = x*y
    sxy = xy.sum()
    
    #Se calcula el tamaño de los arrays y se comprueba que sean iguales
    Nx = np.size(x)
    Ny = np.size(y)
    if Nx != Ny:
        print("Los datos no tienen el mismo tamaño")
        return (0,0)
    #Calculamos el valor de a y de b usando las formulas de los ajustes lineales
    a = (Nx*sxy-sx*sy)/(Nx*sxx-sx*sx)
    b = (sxx*sy-sx*sxy)/(Nx*sxx-sx*sx)
    if R2:
        #Si se cambia el valor a true, devuelve la bondad del ajuste
        yy = y*y
        syy = yy.sum()
        R2 = (Nx*sxy-sx*sy)/(np.sqrt(Nx*sxx-sx*sx)*np.sqrt(Nx*syy-sy*sy))
    
    return(a,b,R2)
