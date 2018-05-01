#hra - oko bere

from random import randrange

print('Odpovídej "ano" nebo "ne".')
odpoved = input('Chces hrat?')

body = 0

while odpoved == 'ano':
    nah_cislo = randrange(2, 11)
    body = body + nah_cislo
    print(body)
    if body == 21:
        print('Vyhral jsi!')
    elif odpoved == 'ne':
        print('Koncime hrat!')
        break
    else:
        print('Odpovídej "ano" nebo "ne".')
        break
