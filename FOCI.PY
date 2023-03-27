#beolvasás
f=open("meccs.txt")
darab=f.readline()
#adatok=f.readlines()
adatok=[]
for sor in f:
    #print(sor.replace("\n","").split(" "))
    adatok.append(sor.replace("\n","").split(" "))
f.close()

#print(adatok)

CsapatokHazai=set()
CsapatokVendeg=set()
for merkozes in adatok:
    #print(merkozes[5])
    CsapatokHazai.add(merkozes[5])
    CsapatokVendeg.add(merkozes[5])

#print(CsapatokHazai)
#print(CsapatokVendeg)

#print(CsapatokHazai == CsapatokVendeg)

Csapatok=[]
for Csapat in CsapatokHazai:
    Csapatok.append(Csapat)

#print(Csapatok)
Csapatok.sort()
#print(Csapatok)

f=open('csapatok.txt',"w")
for cs in  Csapatok: 
    f.write(cs)
    f.write("\n")
f.close

max=adatok[0][0]
for fordulo in adatok:
    if int(max) < int(fordulo[0]):
        max=fordulo[0]
print(max,"Fordúlóból állt!")


max=adatok[0][1]
for gol in adatok:
    if int(max) < int(gol[1]):
        max=fordulo[1]
    if int(max) < int(gol[1]):
        max=fordulo[1]
print(max,"gól állt!")







































































