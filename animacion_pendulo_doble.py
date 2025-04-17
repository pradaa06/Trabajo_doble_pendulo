
#pip3 install -U scipy
import cinematica as cin
import pendulo_ec_dif as ped
from matplotlib.animation import FuncAnimation
import numpy as np

condiciones = [[1, 1, 0.8, 0.9], 7, 5, 6, 3, 20, 500]
variables = condiciones[0]
L1, L2, m1, m2 = condiciones[1], condiciones[2], condiciones[3], condiciones[4]
tf = condiciones[5]
deltat = condiciones[6]
tiempos = np.linspace(0, tf, deltat)
#print(tiempos)

resultados = ped.reslv(ped.fun, condiciones)
#print(resultados)
theta1, theta2, w1, w2 = resultados[0,:], resultados[1,:], resultados[2,:], resultados[3,:]
#print(theta1)
#ejes
x1, y1 = cin.polares_a_cartesianas(-L1, theta1)
x02, y02 = cin.polares_a_cartesianas(-L2, theta2)
x2, y2 = x1 + x02, y1 + y02
#print(x1, y1)

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(11,9))

linea1,  = ax.plot([], [], 'b-')
linea2,  = ax.plot([], [], 'r-')
punto1,  = ax.plot([], [], 'bo')
punto2,  = ax.plot([], [], 'ro')
trayectoria, = ax.plot([], [], 'o', color='red', alpha=0.3)

def init():
	linea1.set_data([], [])
	linea2.set_data([], [])
	punto1.set_data([], [])
	punto2.set_data([], [])
	trayectoria.set_data([], [])
	ax.set_xlim(-10, 10)
	ax.set_ylim(-20, 0)
	return linea1, linea2, punto1, punto2, trayectoria
def update(frame):
	linea1.set_data([0, y1[frame]], [0, x1[frame]])
	linea2.set_data([y1[frame], y2[frame]], [x1[frame], x2[frame]])
	punto1.set_data(y1[frame], x1[frame])
	punto2.set_data(y2[frame], x2[frame])
	trayectoria.set_data(y2[frame-15], x2[frame-15])
	
	return linea1, linea2, punto1, punto2, trayectoria
	
ani = FuncAnimation(fig, update, init_func=init, frames = len(tiempos), interval=20)
	


plt.show()



'''
Animar en vez desde 0 a tf, animar desde t-100 hasta tf
'''
