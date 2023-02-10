#
# PYTHON for DUMMIES 22-23
# Problème 1
#
# Interpolation de Padé
# Interpolation avec des quotients de polynômes
#
# Vincent Legat
# Nathan Coppin
#
# -------------------------------------------------------------------------
#

from numpy import *
from numpy.linalg import solve


# ============================================================
# FONCTIONS A MODIFIER [begin]
#
#

def padeInterpolationCompute(X, U):
    n = len(X)//2
    B = concatenate((array([pow(X, i) for i in range(n+1)]).T, array([-pow(X, i+1)*U for i in range(n)]).T), axis=1)
    a = solve(B, U)
    return a


def padeEval(a, x):
    n = len(a)//2
    u = 0
    v = 1
    for j in range(n+1):
        u += a[j]*pow(x, j)
    for j in range(n):
        v += a[j+n+1]*pow(x, j+1)
    return u/v



#
# FONCTIONS A MODIFIER [end]
# ============================================================

#
# -1- Test de la fonction interpolation
#     On considère un jeu des 3 fonctions u(x)
#


def main():
    n = 2
    u = lambda x: cos(x)
    X = linspace(-2, 2, (2 * n + 1))
    U = u(X)

    #
    # -1- Calcul des coefficients de l'interpolation
    #
    print("==== Computing the Padé approximation :-)")
    a = padeInterpolationCompute(X, U)
    print(" a = ", list(a))

    #
    # -2- Evaluation l'interpolation de Padé
    #     et de l'interpolation polynomiale de Lagrange
    #
    x = linspace(-5, 5, 100)
    upade = padeEval(a, x)
    uh = polyval(polyfit(X, U, len(X) - 1), x)

    #
    # -3- Et un joli plot :-)
    #

    from matplotlib import pyplot as plt
    plt.rcParams['toolbar'] = 'None'
    plt.rcParams['figure.facecolor'] = 'silver'

    plt.figure('Interpolation de Padé n = %d ' % n)
    plt.plot(x, u(x), '-b', label='cosinus')
    plt.plot(x, uh, '-g', label='Lagrangian interpolation')
    plt.plot(x, upade, '-r', label='Padé interpolation')
    plt.plot(X, U, 'ob')
    plt.xlim((-5, 5));
    plt.ylim((-1.2, 1.2))
    plt.legend(loc='upper right')
    plt.show()


main()
