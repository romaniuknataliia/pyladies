pocet_radku = int(input('Kolik radku chces vypsat: '))
pocet_sloupcu = int(input('Kolik sloupcu chces vypsat: '))

#5 Program co vypise 4 radky a
for radek in range(pocet_radku):
    print('a')

print()
#6 vypise 5 radku: Radek 0 - Radek 4
cislo_radku = 0

for cislo_radku_ in range(pocet_radku):
    print('Radek ', cislo_radku)
    cislo_radku = cislo_radku + 1

print()
#8 cislo na druhou
cislo = 0

for cislo in range(pocet_radku):
    print(cislo, ' na druhou je ', cislo ** 2)
    cislo = cislo + 1

print()
#9 vypise maticu z X
for radek in range(pocet_radku):
    for sloupec in range(pocet_sloupcu):
        print('X', end=' ')
    print()

print()
#10 tabulka s nasobilkou
sloupec = 0
radek = 0

for radek in range(pocet_radku):
    for sloupec in range(pocet_sloupcu):
        print(radek * sloupec, end=' ')
        sloupec = sloupec + 1
    print()
    radek = radek + 1

print()
#11 pypis X piramidou
i = 1
for radek in range(pocet_radku):
    for sloupec in range(i):
        print('X', end=' ')
    print()
    i = i + 1

print()
#12 neni prvni radek
cislo_radku2 = 1

for cislo_radku2 in range(1, pocet_radku):
    if cislo_radku2 == 1:
        print('prvni radek')
        cislo_radku2 = cislo_radku2 + 1
    else:
        print('neni prvni')

print()
#13 ctverec z X
cislo_radku3 = 1
cislo_sloupce = 1

for cislo_radku3 in range(1, pocet_radku + 1):
    for cislo_sloupce in range(1, pocet_sloupcu + 1):
        if (cislo_radku3 == 1) or (cislo_radku3 == pocet_radku):
            print('X', end=' ')
            cislo_sloupce = cislo_sloupce + 1
        elif ((cislo_radku3 != 1) or (cislo_radku3 != pocet_radku)) and ((cislo_sloupce == 1) or (cislo_sloupce == pocet_sloupcu)):
            print('X', end=' ')
            cislo_sloupce = cislo_sloupce + 1
        elif ((cislo_radku3 != 1) or (cislo_radku3 != pocet_radku)) and ((cislo_sloupce != 1) or (cislo_sloupce != pocet_sloupcu)):
            print(' ', end=' ')
            cislo_sloupce = cislo_sloupce + 1
        else:
            break
    cislo_radku3 = cislo_radku3 + 1
    print()

print()
#15 co dela kod
for c in "Ahoj svete!":
    print(c)
