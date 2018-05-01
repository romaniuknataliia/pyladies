# Tento program rozdává naivní rady do života.

print('Odpovídej "ano" nebo "ne".')

stastna_retezec = input('Jsi šťastná? ')

if stastna_retezec == 'ano':
    stastna = True
    bohata_retezec = input('Jsi bohatá? ')
    if bohata_retezec == 'ano':
        bohata = True
        print('Gratuluji!')
    elif bohata_retezec == 'ne':
        bohata = False
        print('Zkus míň utrácet.')
    else:
        print('Nerozumím!')
elif stastna_retezec == 'ne':
    stastna = False
    bohata_retezec = input('Jsi bohatá? ')
    if bohata_retezec == 'ano':
        bohata = True
        print('Zkus se víc usmívat.')
    elif bohata_retezec == 'ne':
        bohata = False
        print('To je mi líto.')
    else:
        print('Nerozumím!')
else:
    print('Nerozumím!')

'''bohata_retezec = input('Jsi bohatá? ')
if bohata_retezec == 'ano':
    bohata = True
elif bohata_retezec == 'ne':
    bohata = False
else:
    print('Nerozumím!')

if bohata and stastna:
    # Je bohatá a zároveň štǎstná, ta se má.
    print('Gratuluji!')
elif bohata:
    # Je bohatá, ale není „bohatá a zároveň šťastná“,
    # takže musí být jen bohatá.
    print('Zkus se víc usmívat.')
elif stastna:
    # Tady musí být jen šťastná.
    print('Zkus míň utrácet.')
else:
    # A tady víme, že není ani šťastná, ani bohatá.
    print('To je mi líto.')'''
