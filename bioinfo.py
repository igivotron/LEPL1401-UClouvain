def is_adn(s):
    s = s.upper()
    frog = s.count('A') + s.count('T') + s.count('G') + s.count('C')
    if len(s) == frog:
        return True
    else:
        return False
    
def positions(s, p):
    s = s.upper()
    p = p.upper()
    l =[]
    for i in range(len(s)):
        for j in range(len(p)):
            if s[i] == p[j]:
                froggies = True
            else:
                froggies = False
        if froggies:
            l.append(i-1)
    return l

def distance_h(a,b):
    a = a.upper()
    b = b.upper()
    jambon = 0
    
    for i in range(len(a)):
        if a[i] != b[i]:
            jambon += 1
    return jambon

def distances_matrice(l):
    tac=[]
    for i in range(len(l)):
        tic =[]
        for j in range(len(l)):
            if len(l[i]) == len(l[j]):
                tic.append(distance_h(l[i],l[j]))
            else:
                tic.append(None)
        tac.append(tic)
    return tac

