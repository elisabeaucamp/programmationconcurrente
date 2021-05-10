import os,sys
#ecrire un programme qui dit qui on est, donne les répertoire du dossier et les pross qui m'appartiennent
pid0 = os.fork()
if pid0 == 0 :
    os.execlp("who","a")
os.wait() #passer du simultané au séquentiel
pid1 = os.fork()
if pid1 == 0:
    os.execlp("ps","a")
os.wait()
pid2 = os.fork()
if pid2 == 0 :
    os.execlp("ls","-l")
os.wait()