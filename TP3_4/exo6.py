import os, sys, signal, time
def arreter_programme(signal,frame) :
    print("un signal a ete recu")
    sys.exit(0)

def freception(s,frame) :
    print("signal recu")
    signal.signal(signal.SIGINT,freception)
    sys.exit(0)

#signal.signal(signal.SIGINT,arreter_programme)
pid = os.fork()
if pid!=0 :
    signal.signal(signal.SIGINT,signal.SIG_IGN)
    for i in range(3) :
        time.sleep(1)
        print("une seconde de plus du papa")
    
else :
    signal.signal(signal.SIGINT,freception)
    while True :
        time.sleep(1)
        print("une seconde de plus du fiston")
    
sys.exit(0)         