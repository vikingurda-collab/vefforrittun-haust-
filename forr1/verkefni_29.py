nafn=str(input("settu inn nafni: "))
listi=[]
for i in range(0, len(nafn)):
    if nafn[i]==" ":
        listi.append(i)
print(listi)
if len(listi)==1:
    print("fornafnið er: ", nafn[0:listi[0]])
    print("eftirnafnið er: ", nafn[listi[0]+1:len(nafn)])
elif len(listi)==2:
    print("fornafnið er: ", nafn[0:listi[0]])
    print("millinafnið er: ", nafn[listi[0]+1:listi[1]])
    print("eftirnafnið er: ", nafn[listi[1]+1:len(nafn)])