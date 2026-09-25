dyr = list(["lion", "tiger", "cat", "dog", "humano"])
print (len (dyr))
print("dúrin eru:", end=" ")
for i in dyr:
    print(i,end=" ")
for m in range(0,3):
    dyr.append (str(input("Sláðu inn dýr: ")))
print ("svona lítur listinn minn út: ", dyr)
dyr.sort()
print("listinn í stafrófsröð: ")
for i in range(0, len(dyr)):
    print("dýr nr", i+1, "er", dyr[i])