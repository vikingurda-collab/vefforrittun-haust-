
svar = "j"

while svar == "j":
    tala=int(input("sláðu inn póstnúmer: "))

    if tala in range(101, 111):
        print("Reykjavík")
    elif tala in (112, 113, 116):
        print("Reykjavík")
    elif tala in (170, 172):
        print("Seltjarnarnes")
    elif tala == 190:
        print("Vogum")
    elif tala in (200, 201, 202, 203):
        print("Kópavogur")
    elif tala in (210, 212):
        print("Garðabær")
    elif tala in (220, 221, 222):
        print("Hafnafjörður")
    elif tala == 225:
        print("Álftarnes")
    elif tala in (230, 232, 233, 235):
        print("Reykjanesbær")
    elif tala == 240:
        print("Grindavík")
    elif tala == 245:
        print("Sandgerði")
    elif tala == 250:
        print("Garði")
    elif tala == 260:
        print("Reykjanesbær")
    elif tala in (270, 271, 276):
        print("Mosfellsbær")
    else:
        print("ekki til")
    svar = input("aftur j/n: ").lower()