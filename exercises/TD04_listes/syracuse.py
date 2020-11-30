def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste = [n]
    while True:
        lastNum = liste[-1]
        if lastNum != 1:
            if (lastNum % 2) == 0:
                newNum = lastNum // 2
            else:
                newNum = (lastNum*3)+1
            liste.append(newNum)
        else:
            break
    return liste


print(syracuse(3))


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for i in range(1, n_max+1):
        syracuse(i)
    return True


print(testeConjecture(10000))


def tempsVol(n):
    """ Retourne le temps de vol de n """
    return len(syracuse(n))-1


print("Le temps de vol de", 3, "est", tempsVol(3))

def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    return [tempsVol(i) for i in range(1, n_max+1)]


volListe = tempsVolListe(10000)
print(f"{volListe.index(max(volListe))+1} qui a le temps de vol {max(volListe)}")

