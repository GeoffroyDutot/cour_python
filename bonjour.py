"""Programme qui dit bonjour et dit si vous êtes majeur ou mineur"""
nom = input("Quel est votre nom ? ")
age = input("Quel est votre âge ? ")
while age.isnumeric() ==False:
    print("Veuillez taper un entier")
    age = input("Quel est votre âge ? ")
age= int(age)
print("Bonjour",nom,"!")
if age>= 18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")
