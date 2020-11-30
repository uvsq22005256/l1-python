def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for i in carre:
        print(i)


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes
     les lignes ont la même somme, et -1 sinon """
    constante = -1
    for i in range(len(carre)):
        somme1 = 0
        somme2 = 0
        for a in range(len(carre)):
            somme2 += carre[a][i]
        for a in carre[i]:
            somme1 += a
        if constante == -1:
            if somme1 == somme2:
                constante = somme1
            else:
                return -1
        elif constante != somme1 or constante != somme2:
            return -1
    return constante


def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre
    si toutes les colonnes ont la même somme, et -1 sinon """
    pass


def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre
    si les 2 diagonales ont la même somme, et -1 sinon """
    somme1, somme2 = 0, 0
    for i in range(len(carre)):
        somme1 += carre[i][i]
        somme2 += carre[3-i][i]
    if somme1 == somme2:
        return somme1
    else:
        return -1


def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    if testLignesEgales(carre) == -1 or testDiagonalesEgales(carre) == -1:
        return False
    else:
        return True


def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille
        du carré, et False sinon """
    n = len(carre[0])
    for i in range(1, (n ^ 2)+1):
        pasla = True
        for a in range(n):
            if i in carre[a]:
                pasla = False
                break
        if pasla:
            return False
    return True


carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
# carre_pas_mag = deepcopy(carre_mag)
carre_pas_mag = [list(i) for i in carre_mag]
carre_pas_mag[3][2] = 7


afficheCarre(carre_mag)
print(testLignesEgales(carre_mag))
print(testDiagonalesEgales(carre_mag))
print(estCarreMagique(carre_mag))
print(estNormal(carre_mag))

afficheCarre(carre_pas_mag)
print(testLignesEgales(carre_pas_mag))
print(testDiagonalesEgales(carre_pas_mag))
print(estCarreMagique(carre_pas_mag))
print(estNormal(carre_pas_mag))
