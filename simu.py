a = 0.050
b = 0.003 #Largeur du bord
h = 0.004 #Hauteur du bord
L = 0.4 #Longueur
E = 3E9 #Module de young
energie = 5
cst_frot_roul = 0.010
g = 9.81

m = 167+88 #en gramme
cst_frot_mot = 1/2 #Obtenue par mesure

def constante_K(E,b,h,L):
    K = (E*b*pow(h,3))/(12*L)
    return K

def alpha0(energie):
    K = constante_K(E,b,h,L)
    alpha0 = pow(((2*energie)/K), 1/2) #Alpha0 en radiant
    return alpha0

def forceA(a):
    K = constante_K(E,b,h,L)
    alpha0 = pow(((2*energie)/K), 1/2)
    forceA = K*alpha0/a
    return forceA

def force_frot_mot(cst_frot_mot):
    forceA = forceA(a)
    force_frot_mot = forceA * cst_frot_mot
    return force_frot_mot

def force_frot_roul(cst_frot_roul,m, g):
    force_frot_roul = m*g*cst_frot_roul
    return force_frot_roul

def a_angul(a,m):
    force_frot_mot = force_frot_mot(cst_frot_mot)
    a_angul = force_frot_mot/(m*a)
    return a_angul
