x=True
while x:
    text=str(input("Sláðu inn texta: "))
    t=str(input("Sláðu inn staf: "))
    print(text.count(t))
    oppositetext=text[::-1]
    print(oppositetext)
    y=str(input("Viltu halda áfram? (j/n)"))
    if y=="n":
        x=False
