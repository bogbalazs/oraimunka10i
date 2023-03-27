ismetles = True
while (ismetles):
    elsoszam = int(input("Kérem az első számot ")) 
    masodikszam = int(input("Kérem a második számot ")) 
    if elsoszam < masodikszam  :
        print(masodikszam)
        ismetles = False
    if masodikszam < elsoszam:
        print( elsoszam )
        ismetles = False             