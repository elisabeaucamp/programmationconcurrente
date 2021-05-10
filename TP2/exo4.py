import os,sys
n = 0
for i in range(1,5) :
    fils_pid = os.fork()
    if (fils_pid > 0) :
        n = i*2
        break;
print("n = ",n)
sys.exit(0)

#après le if, on est dans le père
#le pid vaut 0 pour le fils
#le programme est déterministe car il retourne toujours la même chose
#il est déterministe mais n'affiche plus dans le même ordre qu'avant, il n'attend plus
#lancer le programme
#parce qu'il n'y a plus assez d'espace mémoire ou alors si on en lance trop et que l'ordi ne peut plus gérer