import os, sys
for i in range(3) :
    pid = os.fork()
    print("(i : ", i,") je suis le processus ",os.getpid(),",mon père est ",os.getppid(),",retour",pid)