def supprimer_accents(mot):
  """votre doc ici"""
  #votre code ici
  mots_sans_accents = mot.replace("à", "a").replace("é","e").replace("è","e").replace("ê","e")
  return mots_sans_accents

mot = str(input("Entrez une chaîne de caractère : "))
mots_sans_accents = supprimer_accents(mot)
print("Votre mot sans accents : ", mots_sans_accents)
