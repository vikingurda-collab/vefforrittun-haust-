from random import randint
tala= (randint(1,10))

guess=int(input("sláðu inn tölu frá 1 til 10: "))

if guess == tala:
    print("þú giskaðir rétt")
elif guess < tala:
    print("þú giskaðir of lágt tala er", tala)
elif guess > tala:
    print("þú giskaðir of hátt tala er", tala)
else:
    print("þú valdir rangan tölu")
