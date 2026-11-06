def fornafn():
    leita = input("af hvaða fornafni viltu leita?: ")  # biður notanda um að slá inn leitarstreng
    satt=False
    listi=[]
    with open(r"C:\Users\vikin\OneDrive\Desktop\FB\forr1\v36og37\nofn.txt", encoding="utf-8") as fin:
        for line in fin:
            word = line.strip()  # fjarlægir whitespace í byrjun og enda línu
            listi=word.split(" ")
            if listi[0]==leita:
                satt=True
                print(word)  # prentar orðið
    if satt == False:
        print("nafnið fannst ekki í skjalinu, reyndu án íslenska stafa")

def eftirnafn():
    leita=input("af hvaða eftirnafni?: ")
    satt=False
    listi=[]
    with open(r"C:\Users\vikin\OneDrive\Desktop\FB\forr1\v36og37\nofn.txt", encoding="utf-8") as fin:
        for line in fin:
            word = line.strip()  # fjarlægir whitespace í byrjun og enda línu
            listi=word.split(" ")
            if listi[-1]==leita:
                satt=True
                print(word)  # prentar orðið
    if satt == False:
        print("nafnið fannst ekki í skjalinu, reyndu án íslenska stafa")

def foreftir():
    leita = input("af hvaða fornafni viltu leita?: ")  # biður notanda um að slá inn leitarstreng
    leita2=input("af hvaða eftirnafni?: ")
    satt=False
    listi=[]
    with open(r"C:\Users\vikin\OneDrive\Desktop\FB\forr1\v36og37\nofn.txt", encoding="utf-8") as fin:
        for line in fin:
            word = line.strip()  # fjarlægir whitespace í byrjun og enda línu
            listi=word.split(" ")
            if listi[0]==leita and leita2==listi[-1]:
                satt=True
                print(word)  # prentar orðið
    if satt == False:
        print("nafnið fannst ekki í skjalinu, reyndu án íslenska stafa")

def valmynd():
    print("###########################################")
    print("                   veljið                  ")
    print("              1(finnið fornafn)            ")
    print("              2(finnið eftirnafn)          ")
    print("              3(finnið bæði)               ")
    print("              4(stoppa forrit)             ")
    print("###########################################")

afram = True
while afram:
    valmynd()
    val=int(input("veljið: "))
    if val==1:
        fornafn()
    elif val==2:
        eftirnafn()
    elif val == 3:
        foreftir()
    else:
        exit()