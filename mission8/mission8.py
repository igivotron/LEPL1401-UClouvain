### Codé par Igor Grégoire et Brieuc Loncourt

class Duree:
    def __init__(self, h, m, s):
        """
        :param h: Nombre d'heures. Entier plus grand ou égal à 0
        :param m: Nombre de minutes. Entier compris dans [0;60[
        :param s: Nombre de secondes. Entier compris dans [0;60[
        """
        if 0 <= h:
            self.heure = int(h)
        else:
            print('"Heure" doit être un entier positif')
        if 0 <= m < 60:
            self.minute = int(m)
        else:
            print('"Minute" doit être un entier compris dans [0; 60[')
        if 0 <= s < 60:
            self.seconde = int(s)
        else:
            print('"Seconde" doit être un entier compris dans [0; 60[')

    def to_secondes(self):
        """
        Donne le nombre de secondes
        :return: le nombre de seconde
        """
        sec = 0
        sec += self.seconde + 60 * self.minute + 3600 * self.heure
        return sec

    def delta(self, d):
        """
        Donne la différence de secondes entre la durée self et la durée d
        :param d: Durée issue de la classe Durée
        :return: Entier, différence en secondes
        """
        delt = self.to_secondes() - d.to_secondes()
        return delt

    def apres(self, d):
        """
        Retourne True si self est plus long que d
        :param d: Instance Durée
        :return: True si self > d, sinon false
        """
        if self.to_secondes() < d.to_secondes():
            return False
        else:
            return True

    def ajouter(self, d):
        """
        Additionne deux temps
        :param d: Instance de durée
        :return: Met à jour le self
        """
        sec = self.seconde + d.seconde
        minu = sec // 60
        sec = sec % 60
        minu += self.minute + d.minute
        heu = minu // 60
        minu = minu % 60
        heu += self.heure + d.heure
        self.seconde, self.minute, self.heure = sec, minu, heu
        return self

    def __str__(self):
        return "{:02}:{:02}:{:02}".format(self.heure, self.minute, self.seconde)


class Chanson:
    def __init__(self, t, a, d):
        """
        Initialise Chanson
        :param t: Le titre, str
        :param a: L'auteur, str
        :param d: La durée, int
        """
        self.titre = t
        self.auteur = a
        self.duree = d

    def __str__(self):
        return "{TITRE} - {AUTEUR} - {DUREE}".format(TITRE=self.titre, AUTEUR=self.auteur, DUREE=self.duree)


class Album:
    def __init__(self, numero):
        self.numero = numero
        self.music = []
        self.t = Duree(0, 0, 0)

    def add(self, chanson):
        lim = Duree(1, 15, 0)
        if len(self.music) < 100 and self.t.to_secondes() + chanson.duree.to_secondes() < lim.to_secondes():
            self.music.append(chanson)
            self.t.ajouter(chanson.duree)
            return True
        else:
            return False

    def __str__(self):
        text = ""
        for i in range(len(self.music)):
            text += "{:02}: ".format(i+1) + str(self.music[i]) + "\n"
        return text


if __name__ == "__main__":

    with open("music-db.txt", "r") as f:
        l = f.read().splitlines()
        lc = []
        for i in range(len(l)):
            l[i] = l[i].split()
            l[i] = Chanson(l[i][0], l[i][1], Duree(0, int(l[i][2]), int(l[i][3])))

    a = 1
    b = -1
    alb = Album(a)
    for i in l:
        b +=1
        if alb.add(i) == False:
            print("Album {num} ({x} chansons, {d})".format(num=a,x=b,d=alb.t))
            print(alb)
            a +=1
            b = 0
            alb = Album(a)
            alb.add(i)
    print("Album {num} ({x} chansons, {d})".format(num=a, x=b, d=alb.t))
    print(alb)

