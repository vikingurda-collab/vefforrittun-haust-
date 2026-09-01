svar = "j"

while svar == "j":
    tala1 = int(input("sláðu inn tölu frá 1 til 10 til að margfalda: "))

    print("margföldunartafla fyrir", tala1)
    for tala2 in range(1, 11):
        print(tala1, "x", tala2, "=", tala1 * tala2)

    svar = input("aftur j/n: ").lower()
