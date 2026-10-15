def hastafir(t):
    print(t.upper())

def lastafir(t):
    print(t.lower())
#1
texti = str(input("sláðu inn textastreng: "))
hastafir(texti)

#2
texti2 = str(input("sláðu inn textastreng: "))

svar = str(input("viltu breyta strengnum í hástafi eða lástafi?(H/L) "))
if svar == "H" or svar == "h":
    hastafir(texti2)

if svar == "L" or svar == "l":
    lastafir(texti2)

#3
texti3 = str(input("sláðu inn textastreng: "))
texti4 = str(input("sláðu inn textastreng: "))
for i in texti3:
    if i in texti4:
        print(i)