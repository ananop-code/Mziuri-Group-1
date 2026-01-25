f1=open("ricxvebi.txt", "r")
ricxvebi=f1.readlines()
f1.close()
f2=open("shedegi.txt", "w")
for x in ricxvebi:
    n=int(x.strip())
    kvadrati=n**2
    f2.write(str(kvadrati)+"\n")
f2.close()
print("warmatebis chaiwera failshi")