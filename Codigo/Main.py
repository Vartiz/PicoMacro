from _typeshed import OpenTextModeUpdating
from pynput.keyboard import Key, Controller
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

