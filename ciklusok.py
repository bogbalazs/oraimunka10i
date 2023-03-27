''' végtelen ciklus
while True:
    print("ismét")
    print("2.sor") 

print("ciklus utan")


while False:
    print("ismét")
print ("ciklus után")
'''

'''
folytat=True
folytat=False
while folytat:
    valasz=input("folytad ? (i/n)")
    if valasz == 'i':
        folytat=True

    else :
        folytat= False


ciklusValtozo=1
while ciklusValtozo < 11 :
    print(ciklusValtozo,ciklusValtozo**2,sep="\t")
    ciklusValtozo +=1 
    print()
...
...
print ("ciklusutan")
    #print("/nciklus utan")

'''
'''print()
x=1/8
while  x != 1:
    x = x +1000000/800000000
    print(x)














    
   #for ciklus helyett
sor = {1,2,3,4}
# print(type(sor))

for i in sor:
    print(i)

sor = {"alma", "szilva", "ló", 4, "ló" }
for i in sor:
    print(i, end=",")
print()

sor= ("alma","szilva","ló",4, "ló" )
for i in sor:
    print(i ,end=",")
print()

for i in range (10):
   print(i ,end=",")
print()

for i in range (1,10):
   print(i ,end=",")
print()

for i in range (1,10,2):
   print(i ,end=",")
print()
print()
print()
'''
''''
for i in range (1,101):
   print(i ,i**2, sep=",")
   #print(srt(i)+","str(i**2))
print()
'''

szam=1
for sor in range(1,10):
    for oszlop in range(1,11):
        print(szam,end='\t')
        szam +=1
    print()
