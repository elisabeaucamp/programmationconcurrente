import os, sys
#print("PID du PERE : ",os.getpid())
pid = os.fork()
#print("PID du FILS : ", pid)
if pid == 0 :
    os.execlp("python","python","exo1prime.py")
    sys.exit()
else :
    os.execlp("python","python","exo1seconde.py")
    os.wait()
os._exit(0)