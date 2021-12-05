



#---------------------------------------------------------




def ecrire_fichier(score,nom_du_fichier = "score"):
    obFichier = open(str(nom_du_fichier),"w")
    score = str(score)
    obFichier.write(score)
    obFichier.close()



#--------------------------------------------------------



def lire_fichier(nom_du_fichier):
    try:
        fichier = open(str(nom_du_fichier),"r")
        texte = fichier.read()
        print(texte)
        fichier.close()
    except:
        print("Le fichier " + nom_du_fichier + " est introuvable.")


#lire_fichier("Monfichier.txt")

#--------------------------------------------------------




def enumere(texte):
    chiffre = 0
    while chiffre < 100:
        espaces = 1#""
        for lettre in texte:
            ecrire_fichier(espaces + lettre + "\n","test.txt")
            espaces = espaces + 1#" "
            chiffre = chiffre + 1
    print(espaces)
    print(chiffre)
    
    
enumere("william")
