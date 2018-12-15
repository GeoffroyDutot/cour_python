"""programme qui donne la taille d'un dossier en Mo"""

import os

#Lister les fichiers/dossiers contenus dans un dossiers
#print(os.listdir(C:\\Windows))
Battlenet = "D:\\Battle.net\\Battle.net.exe"
print(os.path.isfile(Battlenet))
print(os.path.getsize(Battlenet))
