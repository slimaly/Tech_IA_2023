

#Dans un fichier script, A l'aide de la fonction while et la fonction input (help(input)) écrivez cette blague
#"Si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste?"
#si la personne répond "repète", le programme pose la meme question : "Si repete et pepete sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste?"
#si la personne répond autre chose le programme pose comme question: "Mais non tu comprends pas, si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste "
#si la personne répond "tu es lourd" enfin le programme s'arrete




resultat = input()

while resultat != "tu es lourd":
    if resultat == "répète":
        input("Si repete et pepete sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste?")
    else:
        input("Mais non tu comprends pas, si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste")

print ("Le jeu est fini")
  

    

