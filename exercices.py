"""
Question 01:

Ecrire un programme capable de renvoyer sous forme d'une liste tous les nombres étant divisibles par "isDivisible"
et n'étant pas divisibles par "notDivisible", appliqué à tous les nombres entre rangeMin et rangeMax.

Exemple: DivisibleCheck(isDivisible=5, notDivisible=2, rangeMin=1, rangeMax=7) --> [5]
"""
def DivisibleCheck(isDivisible=7, notDivisible=5, rangeMin=4000, rangeMax=5000):
    i=rangeMin
    liste_return=[]
    while(i<rangeMax):
        if ((i%isDivisible)==0):
            liste_return.append(i)
        if ((i%notDivisible)!=0):
            liste_return.append(i)
        i+=1
    return liste_return


"""
Question 02:

En considérant un nombre de départ n, créer une liste contenant l'ensemble des carrés de tous les nombres allant jusqu'à n.

Exemple: SquaredNumbers(n=4) --> [0, 1, 4, 9, 16]
"""
def SquaredNumbers(n=8):
    i=0
    liste_return=[]
    while(i<=n):
        liste_return.append(i**2)
        i+=1
    return liste_return



"""
Question 03:

En considérant un interval [rangeMin, rangeMax], stocker l'ensemble des carrés des nombres "n" allant de rangeMin à rangeMax indexés par n

Exemple:
result = SquaredInterval(rangeMin=8, rangeMax=100)
result[9] = 81
result[100] = 10000
"""
def SquaredInterval(rangeMin=8, rangeMax=100):
    i=rangeMin
    liste_return=[]
    while(i<=rangeMax):
        liste_return.append(i**2)
        i+=1
    return liste_return


"""
Question 04:

Une entreprise créé un système de mot de passe pour ses employés. 
La personne chargée des vérifications de mots de passe envoie en entrée d'un algorithme une suite de mots de passes séparés par une virgule.

Ces mots de passes doivent répondre à plusieurs critères :
- Le mot de passe doit contenir au moins une lettre minuscule [a-z]
- Le mot de passe doit contenir au moins une lettre majuscule [A-Z]
- Le mot de passe doit contenir au moins un chiffre [0-9]
- Le mot de passe doit commencer par un des symboles suivants [?#@]
- Le mot de passe doit faire au minimum 6 caractères
- Le mot de passe doit faire au maximum 12 caractères

La séquence à tester correspond dans l'ordre aux 100 employés de l'entreprise :
?N21m8O,@y9RJ8J,@c2d01I,@4Eli0p,@qRktu6,#031uwcB,?955XT71c,@heD1P6,?nobQCoVUB9,?Lla13K,#Z4243r,@vSfyupZdC3oi,?R41gGo,?4wB2n1,?Z00Qb0,@080N0x,@EBB9RKk,#wAHk0y,?RLS21l,#Sm2pYC,?2D3ToV,?4py698b0I,BzRBsh8,?r3QJm4,?tDdoyOoqs8,@uZ39Y8,@7uY4c0,@MPWvq2,#Gy8dnb,#zbd2L0,?9m7uSF,?S2fcx1,?pmi9yG,#fP21Wj,@ljZGp5,#hW0d5x,@TqtunAX8,@d8o366vyL,@Fh516S,?Icy0Zz,#4fcwju5f4U,?ZzW2m2,?6xvtt4v3yF,@8D3P81FKf,?eOCdnb6,#lxZ8o7,@caFhwcFUx2,#995gM5,#qEDqsVD,?9W8dd7252f,@lhxz68pC,?7y78bV,#rBCJy3,@cLFrvdF4,@hmL34L,?6bZfX8,@i5T64J,@8S9WI74N4b,@0iCGOo,#hCucluCV5,?TG48zz,?i6BEk0,@2B9Vx2,#tMpRtfLMW6,@cHNMgt6,#5nW7U7,?7d811yG,@3yfJxS,?3pxZuY,?RU0WdT,#W6u253,@iu6SLD,?RGFw78,#17Eq5I,?7s8fvv6iY,#6edQnR,@wl7oH4,#0RKcam,?BBMtd5,?n6E3dN,#pIbrDJqt8,@5N3y02,@vr16gz,?650b0I,@933svJ,#29h6,#m462EB,#NyL2J1,?x3eOek,?1f14xaO,@RHnrrAVXJ8,@Gu0h31,?ODsSJlssj1,?72zD89,@yK4VCV,?UCex5Q,#4573d72aL,@J794T0A00d,@yvTSh6,#Oh5pxz

Aide:
Séparer la séquence en une liste de mots de passes
Utiliser la librairie re pour chercher la présence de caractères dans chaque mot de passe
"""
def PwdCheck(sequence: str):
    return


"""
Question 05:

La fonction doit être capable de générer un nombre n de mots de passes conformes à la Question 04, et les renvoie sous forme d'une chaîne de caractères

Ex: PwdGen(3) --> "?N21m8O,@y9RJ8J,@c2d01I"
"""
def PwdGen(n=100):
    return


"""
Question 06:

Un robot se déplace dans un repère 2D. L'utilisateur peut le commander à l'aide des flèches directionnelles, déplacant le robot d'une case à chaque fois.
Calculer, en temps réel, la distance entre l'origine et le robot (en nb de cases). Le robot peut se trouver à des coordonnées négatives.
Utiliser la librairie keyboard pour détecter les touches du clavier.
"""
def RcRobot():
    pass

#print(DivisibleCheck())
#print(SquaredNumbers())
print(SquaredInterval())

