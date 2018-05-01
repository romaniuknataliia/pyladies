import pyglet
import math

#cerne okno
window = pyglet.window.Window()

#vypis cas
def tik(t):
    pass #projdi dal a nic neudelej
    #had.x = had.x + t * 20  #20 je pocet pixelu o ktery se posouva obrazek za vterinu
    #had.y = 20 + 20 * math.sin(had.x / 5)
    #had.rotation = had.rotation + 10

pyglet.clock.schedule_interval(tik, 1/30)

def zpracuj_text(text):
    had.x = 300 #x je atribut had, posun x souradnice o 300
    had.y = 200

obrazek = pyglet.image.load('had.png')
obrazek2 = pyglet.image.load('had2.png')
had = pyglet.sprite.Sprite(obrazek)

def zmen(t):
    had.image = obrazek2
    pyglet.clock.schedule_once(zmen_zpatky, 0.2)

def zmen_zpatky(t):
    had.image = obrazek
    pyglet.clock.schedule_once(zmen, 0.2)

pyglet.clock.schedule_once(zmen, 1)

def klik(x, y, tlacitko, mod):
    had.x = x
    had.y = y
    print('tlacitko: ', tlacitko)
    print('mod: ', mod)

def vykresli():
    window.clear()
    had.draw()

window.push_handlers(on_text=zpracuj_text,
                     on_draw=vykresli,
                     on_mouse_press=klik,
                     )

pyglet.app.run()
print('Hotovo!')
