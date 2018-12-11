"""Programme qui dit bonjour et dit si vous êtes majeur ou mineur"""
nom = input("Quel est votre nom ? ")
age = input("Quel est votre âge ? ")
if age.isnumeric():
    age = int(age)
else:
    print("Veuillez taper un entier")
    exit()
print("Bonjour",nom,"!")
#si age>=18
if age>= 18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")
