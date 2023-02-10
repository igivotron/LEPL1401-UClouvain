def is_adn(s):
    """
    Permet de savoir si la séquence donnée est de l'ADN
    :param s: sequence de type string
    :return:  si la séquence ne contient que des atgc peu importe les majuscules alors la fonction return True
    """
    s = s.upper()
    frog = s.count('A') + s.count('T') + s.count('G') + s.count('C')
    if len(s) == frog:
        return True
    else:
        return False


def positions(s, p):
    """
    Détermine si la séquence p se trouve dans la séquence s et donne ses positions
    :param s: Séquence à comparer
    :param p: Séquence de comparaison
    :return: les positions de la séquence p dans la séquence s
    """
    s = s.upper()
    p = p.upper()
    l = []
    for i in range(len(s)):
        a = s[0+i:len(p)+i]
        if a == p:
            l.append(i)
    return l


def distance_h(a, b):
    """
    Compare deux séquences de même longueur et retourne les différences
    :param a: première séquence à comparer
    :param b: deuxième séquence à comparer
    :return: Retourne la distance entre les deux séquences sous forme d'une liste
    """
    a = a.upper()
    b = b.upper()
    jambon = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            jambon += 1
    return jambon


def distances_matrice(l):
    """
    Compare des séquences venant d'une liste
    :param l: liste de séquences
    :return: Retourne une matrice carrée des distances entre les séquences
    """
    tac = []
    for i in range(len(l)):
        tic = []
        for j in range(len(l)):
            if len(l[i]) == len(l[j]):
                tic.append(distance_h(l[i], l[j]))
            else:
                tic.append(None)
        tac.append(tic)
    return tac
