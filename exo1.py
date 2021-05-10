import os
dfr,dfw = os.pipe()
pid = os.fork()
signal = 'Hello world'.encode()
signal=bytes(signal)

if pid == 0 : #si c'est le fils
    os.close(dfr) #on ferme la lecture
    os.write(dfw,signal) #on écrit le signal dans le pipe
    os.close(dfw) #on n'oublie pas de fermer l'écriture

else : #si c'est le père
    os.close(dfw) #on ferme l'écriture
    reception_pid_fils = os.read(dfr,signal) #on lit le message
    print(reception_pid_fils)
    os.close(dfr) #on n'oublie pas de ferme le lecteur