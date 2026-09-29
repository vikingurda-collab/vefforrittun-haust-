u = str(input(""))
while len(u) < 5:
    u = str(input(""))
while len(u) > 100000:
    u = str(input(""))
print(len(u))