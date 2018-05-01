pocet_uhlu = int(input("Zadaj pocet uhlu: "))
strana = int(input("Zadej stranu v cm: "))


from turtle import forward, right, left
#from turtle import penup, pendown
from turtle import exitonclick
from turtle import shape

shape('turtle')

#5.domik opakovane
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
else:
    print("Takova strana nedava smysl.")

#6-9. n-uhelnik
from math import ceil
pocet_uhlu_dava_smysl = ceil(pocet_uhlu) > 0

'''if pocet_uhlu_dava_smysl and strana_dava_smysl:
    for cislo in range(ceil(pocet_uhlu)):
        forward(strana)
        left(180 - 180 * (1 - 2/ceil(pocet_uhlu)))
else:
    print("Takovy strana nedava smysl.")'''

#10.
'''if strana_dava_smysl:
    for cislo in range(51):
        left(90)
        forward(strana)
        strana = strana + 5
else:
    print("Takova strana nedava smysl.")'''

#11-12.spirala
'''if strana_dava_smysl and pocet_uhlu_dava_smysl:
    for cislo in range(100):
        left(180 - 180 * (1 - 2/ceil(pocet_uhlu)))
        forward(strana)
        strana = strana + 0.1
else:
    print("Takova strana nedava smysl.")'''



exitonclick()
