##################################
# fichier 03-deux-rectangles-obligatoire.py
# nom de l'exercice : Deux rectangles
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=5
# type : obligatoire
#
# Chapitre : chapitre-4-fonctions
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

def rectangles(caractere, nbLignes, nbCaracteres):
   
   for loop in range(nbLignes):
      for loop in range(nbCaracteres):
         print(caractere, end = "")
      print("")

rectangles('X', 4, 10)
rectangles('O', 6, 5)
