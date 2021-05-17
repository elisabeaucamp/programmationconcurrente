import os,sys,signal
global fin
fin = False
def arreter_programme(signal,frame) :
    print("un signal a ete recu")
    fin = True
    sys.exit(0)
    
signal.signal(signal.SIGINT, arreter_programme)
print("Le programme va boucler...")
while fin == False :
    continue