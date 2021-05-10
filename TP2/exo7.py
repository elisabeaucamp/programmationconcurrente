import os,sys
N = 3
nb = 0
tot = 4^N
for i in range(N) :
    if os.fork() :
        if os.fork() :
            os.fork()
            nb +=1
print("Bonjour")
print(nb)
os._exit(0)