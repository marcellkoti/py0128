import random

szam=random.randint(0,1100)
tipp=int(input("Melyik számra gondoltam?"))
darab = 1
while szam!= tipp:
    if(szam>tipp):
        print("Hibás! Nagyobbara gondoltam!")
    else:
        print("Hibás! Kissebbbre gondoltam!")
    tipp=int(input("Melyik számra gondoltam?"))
    darab+=1
print(f"Ügyes vagy a {szam} számra gondoltam!\n {darab} próbálkozásod volt!")
print()






