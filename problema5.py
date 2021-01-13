with open("H:\Vlad\Informatica\probleme_fisiere14.01\cifra.txt","r") as f:
    cifra=f.readline()
with open("H:\Vlad\Informatica\probleme_fisiere14.01\inmultire.txt","w") as f:
    for i in range(11):
        numar=int(cifra)*i
        inmultire=str(i)+"x"+cifra+"="+str(numar)
        f.write(inmultire)
        f.write("\n")