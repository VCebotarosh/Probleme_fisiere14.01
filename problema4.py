with open("H:\Vlad\Informatica\probleme_fisiere14.01\input.txt","r") as f:
    numar=f.readline().strip()
numar1=str(int(numar)-2)
numar2=str(int(numar)-1)
numar4=str(int(numar)+1)
numar5=str(int(numar)+2)
with open("H:\Vlad\Informatica\probleme_fisiere14.01\output.txt","w") as f:
    f.writelines([numar1," ",numar2," ",numar," ",numar4," ",numar5])