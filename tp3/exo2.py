import os,sys
fichier = "exo2.txt"
chaine = "est"

#creation du pipe premier pipe
(dfr1,dfw1) = os.pipe()

#separation des processus
pid1 = os.fork()
if pid1 == 0 : #le fils va se charger des commandes
    os.close(dfr1) #on va juste écrire dans le premier pipe
    os.dup2(dfw1,1)
    os.close(dfw1)
    os.execlp('sort','sort',fichier)

else :
    (dfr2,dfw2) = os.pipe() #on crée un 2e pipe
    pid2 = os.fork()


    if pid2 == 0 :
        os.close(dfw1) #on va juste lire la sorte du premier pipe
        os.dup2(dfr1,0)
        os.close(dfr1)

        os.close(dfr2) #on va écrire à l'entrée du deuxième pipe
        os.dup2(dfw2,1)
        os.close(dfw2)

        os.execlp('grep','grep',chaine)

    else :
        os.close(dfr1)
        os.close(dfw1)

        os.close(dfw2) #on va lire la sortie du deuxième pipe
        os.dup2(dfr2,0)
        os.close(dfr2)
        sortie.write(os.execlp('tail','tail','-n','5'))
sys.exit(0)