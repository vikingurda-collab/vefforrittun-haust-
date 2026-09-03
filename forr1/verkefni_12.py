from random import randint

aftur=True
while aftur:
    for leikir in range(1,14):
        print(f"Leikur {leikir}")
        stig=randint(1,3)
        if stig == 1:
            print(1)
            aftur=False
        elif stig == 2:
            print(2)
            aftur=False
        elif stig == 3:
            print("x")
            aftur=False