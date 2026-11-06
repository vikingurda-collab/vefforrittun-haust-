def summa():
    samtals=0
    for i in range (0,len(listi)):
        samtals += listi[i]
    return samtals

def safntidni():
    summ=0
    safnt=[]
    for i in range (0, len(listi)):
        summ += listi[i]
        safnt.append(summ)
    return safnt

def rada():
    listi.sort()
    return listi

listi = []
svar = int(input("hvað viltu margar tölur? : "))
for i in range(svar):
    listi.append(int(input("sláðu inn tölu: ")))
print(listi)
print("summan er:", summa())
print("safntíðni er:", safntidni())
print("listinn raðaður:", rada())