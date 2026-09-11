svar = "j"

while svar == "j":
    linur=int(input("sláðu inn hversu margar línur þú vilt: "))
    for i in range(0, linur):
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    svar = input("aftur j/n: ").lower()
