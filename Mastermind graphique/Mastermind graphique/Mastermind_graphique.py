import json
import string
import random
from tkinter import *

#liste_couleur = {'R':'1', 'V':'2', 'B':'3', 'J':'4','O':'5','N':'6','M':'7','G':'8'}
liste_couleur = ['R', 'V', 'B', 'J','O','N','M','G']
combinaison_finale = []
nbredessaimax=12

#######################################################################################################################
def mode()-> int:
    parametre1 = 0
    print("Quelle mode de jeu ? (1 = 1joueur ou 2 = 2joueurs)")
    while(parametre1 != 1 and parametre1 !=2):
        parametre1 = int(input())
    return parametre1

def nbremanche() -> int :
    n=0
    print ("Combien de manches ? ")
    while n<0 :
        n : int(input()) 
    return n

def choix4couleurs (liste:str):
    print("Votre proposition ? ")
    i=0
    while i<4:
        n = str(input())
        while((n in liste_couleur) == False):
            print("saisie incorrect? veuillez resaisir")
            n = str(input())
        liste.append(n)
        n='pas dans la liste'
        i=i+1

def choix4couleurs2 (liste:str):
    print("Votre proposition ? ")
    i=0
    n = 0
    while i<4:
        while(int(n) <1 or int(n)>8):
            n = str(input())
            liste.append(liste_couleur[str(n)])
        n=0
        i=i+1

def initmemoire():
    data= []
    with open("tentative.json", "w+") as file:
        json.dump(data, file)
#######################################################################################################################

#def mode1joueur(nbr_manche:int) :
#rouge, jaune, vert, bleu, orange, noir, marron, fuchsia

def memoire(i:int, tenta:list, languet:list):
    thing = {"tentative" : i, "couleur" : tenta, "reponse":languet}
    #1 read
    with open("tentative.json", "r") as T:   
        data = json.load(T)
    #2 UPDATE
    data.append(thing)
    #3 write json file
    with open("tentative.json", "w") as file:
        json.dump(data, file)

#création du joueur
def initjoueur():
    prenom = ""
    print("Saisir le nom du joueur : ")
    prenom = str(input())
    return prenom

#compte des billes bonne couleur/Bien placé
def comparaison(tentative:list):
    languette = [0, 0]  #première valeur languette blache seconde languette rouge
    for i in range(4):
        for y in range(4):
            if(tentative[i]==combinaison_finale[y] and i == y):
                languette[1] += 1
            if(tentative[i] == combinaison_finale[y]):
                languette[0] += 1
    languette[0]=languette[0]-languette[1]
    print(languette)
    return languette

#Tentative de combinaison
def tupeuxpastest(joueurchoisi:str, joueurautre:str)-> list:
    i = 0
    languet = [0, 0]
    while(i<nbredessaimax and languet[1]!=4):
        tentative = []
        print("Tentatice numéro : ", i+1, "choisir une combinaison : ", joueurautre)
        choix4couleurs(tentative)
        languet = comparaison(tentative)
        print("il y a ", languet[0]," de billes de bonne couleur mais pas bien placer" )
        print("il y a ", languet[1]," de billes de bonne couleur et bien placer" )
        i=i+1
        memoire(i, tentative, languet)
    if(languet[1]==4):
        print(joueurautre, "a Gagné")
    else:
        print(joueurchoisi, "a Gagné")
        score[joueurchoisi] += 1

# ICI CHOIX DE LA COMBINAISON A TROUVER
def mode2joueurs(nbr_manche:int) :
    joueur1=initjoueur()
    joueur2=initjoueur()
    score = {joueur1:0, joueur2:0}
    t= ""
    while t!=joueur1 and t!=joueur2:
        print("Quelle joueur commence a choisir la combinaison ? (nom du joueur attendu)")
        t=str(input())
    if(t==joueur1):
        print(joueur1, " fait votre composition a deviner : ")
        choix4couleurs(combinaison_finale)
        tupeuxpastest(joueur1, joueur2)
    else:
        print(joueur2, " fait votre composition a deviner : ")
        choix4couleurs(combinaison_finale)
        tupeuxpastest(joueur2, joueur1)

def mode1joueurs(nbr_manche:int) :
    print("Rien")

#m=mode()
#nbrm=nbremanche()
#initmemoire()
#if m==1:
#    mode1joueur()
#else:
#    mode2joueurs(nbrm)

##############################################################################################
#graphique

root = Tk()
root.title('Mastermind')
root.resizable(True, True)

Label(root,
      text='[F1] À propos - [F2] Paramètres - [F5] Nouvelle partie - [ESC] Quitter',
      foreground="white",
      background="blue").pack(anchor=N, fill=X)

# Create the game area:
fenetredejeu = GameArea(text="Zone de jeu")
fenetredejeu.pack(anchor=N, expand=True, fill=BOTH)

