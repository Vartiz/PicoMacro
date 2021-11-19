from pynput import keyboard
from pynput.keyboard import Key, Controller, Listener
from machine import Pin

Teclado = Controller()

#PinOuts
Linha1 = Pin(0, Pin.IN)
Linha2 = Pin(1, Pin.IN)
Linha3 = Pin(2, Pin.IN)
Linha4 = Pin(3, Pin.IN)
Linha5 = Pin(4, Pin.IN)

Coluna1 = Pin(5, Pin.IN)
Coluna2 = Pin(6, Pin.IN)
Coluna3 = Pin(7, Pin.IN)
Coluna4 = Pin(8, Pin.IN)

NumLock = Pin(11, Pin.OUT)
CapsLock = Pin(10, Pin.OUT)
ScrollLock = Pin(9, Pin.OUT)

b0 = Pin(12, Pin.OUT)
b1 = Pin(13, Pin.OUT)
b2 = Pin(14, Pin.OUT)
b3 = Pin(15, Pin.OUT)

#detecta Locks
num = 0
caps = 0
scroll = 0

def Pressiona(key):
    global num, caps, scroll
    #detecta Caps Lock
    if key == Key.caps_lock:
        if (caps == 0):
            print("GRITO")
            caps = 1
        elif  (caps == 1):
            print("sussurro")
            caps = 0
    #detecta Num Lock
    if key == Key.num_lock:
        if (num == 0):
            print("Numerico")
            num = 1
        elif (num == 1):
            print("Alfabetico")
            num = 0
    #detecta Scroll Lock
    if key == Key.scroll_lock:
        if (scroll == 0):
            print("Roda")
            scroll = 1
        elif (scroll == 1):
            print("Quadrado")
            scroll = 0

with Teclado.Listener(on_press=Pressiona) as ouvidor:
    ouvidor.join()