from random import randrange
cislo = randrange(3)
print(cislo)


if cislo == 0:
    tah_pocitace = 'kamen'
elif cislo == 1:
    tah_pocitace = 'nuzky'
else:
    tah_pocitace = 'papir'

tah_hrace = input('Jak hrajes? ')

if (tah_pocitace == 'kamen' and tah_hrace == 'kamen') or (tah_pocitace == 'nuzky' and tah_hrace == 'nuzky') or (tah_pocitace == 'papir' and tah_hrace == 'papir') :
    print('Remize')
elif (tah_pocitace == 'kamen' and tah_hrace == 'papir') or (tah_pocitace == 'papir' and tah_hrace == 'nuzky') or (tah_pocitace == 'nuzky' and tah_hrace == 'kamen'):
    print('Vyhrala jsi!')
elif (tah_pocitace == 'kamen' and tah_hrace == 'nuzky') or (tah_pocitace == 'papir' and tah_hrace == 'kamen') or (tah_pocitace == 'nuzky' and tah_hrace == 'papir'):
    print('Prohrala jsi')
else:
    print('NEROZUMIM')

'''if tah_pocitace == 'kamen':
    if tah_hrace == 'kamen':
        print('Remize')
    elif tah_hrace == 'papir':
        print('Vyhrala jsi!')
    elif tah_hrace == 'nuzky':
        print('Prohrala jsi')
    else:
        print('NEROZUMIM')
elif tah_pocitace == 'papir':
    if tah_hrace == 'kamen':
        print('Prohrala jsi')
    elif tah_hrace == 'papir':
        print('Remize')
    elif tah_hrace == 'nuzky':
        print('Vyhrala jsi!')
    else:
        print('NEROZUMIM')
elif tah_pocitace == 'nuzky':
    if tah_hrace == 'kamen':
        print('Vyhrala jsi!')
    elif tah_hrace == 'papir':
        print('Prohrala jsi')
    elif tah_hrace == 'nuzky':
        print('Remize')
    else:
        print('NEROZUMIM')
else:
    print('NEROZUMIM')'''
