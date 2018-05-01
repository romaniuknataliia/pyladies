# Geometricka kalkulacka
''' Geometricka kalkulacka '''

strana = int(input("Zadej stranu v cm: "))

strana_dava_smysl = strana > 0

if strana_dava_smysl:
    obvod = 4 * strana
    obsah = strana ** 2
    print('Obvod ctverce se stranou', strana, 'cm je', obvod, 'cm')
    print('Obsah ctverce se stranou', strana, 'cm je', obsah, 'cm')
else:
    print("Takova strana nedava smysl.")

print("Dekujeme za pouziti geometricke kalkulacky!")
