lönd = list(["Bandaríkin", "Bretland", "Svíþjóð", "Ísland", "Danmörk", "Finnland", "Spánn", "Norgegur", "Skotland", "Írland"])
svar = 1
while svar < 5:
    svar = int(input("sláðu inn tölu af löndum(min=5): "))
for i in range(0,svar):
    lönd.append(str(input("Sláðu inn nýtt land: ")))
lönd.sort()
print("Löndin eru: ", *lönd)
print("fjöldi landa er: ", len(lönd))
print("þriðja hvert land á listanum er: ",end=" ")
for i in range(0, len(lönd), 3):
    print(lönd[i], end=" ")
print()
print("landið í miðju er: ", lönd[round(len(lönd)/2)-1])
print("fyrstu stafir: ", end=" ")
for i in lönd:
    print(i[0], end=" ")
print()
z=round(len(lönd)/2)
for i in range(0,z):
    print(lönd[i], lönd[-(i+1)], end=" ")
