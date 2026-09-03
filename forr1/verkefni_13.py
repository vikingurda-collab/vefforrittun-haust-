
from random import randint
print("Já þetta á að virka svona")


u = True
while u == True:
    for leikir in range(1,101):
        print(f"Leikur {leikir}")
        stig=randint(1,3)
        if stig == 1:
            print(1)
            u=str(input("Viltu spila aftur? (j/n)" ))
            if u == "n":
                u=False
                exit()
        elif stig == 2:
            print(2)
            u=str(input("Viltu spila aftur? (j/n)" ))
            if u == "n":
                 u=False
                 exit()
        elif stig == 3:
            print("x")
            u=str(input("Viltu spila aftur? (j/n)" ))
            if u == "n":
                u=False
                exit()
