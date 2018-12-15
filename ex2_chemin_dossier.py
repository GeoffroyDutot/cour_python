import os

#Lister les fichiers/dossiers contenus dans un dossiers
#print(os.listdir(C:\\Windows))
chemin = input("Chemin de dossier : ")
while os.path.exists(chemin) == False:
    chemin = input("Mauvais chemin ! Veuillez le resaisir ")
print("Votre dossier existe")
