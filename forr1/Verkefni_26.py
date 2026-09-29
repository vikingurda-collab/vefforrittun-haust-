from random import randint

strnafn = str(input("Sláðu inn stráka nafn: "))
stenafn = str(input("Sláðu inn stelpu nafn: "))

print("Þau hafa", randint(1, 101), "%", "séns að vera saman")
listi = list[strnafn, stenafn]
print("Barnið þeirra heitir:", strnafn[:len(strnafn) // 2] + stenafn[len(stenafn) // 2:])