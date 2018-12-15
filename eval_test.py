#x = int(input( " entrez un nombre : "))
#def est_pair(x):

#    if x%2 == 0:
#        return True
#    else:
#        return False

#nombre = est_pair(x)

#print(nombre)


#def supprimer_voyelles(string):
#    trans = str.maketrans('', '', 'aàäâAeééèêëEiiîïIoOuUôö')
#    return string[0] + string[1:].translate(trans)

#def calculer_vitesse(t,m):

#    return round((3.6*(m/t)),1)

#def est_palindrome(texte):
#  texte = texte.lower()
 # a_retirer = {
#        'a': ['à', 'ã', 'á', 'â'],
#        'e': ['é', 'è', 'ê', 'ë'],
#        'i': ['î', 'ï'],
#        'u': ['ù', 'ü', 'û'],
#        'o': ['ô', 'ö'],
#        'y': ['ÿ'],
#        'n': ['ñ'],
#        '' : [",", ".", ";", ":", "!", "/", "?","'",'"',"«", "»", " — ", "’", " ","-"]
#  }

 # for (cle, valeur) in a_retirer.items():
#    for possibilite in valeur:
#      texte = texte.replace(possibilite, cle)

 # i = len(texte)
#  palindrome = ""
#  c = i - 1

#  while c > -1:
#      palindrome += texte[(c-i)]
#      c -= 1
#  if palindrome == texte:
#      return True
 # else:
#      return False

def exchange_variables(var1,var2):

  var3=var2
  var2=var1
  var1=var3

  return(var1,var2)

print(exchange_variables(var2))
