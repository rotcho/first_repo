#fichier: TP5_lit_ecrit.py
#auteur: OKILA Romain SP1 B2
#date : 28/04/21

# ---------- imports ----------
# ---------- définitions de fonctions ----------

#-------Programme Principal-------

f=open("data1.txt","w",encoding="utf-8") #on crée le fichier
f.write("Mon premier fichier texte,\n") #on ecrit dans le ficher
f.write("écrit a partir d'un programme,\n") #
f.write("tout en automatique (une fois le script écrit).\n")
f.close() #refermer le ficher crée

#lecture d'un bloc:
f1=open("data1.txt", "r", encoding="utf-8") #ouvrir le ficher "r" pour read
tout= f1.read() #pour lire le bloc
print(tout) #pour ecrire le bloc
type(tout)
f1.close() #fermer le bloc

#lecture ligne par ligne du fichier, affichant pour chaque ligne son n° et son contenu :
f1=open("data1.txt", "r", encoding="utf-8") #ouvrir le ficher "r" pour read
type(f1)
a=f1.readline()
print("n°1 "+a) #afficher la 1er ligne + le n° de la ligne
b=f1.readline()
print("n°2 "+b) #afficher la 2ème ligne + le n° de la ligne
c=f1.readline()
print("n°3 "+c) #afficher la 3ème ligne + le n° de la ligne
f1.close() #fermer le programme

#on ajoute le numero des lignes 4 à 100 après :'je suis a la ligne'
for i in range(4,101):
    print("je suis a la ligne n°",i)

# ---------- résultats de l'exécution ----------
"""
Running script: "C:\Users\romainokila\Documents\cours mp\info tp\tp5\TP5_lit_ecrit.py"
Mon premier fichier texte,
écrit a partir d'un programme,
tout en automatique (une fois le script écrit).

n°1 Mon premier fichier texte,

n°2 écrit a partir d'un programme,

n°3 tout en automatique (une fois le script écrit).

n°1 Mon premier fichier texte,

n°2 écrit a partir d'un programme,

n°3 tout en automatique (une fois le script écrit).

je suis a la ligne n° 4
je suis a la ligne n° 5
je suis a la ligne n° 6
je suis a la ligne n° 7
je suis a la ligne n° 8
je suis a la ligne n° 9

...

"""