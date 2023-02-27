#fügvényekről
def teszt():
    print("Szia!")

teszt("pisti")
teszt("Zoli")
teszt("Karcsi")
teszt("Ági")
#print(név)
def negyzet(x):
    n=x*x
 #   print(x)
    return n
negyzet(3)
print(negyzet(3))

harom=negyzet(3)
negy=negyzet(4)
ot=negyzet(5)
print(harom+negy/ot)

for i in range(1,101):
    x=negyzet(i)
    print(i,x)
print(x)