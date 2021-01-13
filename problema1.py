with open ("H:\Vlad\Informatica\probleme_fisiere14.01\cifre.txt","r") as f:
    a=f.readline()
    b=f.readline()
if int(a)<int(b):
    x=a
elif int(a)>int(b):
    x=b
elif int(a)==int(b):
    x="Numerele sunt egale"
with open ("H:\Vlad\Informatica\probleme_fisiere14.01\minim.txt", "w") as f:
    f.write(x)