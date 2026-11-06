fin=open("nofn2.txt")
teljar=0
for line in fin:
    word = line.strip()
    if len(word) > 30:
        teljar += 1
        print(word)
print("Fjöldi orða sem eru lengri en 30 stafir:", teljar)
print("##################################################")
fin = open("nofn2.txt")
count=0
for line in fin:
    teljari2=0
    word = line.strip()
    for stafur in word:
        if stafur == " ":
            teljari2 += 1
    if teljari2 == 3:
        print(word)
        count += 1
print("Fjöldi nafna sem eru með 3 bil:", count)