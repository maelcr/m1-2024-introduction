import re
import random
import keyboard

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
        if ((i%isDivisible)==0 and (i%notDivisible)!=0):
            liste_return.append(i)
        i+=1
    return liste_return


"""
Question 02:

En considérant un nombre de départ n, créer une liste contenant l'ensemble des carrés de tous les nombres allant jusqu'à n.

Exemple: SquaredNumbers(n=4) --> [0, 1, 4, 9, 16]
"""
def SquaredNumbers(n=4):
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
    pwd_checked_list=[]
    pwd_list=sequence.split(",")
    i=0
    minu=re.compile('[a-z]+')
    maju=re.compile('[A-Z]+')
    chiffre=re.compile('[0-9]+')
    while(i<len(pwd_list)):
        pwd_checked_list.append(pwd_list[i])
        #pwd_checked_list[i]=0
        if(len(pwd_list[i])>=6 and len(pwd_list[i])<=12):
            if(pwd_list[i][0]=="?" or pwd_list[i][0]=="#" or pwd_list[i][0]=="@"):
                if(re.search(minu,pwd_list[i])!=None and re.search(maju,pwd_list[i])!=None and re.search(chiffre,pwd_list[i])!=None):
                    pwd_checked_list[i]=1
        i+=1
    return pwd_checked_list

def PwdCheck2(sequence: list):
    pwd_checked_list=[]
    pwd_list=sequence
    i=0
    minu=re.compile('[a-z]+')
    maju=re.compile('[A-Z]+')
    chiffre=re.compile('[0-9]+')
    while(i<len(pwd_list)):
        pwd_checked_list.append(pwd_list[i])
        #pwd_checked_list[i]=0
        if(len(pwd_list[i])>=6 and len(pwd_list[i])<=12):
            if(pwd_list[i][0]=="?" or pwd_list[i][0]=="#" or pwd_list[i][0]=="@"):
                if(re.search(minu,pwd_list[i])!=None and re.search(maju,pwd_list[i])!=None and re.search(chiffre,pwd_list[i])!=None):
                    pwd_checked_list[i]=1
        i+=1
    return pwd_checked_list



"""
Question 05:

La fonction doit être capable de générer un nombre n de mots de passes conformes à la Question 04, et les renvoie sous forme d'une chaîne de caractères

Ex: PwdGen(3) --> "?N21m8O,@y9RJ8J,@c2d01I"
"""
def PwdGen(n=100):
    #sinon possibilité de passer par ascii"
    lettre_min=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","w","x","y","z"]
    carac_spe=["?","#","@"]
    i=0
    minu=re.compile('[a-z]+')
    maju=re.compile('[A-Z]+')
    chiffre=re.compile('[0-9]+')
    liste_mdp_return=[]
    while(i<n):
        mdp_n=""
        mdp_n+=random.choice(carac_spe)
        y=1
        while(y<12):
            z=random.randrange(2)
            if(z==0):
                mdp_n+=random.choice(lettre_min)
            elif(z==1):
                mdp_n+=random.choice(lettre_min).upper()
            elif(z==2):
                mdp_n+=str(random.randrange(10))

            if((len(mdp_n)>=6 and random.randrange(2)==0) or len(mdp_n)==9):
                if not (re.search(minu,mdp_n)!=None and re.search(maju,mdp_n)!=None and re.search(chiffre,mdp_n)!=None):
                   mdp_n+=random.choice(lettre_min) 
                   mdp_n+=random.choice(lettre_min).upper()
                   mdp_n+=str(random.randrange(10))
                liste_mdp_return.append(mdp_n)
                y=12
            y+=1
        i+=1
    return liste_mdp_return


"""
Question 06:

Un robot se déplace dans un repère 2D. L'utilisateur peut le commander à l'aide des flèches directionnelles, déplacant le robot d'une case à chaque fois.
Calculer, en temps réel, la distance entre l'origine et le robot (en nb de cases). Le robot peut se trouver à des coordonnées négatives.
Utiliser la librairie keyboard pour détecter les touches du clavier.
""" 
    #correction prof
def RcRobot():
    pos = [0, 0]
    while True:
        if keyboard.is_pressed("UP"):
            pos[1] += 1
            print(f"Moving Up. I'm {abs(pos[0]) + abs(pos[1])}m away from origin.")
            while keyboard.is_pressed("UP"):
                pass
        elif keyboard.is_pressed("DOWN"):
            pos[1] -= 1
            print(f"Moving Down. I'm {abs(pos[0]) + abs(pos[1])}m away from origin.")
            while keyboard.is_pressed("DOWN"):
                pass
        elif keyboard.is_pressed("LEFT"):
            pos[0] -= 1
            print(f"Moving Left. I'm {abs(pos[0]) + abs(pos[1])}m away from origin.")
            while keyboard.is_pressed("LEFT"):
                pass
        elif keyboard.is_pressed("RIGHT"):
            pos[0] += 1
            print(f"Moving Right. I'm {abs(pos[0]) + abs(pos[1])}m away from origin.")
            while keyboard.is_pressed("RIGHT"):
                pass

#print(DivisibleCheck())
#print(SquaredNumbers())
#print(SquaredInterval())
#liste_100_code="?N21m8O,@y9RJ8J,@c2d01I,@4Eli0p,@qRktu6,#031uwcB,?955XT71c,@heD1P6,?nobQCoVUB9,?Lla13K,#Z4243r,@vSfyupZdC3oi,?R41gGo,?4wB2n1,?Z00Qb0,@080N0x,@EBB9RKk,#wAHk0y,?RLS21l,#Sm2pYC,?2D3ToV,?4py698b0I,BzRBsh8,?r3QJm4,?tDdoyOoqs8,@uZ39Y8,@7uY4c0,@MPWvq2,#Gy8dnb,#zbd2L0,?9m7uSF,?S2fcx1,?pmi9yG,#fP21Wj,@ljZGp5,#hW0d5x,@TqtunAX8,@d8o366vyL,@Fh516S,?Icy0Zz,#4fcwju5f4U,?ZzW2m2,?6xvtt4v3yF,@8D3P81FKf,?eOCdnb6,#lxZ8o7,@caFhwcFUx2,#995gM5,#qEDqsVD,?9W8dd7252f,@lhxz68pC,?7y78bV,#rBCJy3,@cLFrvdF4,@hmL34L,?6bZfX8,@i5T64J,@8S9WI74N4b,@0iCGOo,#hCucluCV5,?TG48zz,?i6BEk0,@2B9Vx2,#tMpRtfLMW6,@cHNMgt6,#5nW7U7,?7d811yG,@3yfJxS,?3pxZuY,?RU0WdT,#W6u253,@iu6SLD,?RGFw78,#17Eq5I,?7s8fvv6iY,#6edQnR,@wl7oH4,#0RKcam,?BBMtd5,?n6E3dN,#pIbrDJqt8,@5N3y02,@vr16gz,?650b0I,@933svJ,#29h6,#m462EB,#NyL2J1,?x3eOek,?1f14xaO,@RHnrrAVXJ8,@Gu0h31,?ODsSJlssj1,?72zD89,@yK4VCV,?UCex5Q,#4573d72aL,@J794T0A00d,@yvTSh6,#Oh5pxz"
#print(PwdCheck(liste_100_code))
#liste_n_code=PwdGen(100)
#print(liste_n_code)
#print(PwdCheck2(liste_n_code))
RcRobot()
