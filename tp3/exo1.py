import os,sys
a = 10
import multiprocessing as mp
msg='hello'
msg=msg.encode('ascii')
(dfr,dfw)=os.pipe()
n=os.write(dfw,msg)
print('Le processus %d a tansmis le message %s \n' %(os.getpid(),msg.decode('ascii')))
msg_recu = os.read(dfr,len(msg))
print('Le processus %d a recu le mesage %s \n' %(os.getpid(),msg_recu.decode('ascii')))
os.close(dfr);os.close(dfw)
sys.exit(0)