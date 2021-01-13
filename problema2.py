with open ("H:\Vlad\Informatica\probleme_fisiere14.01\cifre.txt","r") as f:
    a=f.readline()
    b=f.readline()
if int(a)>int(b):
    x=int(a)*2
    y=int(b)*3
elif int(a)<int(b):
    x=int(b)*2
    y=int(a)*3
elif int(a)==int(b):
    x=y="NUmerele sunt egale"
with open("H:\Vlad\Informatica\probleme_fisiere14.01\produs.txt","w") as f:
    f.write(str(x))
    f.write("\n")
    f.write(str(y))