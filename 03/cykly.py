'''from math import pi, sin, cos, ceil

x = sin(1) # v radianech
print(x)

a = cos(sin(1))
print(a)

if sin(1) < 3:
    print('Je to mensi.')

print(pi)

y = 6
z = str(y)
print(type(y))   #funkce co rika typ promene

print(ceil(6.2))  #zaokruhli do 7'''

'''import math
help(math)'''

'''from random import randrange, uniform
print(randrange(1, 7))
print(uniform(1, 7))'''


from turtle import forward, right, left
from turtle import penup, pendown
from turtle import exitonclick
from turtle import shape

shape('turtle')

# 3 kvadrata pid riznym kutom
'''for _cislo in range(3):
    for _cislo in range(4):
        forward(150)
        right(90)
    left(20)'''

#sxody
'''for _ in range(5):
    forward(50)
    left(90)
    forward(50)
    right(90)'''


#punktyr
'''for delka in range(10):
    forward(1 + delka)
    penup()
    forward(10)
    pendown()'''


#left(20)

'''forward(150)
right(90)
forward(150)
right(90)
forward(150)
right(90)
forward(150)
right(90)'''

#trouhelnik
for cislo in range(3):
    forward(150)
    left(120)

exitonclick()
