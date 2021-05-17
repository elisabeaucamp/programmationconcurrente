import os,sys,signal
def arreter_programme(signal,frame) :
    print("un signal a ete recu")
    sys.exit(0)
signal.signal(signal.SIGINT, arreter_programme)
print("Le programme va boucler...")
while True :
    continue