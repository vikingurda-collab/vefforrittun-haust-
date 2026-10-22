#1,1: Skrifaðu forrit sem les í gegnum allan orðalistann og prentar út hvað
#það eru mörg orð sem ekki innihalda stafinn e

#1,2: Prentið út hvað orðin eru mörg í heildina og prentið líka út hvað mörg
#orð innihalda stafinn e

#1,3: Prentið út hvað mörg prósent orða innihalda stafinn e. (prósentutölu
#án aukastafa)
akbar = 0
eword = 0
ashar = 0
fin=open("C:\\Users\\vikin\\OneDrive\\Desktop\\FB\\forr1\\v32 og v33\\words.txt")
for line in fin:
    word=line.strip()
    if "e" not in word:
        akbar+=1
    elif "e" in word:
        eword +=1
    elif "" in word:
        ashar+=1
print(akbar)
print(eword)
print(len(word))