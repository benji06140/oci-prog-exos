##################################
# fichier 02e-une-ligne-sur-deux-obligatoire.py
# nom de l'exercice : Une ligne sur deux
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=7
# type : obligatoire
#
# Chapitre : chapitre-3-chaines-de-caracteres
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nbLignes = int(input())
ligne = [0] * nbLignes

for imprime in range(nbLignes):
   ligne[imprime] = input()
   if imprime % 2 == 0:
      print(ligne[imprime]
