from random import choice
svar = "j"

while svar == "j":
    listi = ["Víkingur", "Aron", "Ásgeir", "Elvar", "Guðrún"]
    rng = choice(listi)
    print(rng, "vann milljón í happadrætti FB!")

    rest = [nafn for nafn in listi if nafn != rng]
    print("þessir unnu ekki: ", rest)
    svar = str(input("spila aftur?: "))
