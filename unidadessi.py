'''
Este módulo establece las unidades fundamentales del SI, asi como sus multiplos, algunas unidades derivadas del mismo y algunas constantes expresadas en las correspondientes unidades
'''
from numpy import pi

#UNIDADES FUNDAMENTALES
segundo = 1
metro = 1
gramo = 1e-3 #Por simplicidad para trabajar con multiplos, se toma el gramo por unidad fundamental en lugar del kilogramo
amperio = 1
kelvin = 1
mol = 1
candela = 1

#---------------------------------
#MULTIPLOS
peta = 1e15
tera = 1e12
giga = 1e9
mega = 1e6
kilo = 1e3
hecto = 1e2
deca = 10
deci = 0.1
centi = 1e-2
mili = 1e-3
micro = 1e-6
nano = 1e-9
pico = 1e-12
femto = 1e-15
#---------------------------------
#UNIDADES DERIVADAS
#Equivalencia de unidades externas al SI
kilogramo = kilo*gramo #Como se menciono, tecnicamente es al reves pero se hace asi por simplicidad
tonelada = kilo*kilogramo
litro = (deci**3)*(metro**3)
minuto = 60*segundo
hora = 60*minuto
dia = 24*hora
año = 365*dia

#Unidades mecanicas

hercio = segundo**(-1)
newton = metro*kilogramo/(segundo**2)
pascal = newton/(metro**2)
julio = newton*metro
vatio = julio/segundo

#Unidades electromagneticas

culombio = segundo*amperio
voltio = vatio/amperio
faradio = culombio/voltio
ohmio = voltio/amperio
siemens = amperio/voltio
weber = voltio * segundo
tesla = weber/(metro**2)
henrio = weber/amperio

#Unidades quimicas

celsius = kelvin - 273.15
katal = mol/segundo

#Unidades radiologicas

bequerelio = segundo**(-1)
gray = julio/kilogramo
sievert = julio/kilogramo

#Unidades fotometricas

lumen = candela*4*pi
lux = lumen/(metro**2)

#-----------------------------
#Constantes en unidades del SI
velocidad_luz =299792458*metro/segundo
h_planck = 6.62607015e-34*julio*segundo
carga_elemental = 1.602176634e-19*culombio
k_boltzman = 1.380649e-23*julio/kelvin
n_avogadro = 6.02214076e23/mol
g_terrestre = 9.80665*metro/(segundo**2)
k_coulomb= 8.9875517873681764e9*newton*(metro**2)/(culombio**2)
epsilon_vacio = 8.8541878128e-12*faradio/metro
mu_vacio = 1.25663706212e6*newton/(amperio*2) 	








