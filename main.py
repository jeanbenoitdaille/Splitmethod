    def separateur(mot, sep):
        liste = []
        mot_courant = ""
     
        for lettre in mot:
    	if lettre != sep:
    	    mot_courant += lettre
    	else:
    	    liste.append(mot_courant)
    	    mot_courant = ""
     
        liste.append(mot_courant)
        return liste
     
    phrase = "bonjour-tout-le-monde"
    print(separateur(phrase, "-"))
