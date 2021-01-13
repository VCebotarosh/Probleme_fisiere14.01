with open ("H:\Vlad\Informatica\probleme_fisiere14.01\globulete.txt","r") as f:
    globulete_albe=f.readline()
globulete_rosii=int(globulete_albe)+3
globulete_albastre=globulete_rosii+int(globulete_albe)-2
total_globulete=int(globulete_albe)+globulete_rosii+globulete_albastre
with open( "H:\Vlad\Informatica\probleme_fisiere14.01\Bradut.txt","w") as f:
    f.write(str(total_globulete))