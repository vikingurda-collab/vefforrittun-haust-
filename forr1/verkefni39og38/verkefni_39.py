nofn1 = ['Víkingur', 'Kári', 'Jón', 'Guðrún', 'Anna', 'Björn', 'Einar', 'Hrafn', 'Sigríður', 'Þórður']
nofn2 = ['Andrason', 'Björnsdóttir', 'Einarsson', 'Guðmundsdóttir', 'Jónsson', 'Káradóttir', 'Ólafsson', 'Sigurðardóttir', 'Þórðarson', 'Víkingsson']

for i in nofn1:
    for j in nofn2:
        line = (i + ' ' + j).strip()
        print(line)