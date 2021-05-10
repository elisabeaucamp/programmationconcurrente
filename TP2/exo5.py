import os,sys,time
N = sys.argv[1]
if len(sys.argv) == 2 :
    if N.isnumeric() == True :
        N = int(N)
else :
    sys.exit(0)
pid = os.getpid()
for i in range(N):
    if pid!= 0:
        pid = os.fork()
    else :
        print('PID fils : ',os.getpid())
        print('PID pere : ',os.getppid())
        time.sleep(2*i)
        sys.exit(i)
if pid !=0 :
    os.wait()
    print(pid)