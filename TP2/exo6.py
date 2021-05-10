import os,sys,time,random
for i in range(4) :
    if os.fork() != 0 :
        break
random.seed()
delai = random.randint(0,4)
time.sleep(delai)
print("Mon nom est "+chr(ord('A')+i)+" j ai dormi "+str(delai)+" secondes")
sys.exit(0)

#D A B C D
#random entre toutes les 4 lettres et le D en double
