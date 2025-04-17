'''
SIMULACIÓN DE UN DOBLE PÉNDULO MEDIANTE ECUACIONES DIFERENCIALES ORDINARIAS
'''

import numpy as np
from scipy.integrate import solve_ivp
import unidadessi as us

#variables = np.array([theta1, theta2, w1, w2])
#conidiciones = [[variables], L1, L2, m1, m2, tf, deltat]

def alpha1(t, m1, m2, w1, w2, L1, L2, theta1, theta2, g = us.g_terrestre):
    '''
    Calcula la aceleración angular (α₁ = d²θ₁/dt²) del primer péndulo en un sistema de doble péndulo.
    
    La expresión implementada es:
    
              -g(2m₁ + m₂)sinθ₁ - m₂gsin(θ₁-θ₂) - 2sin(θ₁-θ₂)m₂[ω₂²L₂ + ω₁²L₁cos(θ₁-θ₂)]
    α₁ =  -----------------------------------------------------------------------------------
                         L₁ [2m₁ + m₂ - m₂cos(2θ₁ - 2θ₂)]
    
    Parámetros:
    -----------
    t: tiempo [s].
    m1, m2: masas del primer y segundo péndulo [kg].
    L1, L2: longitudes de los brazos del primer y segundo péndulo [m].
    theta1, theta2: ángulos de los péndulos respecto a la vertical [rad].
    g: aceleración debido a la gravedad del campo terrestre [m/s²].
    '''
    num = -g*(2*m1 + m2)*np.sin(theta1) - m2*g*np.sin(theta1-theta2) - 2*np.sin(theta1-theta2)*m2*((w2**2)*L2 + (w1**2)*L1*np.cos(theta1-theta2))
    denom = L1 * (2*m1 + m2 - m2*np.cos(2*theta1 - 2*theta2))
    return num/denom

def alpha2(t, m1, m2, w1, w2, L1, L2, theta1, theta2, g = us.g_terrestre):
    '''
    Calcula la aceleración angular (α₂ = d²θ₂/dt²) del segundo péndulo en un sistema de doble péndulo.
    
    La expresión implementada es:
    
              2sin(θ₁-θ₂)[ω₁²L₁(m₁+m₂) + g(m₁+m₂)cosθ₁ + ω₂²L₂m₂cos(θ₁-θ₂)]
    α₂ =  ----------------------------------------------------------------------
                          L₂ [2m₁ + m₂ - m₂cos(2θ₁ - 2θ₂)]
    
    Parámetros:
    -----------
    t: tiempo [s].
    m1, m2: masas del primer y segundo péndulo [kg].
    w1, w2: velocidades angulares de los péndulos [rad/s].
    L1, L2: longitudes de los brazos del primer y segundo péndulo [m].
    theta1, theta2: ángulos de los péndulos respecto a la vertical [rad].
    g: aceleración debido a la gravedad del campo terrestre [m/s²].
    '''
    num = 2*np.sin(theta1-theta2)*((w1**2)*L1*(m1+m2)+g*(m1+m2)*np.cos(theta1) + (w2**2)*L2*m2*np.cos(theta1-theta2))
    denom = L2*(2*m1 + m2 - m2*np.cos(2*theta1 - 2*theta2))
    return(num/denom)
    

def fun(t, variables, L1, L2, m1, m2):
    '''
    Sistema de ecuaciones diferenciales para un doble péndulo.
    
    Convierte el problema de segundo orden en un sistema de primer orden para
    ser resuelto por solve_ivp. Las ecuaciones implementadas son:
    
    1. dθ₁/dt = ω₁
    2. dθ₂/dt = ω₂
    3. dω₁/dt = α₁(t, m1, m2, ω₁, ω₂, L1, L2, θ₁, θ₂, g)
    4. dω₂/dt = α₂(t, m1, m2, ω₁, ω₂, L1, L2, θ₁, θ₂, g)
    
    Donde α₁ y α₂ son las aceleraciones angulares calculadas por las funciones alpha1 y alpha2.
    
    Parámetros:
    -----------
    t: tiempo [s].
    variables: lista con las condiciones iniciales del sistema [θ₁, θ₂, ω₁, ω₂], donde:
        - θ₁, θ₂: ángulos actuales de los péndulos [rad].
        - ω₁, ω₂: velocidades angulares actuales [rad/s].
    '''
    theta1, theta2  = variables[0], variables[1]
    w1, w2 = variables[2], variables[3]
    
    dtheta1dt = w1
    dtheta2dt = w2
    
    dw1dt = alpha1(t, m1, m2, w1, w2, L1, L2, theta1, theta2)
    dw2dt = alpha2(t, m1, m2, w1, w2, L1, L2, theta1, theta2)
    
    return [dtheta1dt, dtheta2dt, dw1dt, dw2dt]

def reslv(fun, condiciones):
    '''
    Resuelve el sistema de ecuaciones diferenciales asociado a un doble péndulo
    utilizando la función 'solve_ivp' de 'scipy.integrate'. La solución calcula
    las posiciones angulares y velocidades angulares de los dos péndulos en función
    del tiempo.
    
    Parámetros:
    -----------
    fun: función que describe el sistema de ecuaciones diferenciales del doble péndulo.
        Debe aceptar los argumentos (t, variables, L1, L2, m1, m2).
    condiciones: lista con las condiciones iniciales y parámetros del sistema:
        - condiciones[0]: lista de variables iniciales [θ₁, θ₂, ω₁, ω₂], donde:
            - θ₁, θ₂: ángulos iniciales de los péndulos [rad].
            - ω₁, ω₂: velocidades angulares iniciales de los péndulos [rad/s].
        - condiciones[1]: L1, longitud del brazo del primer péndulo [m].
        - condiciones[2]: L2, longitud del brazo del segundo péndulo [m].
        - condiciones[3]: m1, masa del primer péndulo [kg].
        - condiciones[4]: m2, masa del segundo péndulo [kg].
        - condiciones[5]: tf, tiempo final de la simulación [s].
        - condiciones[6]: deltat, número de puntos para discretizar el intervalo de tiempo.
    '''
    variables = condiciones[0]
    L1, L2, m1, m2 = condiciones[1], condiciones[2], condiciones[3], condiciones[4]
    tf, deltat = condiciones[5], condiciones[6]
    return solve_ivp(fun, [0, tf], variables, t_eval=np.linspace(0,tf,deltat), args=(L1, L2, m1, m2)).y

