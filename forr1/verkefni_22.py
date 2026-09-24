listi = list(["lion", "tiger", "cat", "dog", "humano"])
print (len (listi))
print("dúrin eru:", end=" ")
for i in listi:
    print(i,end=" ")
for m in range(0,3):
    listi.append (str(input("Sláðu inn dýr: ")))
print ("svona lítur listinn minn út: ", listi)