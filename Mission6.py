def line_count(filename):
    """
    Compte le nombre de ligne dans le fichier
    :param filename: Nom du fichier
    :return: le nombre de ligne
    """
    a = 0
    with open(filename, "r") as f:
        for ligne in f:
            a += 1
        return a

def char_count(filename):
    """
    Compte le nombre de mot dans le fichier
    :param filename: Nom du fichier
    :return: nombre de mots
    """
    with open(filename,"r") as f:
        a = len(f.read())
        return a

def words_command(filename):
    """
    trasforme le fichier en liste de str
    :param filename: nom du fichier
    :return: liste de str
    """
    l = []
    with open(filename,"r") as f:
        for ligne in f:
            if "," in ligne:
                a = ligne.index(",")
                ligne = ligne[:a]
            else:
                ligne = ligne[0:-1]
            l.append(ligne)
    return l

def search_command(l,word):
    """
    Cherche un mot dans la liste de str
    :param l: liste de str
    :param word: mot à chercher
    :return: True si le mot est dans la liste
    """
    if word in l:
        return True

def sum(l):
    """
    additionne des nombres
    :param l: liste des nombres à additionner. Le premier élément de cette liste n'est pas compté dans le calcul, le reste de la liste sont de type int ou float.
    :return: la somme des nombres
    """
    a = 0
    for i in range(1, len(l)):
        a += float(l[i])
    return a

def avg(l):
    """
    Calcule la moyenne
    :param l: nombre à calculer. Le premier élément de cette liste n'est pas compté dans le calcul, le reste de la liste sont de type int ou float.
    :return: la moyenne des nombres
    """
    a = sum(l)
    b = a/(len(l)-1)
    return b

def main():
    loop = True
    while loop:
        command = input(">")
        command_l = command.split()
        
        if command_l == []:
            print("Command not available")
            print("Enter help to see the available commands")
            
        elif command_l[0] == "file":
            filename = command[5:]
            print("Loaded", filename)

        elif command_l[0] == "info":
            try:
                lines = line_count(filename)
                caracters = char_count(filename)
                print(lines, "lignes")
                print(caracters, "characters")
            except:
                print("An error has occurred. Did you choose the right file?")
                print("Enter help to see the available commands")

        elif command_l[0] == "words":
            try:
                print("Read file as list of words")
                l = words_command(filename)
            except:
                print("An error has occurred. Did you choose the right file?")
                print("Enter help to see the available commands")

        elif command_l[0] == "search":
            try:
                if search_command(l ,command_l[1]):
                    print(command_l[1],"is in the list of words")
                else:
                    print(command_l[1],"is not in the list of words")
            except:
                print("An error has occurred. Did you transform your file into a list of words?")
                print("Enter help to see the available commands")

        elif command_l[0] == "sum":
            try:
                rep = sum(command_l)
                print(rep)
            except:
                print("sum <number 1> <number 2> ... <number n>")
                print("An error occurred. Did you only use int or float ?")
                print("Enter help to see the available commands")

        elif command_l[0] == "avg":
            try:
                rep = avg(command_l)
                print(rep)
            except:
                print("avg <number 1> <number 2> ... <number n>")
                print("An error occurred. Did you only use int or float ?")
                print("Enter help to see the available commands")

        elif command_l[0] == "help":
            print("file <name>                                 Specifies the name of a file")
            print("info                                        Shows the number of lines and characters in the file")
            print("words                                       Uses the file as a word list")
            print("search <word>                               Searchs a word in the word list")
            print("sum <number 1> <number 2> ... <number n>    Calculates the sum of the specified numbers")
            print("avg <number 1> <number 2> ... <number n>    Calculates the average of the specified numbers")
            print("exit                                        Quit the program")

        elif command_l[0] == "exit":
            loop = False
    
main()

