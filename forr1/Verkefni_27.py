from random import randint

aftur = True
while aftur:              # keyrir meðan breytan er true
    samtals1 = 0          # samtals stig fyrir spilara 1
    samtals2 = 0          # samtals stig fyrir spilara 2
    running = True
    spilari1 = 'j'
    spilari2 = 'j'

    while running:        # keyrir meðan spilarar vilja spila
        if spilari1 == "j":
            para1 = randint(1, 13)
            samtals1 = samtals1 + para1
            print("Spilari 1 fékk", para1, "og samtals er", samtals1)
            spilari1 = input("Viltu fá annað para? (j/n)").strip().lower()
        if spilari2 == "j":
            para2 = randint(1, 13)
            samtals2 = samtals2 + para2
            print("Spilari 2 fékk", para2, "og samtals er", samtals2)
            spilari2 = input("Viltu fá annað para? (j/n)").strip().lower()

        print("Spilari 1 er með", samtals1, "stig og Spilari 2 er með", samtals2, "stig")

        if samtals1 > 21 and samtals2 > 21:
            print("Báðir spilarar fóru yfir 21, enginn vinnur")
            running = False
        elif samtals1 > 21:
            print("Spilari 1 fór yfir 21, Spilari 2 vinnur")
            running = False
        elif samtals2 > 21:
            print("Spilari 2 fór yfir 21, Spilari 1 vinnur")
            running = False
        elif spilari1 == "n" and spilari2 == "n":
            if samtals1 > samtals2:
                print("Spilari 1 vinnur með", samtals1, "stigum")
            elif samtals2 > samtals1:
                print("Spilari 2 vinnur með", samtals2, "stigum")
            else:
                print("Jafntefli, báðir spilarar eru með", samtals1, "stig")
            running = False

    breyta = input("Viltu byrja upp á nýtt? (j/n)").strip().lower()
    if breyta == "n":
        aftur = False

print("Takk fyrir að spila")
# rollin