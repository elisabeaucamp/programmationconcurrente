import os, sys, signal, time
def arreter_programme(signal,frame) :
    print("un signal a ete recu")
    sys.exit(0)

signal.signal(signal.SIGINT,arreter_programme)
pid = os.fork()
if pid!=0 :
    for i in range(3) :
        time.sleep(1)
        print("une seconde de plus du papa")
    os.kill(pid,signal.SIGKILL)
else :
    while True :
        time.sleep(1)
        print("une seconde de plus du fiston")

sys.exit(0)