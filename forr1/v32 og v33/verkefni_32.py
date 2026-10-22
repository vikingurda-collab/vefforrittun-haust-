fin=open("C:\\Users\\vikin\\OneDrive\\Desktop\\FB\\forr1\\v32\\words.txt") #opnar words.txt í breytuni fin
for line in fin:
    word=line.strip() #fjarlægir whitespace í byrjun og enda línu
    if len(word) > 20:
        print(word)

print() #prentar tóma línu
leita=str(input("Hvað viltu leita: ")) #biður notanda um að slá inn leitarstreng
fin=open("C:\\Users\\vikin\\OneDrive\\Desktop\\FB\\forr1\\v32 of v33\\words.txt") #opnar words.txt í breytuni fin upp á nýtt
for line in fin:
    word=line.strip() #fjarlægir whitespace í byrjun og enda línu
    if leita in word: #ef leitarstrengurinn er í orðinu
        print(word) #prentar orðið

print() #prentar tóma línu
samtals = 0 #breyta sem heldur utan um fjölda orða sem innihalda leitarstrenginn
leita2=str(input("Hvað viltu leita: ")) #biður notanda um að slá inn leitarstreng
fin=open("C:\\Users\\vikin\\OneDrive\\Desktop\\FB\\forr1\\v32\\words.txt") #opnar words.txt í breytuni fin upp á nýr
for line in fin:
    word=line.strip() #fjarlægir whitespace í byrjun og enda línu
    for stafur in word:
        if stafur == leita2: #ef leitarstrengurinn er í orðinu
            samtals += 1 #ef leitarstrengurinn er í orðinu þá hækkar samtals um 1
print(f"Fjöldi orða sem innihalda '{leita2}': {samtals}")