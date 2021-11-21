from pynput import keyboard, mouse
from pynput.keyboard import Key, Controller, Listener
from machine import Pin
import _thread
from pynput.mouse import Button, Controller

Teclado = keyboard.Controller()
Rato = mouse.Controller()

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

#variaveis
Camada = 0

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

#Leitura das Linhas e Colunas
if Linha1 == 1:
    if Coluna1 == 1: Teclado.press(Key.num_lock) # toggle Num Lock
#Troca de Camadas
    elif Coluna2 == 1: Camada + 1
    elif Coluna3 == 1: Camada - 1
    elif Coluna4 == 1:
        if num == 1: Teclado.press('/')
        elif num == 0:
            #if Camada == 0: Teclado.press(Key.media_play_pause)
            #if Camada == 1: Teclado.press(Key.media_play_pause)
            if Camada == 2:
                Key.tap('/')
                Key.tap('/')

if Linha2 == 1:
    if Coluna1 == 1:
        if num == 1: Teclado.press(' 7')
        elif num == 0:
            if Camada == 0: Teclado.press(Key.home)
            elif Camada == 1: Teclado.press(Key.media_volume_mute)
            elif Camada == 2: Teclado.press('(')
    elif Coluna2 == 1:
        if num == 1: Teclado.press('8')
        elif num == 0:
            if Camada == 0: Teclado.press(Key.up)
            elif Camada == 1: Teclado.press(Key.media_volume_up)
            elif Camada == 2: Teclado.press(')')
    elif Coluna3 == 1:
        if num == 1: Teclado.press(' 9')
        elif num == 0:
            if Camada == 0: Teclado.press(Key.page_up)
            elif Camada == 1: Teclado.press(Key.media_volume_down)
            elif Camada == 2: Teclado.press('<')
    elif Coluna4 == 1:
        if num == 1: Teclado.press('*')
        elif num == 0:
            if Camada == 0: Teclado.press(Key.media_play_pause)
            elif Camada == 1: Teclado.press(Key.media_play_pause)
            elif Camada == 2: Teclado.press('>')

if Linha3 == 1:
    if Coluna1 == 1:
        if num == 1: Teclado.press (' 4')
        elif num == 0:
            if Camada == 0: Teclado.press(Key.left)
            elif Camada == 1: Teclado.press(Key.f20)
            elif Camada == 2: Teclado.press('{')
    elif Coluna2 == 1:
        if num == 1: Teclado.press('5')
        elif num == 0:
            if Camada == 0: Rato.click(Button.left, 1)
            elif Camada == 1: Teclado.press(Key.media_previous)
            elif Camada == 2: Teclado.press('}')
    elif Coluna3 == 1:
        if num == 1: Teclado.press('6')
        elif num == 0:
            if Camada == 0: Teclado.press(Key.right)
            elif Camada == 1: Teclado.press(Key.media_next)
            elif Camada == 2: Teclado.press('"')
    elif Coluna4 == 1:
        if num == 1: Teclado.press('-')
        elif num == 0:
            #if Camada == 0: achar algo
            #if Camada == 1: achar algo
            if Camada == 2: Teclado.press("'")

if Linha4 == 1:
    if Coluna1 == 1:
        if num == 1: Teclado.press('1')
        elif num == 0:
            if Camada == 0: Teclado.press(Key.end)
            elif Camada == 1: Teclado.press(Key.f17)
            elif Camada == 2: Teclado.press('[')
    if Coluna2 == 1:
        if num == 1: Teclado.press('2')
        elif num == 0:
            if Camada == 0: Teclado.press(Key.down)
            elif Camada == 1: Teclado.press(Key.f16)
            elif Camada == 2: Teclado.press(']')
    if Coluna3 == 1:
        if num == 1: Teclado.press('3')
        elif num == 0:
            if Camada == 0: Teclado.press(Key.page_down)
            elif Camada == 1: Teclado.press(Key.f19)
            elif Camada == 2: Teclado.press('%')
    if Coluna4 == 1:
        if num == 1: Teclado.press('3')
        elif num == 0:
            #if Camada == 0: achar algo
            if Camada == 1: Teclado.press(Key.f20)
            elif Camada == 2: Teclado.press('#')

if Linha5 == 1:
    if Coluna1 == 1:
        if num == 1: Teclado.press('0')
        elif num == 0:
            if Camada == 0: Teclado.press(Key.insert)
            elif Camada == 1: Teclado.press(Key.f13)
            elif Camada == 2: Teclado.press(Key.tab)
    if Coluna2 == 1:
        if num == 1: Teclado.press(',')
        elif num == 0:
            #if Camada == 0: achar algo
            if Camada == 1: Teclado.press(Key.f14)
            elif Camada == 2: Teclado.press(',')
    if Coluna3 == 1:
        if num == 1: Teclado.press('.')
        elif num == 0:
            if Camada == 0: Teclado.press(Key.delete)
            elif Camada == 1: Teclado.press(Key.f15)
            elif Camada == 2: Teclado.press('.')
    if Coluna4 == 1:
        if num == 1: Teclado.press(Key.enter)
        elif num == 0:
            if Camada == 0: Teclado.press(Key.enter)
            elif Camada == 1: Teclado.press(Key.f16)
            elif Camada == 2: Teclado.press(Key.enter)