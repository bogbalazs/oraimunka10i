import random
#random.seed(0)
gondolt = random.randint(1,100)
print(gondolt)
while 
int(input("Hány éves vagy"))

'''
# tipp = int(input"kérem a tippet")
ismetles = True
while (ismetles):
    tipp = input("kérem a tipped")
    tipp = int(tipp)

    if tipp < gondolt:
        print("kicsi")
    if tipp > gondolt:
        print("Nagy")
    if tipp == gondolt:
        print("talalt")
        ismetles = False
'''

szam=0
tipp =0
while (tipp != gondolt):
    tipp = input("kérem a tipped")
    tipp = int(tipp)
    szam +=1

    if tipp < gondolt:
        print("kicsi")


    else: 
     if tipp > gondolt:
             print("Nagy")
print("Talált")
print("Ennyiszer probálkoztál", szam)
   













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
