leita = input("Hvað viltu leita: ")  # biður notanda um að slá inn leitarstreng
satt=False
with open(r"C:\Users\vikin\OneDrive\Desktop\FB\forr1\v34\nofn_v34.txt", encoding="utf-8") as fin:
    for line in fin:
        word = line.strip()  # fjarlægir whitespace í byrjun og enda línu
        if leita in word:  # ef leitarstrengurinn er í orðinu
            satt=True
            print("nafnið er í skjalinu")  # prentar orðið
if satt == False:
    print("nafnið fannst ekki í skjalinu, reyndu án íslenska stafa")

print("#################################################################")

teljari_max = 0 #geymir hvað lengsta orðið er langt
teljari_min = 1000 #geymir hversu stutt styðsta orðið er
with open(r"C:\Users\vikin\OneDrive\Desktop\FB\forr1\v34\nofn_v34.txt", encoding="utf-8") as fin:
    for line in fin:
        word = line.strip()  # fjarlægir whitespace í byrjun og enda línu
        if len(word)>teljari_max:
            teljari_max=len(word)
        if len(word)<teljari_min:
            teljari_min=len(word)
print("lengsta nafnið er: ", teljari_max, " á lengd")
print("minnsta nafnið er: ", teljari_min, " á lengd")

print("#################################################################")

with open(r"C:\Users\vikin\OneDrive\Desktop\FB\forr1\v34\nofn_v34.txt", encoding="utf-8") as fin:
    for line in fin:
        word = line.strip()  # fjarlægir whitespace í byrjun og enda línu
        if len(word)==teljari_max:
            print("þetta er lengsta orðið:", word)
        elif len(word)==teljari_min:
            print("þetta er eitt af stystu orðum:", word)