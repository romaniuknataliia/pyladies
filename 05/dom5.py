'''#pocet_uhlu = int(input("Zadaj pocet uhlu: "))
strana = int(input("Zadej stranu v cm: "))


from turtle import forward, right, left
#from turtle import penup, pendown
from turtle import exitonclick
from turtle import shape

shape('turtle')

#2.domik se zvetsuje opakovane
strana_dava_smysl = strana > 0

if strana_dava_smysl:
    for cislo in range(3):
        for cislo in range(4):
            forward(strana)
            left(90)
        left(45)
        forward((2**(1/2))*strana)
        left(90)
        for cislo in range(2):
            forward(((2**(1/2))*strana)/2)
            left(90)
        forward((2**(1/2))*strana)
        left(45)
        forward(15)
        strana = strana + 10
else:
    print("Takova strana nedava smysl.")

exitonclick()
'''

#4. Kamen, nuzky, papir konci na slove "konec"
'''from random import randrange


def pocitac_hraje():
    cislo = randrange(3)
    #print(cislo)
    if cislo == 0:
        tah_pocitace = 'kamen'
    elif cislo == 1:
        tah_pocitace = 'nuzky'
    else:
        tah_pocitace = 'papir'
    return tah_pocitace

tah_pocitace = pocitac_hraje()
tah_hrace = input('Jak hrajes? ')

while tah_hrace != 'konec':
    if (tah_pocitace == 'kamen' and tah_hrace == 'kamen') or (tah_pocitace == 'nuzky' and tah_hrace == 'nuzky') or (tah_pocitace == 'papir' and tah_hrace == 'papir') :
        print('Remize')
        tah_pocitace = pocitac_hraje()
        tah_hrace = input('Jak hrajes dal? ')
    elif (tah_pocitace == 'kamen' and tah_hrace == 'papir') or (tah_pocitace == 'papir' and tah_hrace == 'nuzky') or (tah_pocitace == 'nuzky' and tah_hrace == 'kamen'):
        print('Vyhrala jsi!')
        tah_pocitace = pocitac_hraje()
        tah_hrace = input('Jak hrajes dal? ')
    elif (tah_pocitace == 'kamen' and tah_hrace == 'nuzky') or (tah_pocitace == 'papir' and tah_hrace == 'kamen') or (tah_pocitace == 'nuzky' and tah_hrace == 'papir'):
        print('Prohrala jsi')
        tah_pocitace = pocitac_hraje()
        tah_hrace = input('Jak hrajes dal? ')
    elif tah_hrace == 'konec':
        print('Naschledanou!')
        break
    else:
        print('NEROZUMIM! Mozne odpevedi: kamen, nuzky, papir!')
        tah_hrace = input('Jak hrajes dal? ')
'''
#5. ano_nebo_ne muze cist a i n nejen ano, ne
'''from random import randrange

print('Odpovídej "ano" nebo "ne".')
odpoved = input('Chces hrat?')

def ano_nebo_ne(odpoved):
    body = 0
    if (odpoved == 'ano') or (odpoved == 'a'):
        while body <= 21:
            nah_cislo = randrange(2, 11)
            body = body + nah_cislo
            print('Body: ', nah_cislo)
        if body == 21:
            print('Vyhral jsi!')
        else:
            print('Prohral jsi!')
    elif (odpoved == 'ne') or (odpoved == 'n'):
        print('Koncime hrat!')
    else:
        print('Odpovídej "ano" nebo "ne".')
    return body


print('Celkem bodu: ', ano_nebo_ne(odpoved))
'''

# sereda 11.4.2018

def secti(a, b):
    return a + b

def test_secti():  #dulezite je pojmenovat TEST_ protoze ten modul testovaci hleda funkce co zacinaji na TEST_
    assert secti(1, 2) == 3 #pozitivni test

def test_secti2():
    assert secti(1, 2) != 1 #negativni test
