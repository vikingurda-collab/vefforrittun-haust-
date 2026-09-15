from random import randint
svar = "j"

while svar == "j":
    tala=randint(1,4)
    if tala == 1:
        print("það verður rok og rigning á morgun")
    elif tala == 2:
        print("Það verður sól og blíða á morgun")
    elif tala == 3:
        print("Það verður þurrt en kalt á morgun")
    elif tala == 4:
        print("Það verður logn með smá skúrum á morgun")
    svar = input("aftur j/n: ").lower()