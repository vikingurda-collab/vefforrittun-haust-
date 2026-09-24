listi = list(["Anton", "Aron", "Asgeir", "Elvar", "Víkingur", "Eggert", "Embla", "Ari", "Sindri", "Haraldur"])
strengur="Háfjallaveiki"
listi.sort()
print("Nofnin eru: ", end=" ")
for i in listi:
    print(i, end=" ")
print()
print(listi[5:8])
print(listi[-4:])

print(strengur[2:7])

print(strengur[8:])

print(strengur[0:2], strengur[8:])