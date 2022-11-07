import matplotlib.pyplot as plt
import numpy as np

a = 0.050
b = 0.003 #Largeur du bord
h = 0.004 #Hauteur du bord
L = 0.4 #Longueur
E = 3E9 #Module de young
energie = 5
cst_frot_roul = 0.010
g = 9.81

m = 0.255 #en gramme
cst_frot_mot = 1/2 #Obtenue par mesure

def constante_K(E,b,h,L):
    K = (E*b*pow(h,3))/(12*L)
    return K

def falpha0(energie):
    K = constante_K(E,b,h,L)
    alpha0 = pow(((2*energie)/K), 1/2) #Alpha0 en radiant
    return alpha0

def fforceA(a, alpha):
    K = constante_K(E,b,h,L)
    forceA = K*alpha/a
    return forceA

def fforce_frot_mot(cst_frot_mot, forceA):
    force_frot_mot = forceA * cst_frot_mot
    return force_frot_mot

def fforce_frot_roul(cst_frot_roul,m, g):
    force_frot_roul = m*g*cst_frot_roul
    return force_frot_roul

def fa_angul(a,m,force_frot_mot):
    a_angul = force_frot_mot/(m*a)
    return a_angul

K = constante_K(E, b, h, L)
alpha = falpha0(energie)



loop = True
t = 0.001
v = 0
x = 0
v_t = [0]
x_t = [0]
k= 1
while loop:
    forceA = fforceA(a, alpha)
    force_frot_mot = fforce_frot_mot(cst_frot_mot, forceA)
    force_frot_roul = fforce_frot_roul(cst_frot_roul, m, g)
    force_res = forceA - force_frot_roul - force_frot_mot - v*k
    a_res = force_res / m

    v += a_res*t
    v_t.append(v)
    x += v*t
    x_t.append(x)

    a_angul = fa_angul(a, m, force_frot_mot)
    alpha = alpha - t*a_angul/100

    if alpha <= 0.000001:
        loop = False

loop = True
while loop:

    a = (force_frot_roul + v*k)/m
    v -= a*t
    x += v*t
    v_t.append(v)
    x_t.append(x)

    if v <= 0.000001:
        loop = False

plt.plot(x_t, label="Positon en [m]")
plt.plot(v_t, label="Vitesse en [m/s]")
plt.title("Simulation de notre véhicule")
plt.xlabel("Temps en ms")
plt.ylabel("Distance en m")
plt.legend()
plt.show()
