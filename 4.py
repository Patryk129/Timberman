import random
import time
import sys
from pynput.keyboard import Key, Listener
import os                                                  
os.system("mode 800")  

szerokosc = 3
wysokosc = 10
mapa = []
wynik = 0

def WypiszWynik():
    UstawCursor(0,4)
    print(wynik)

def ZmienWynik():
    global wynik   
    wynik += 1

def UstawCursor(x, y):
    x = str(x)
    y = str(y)
    linia = '\033['+x+';'+y+'H'
    print(linia, end="")
    sys.stdout.flush()

def GenerujMape():
    global mapa
    mapa = [[0 for x in range(szerokosc)] for y in range(wysokosc)]
    for i in range(wysokosc):
        mapa[i-1][1]=1
        if i>0:
            g = random.randint(0,2)
            if g == 0:
                pass
            elif g == 1:
                mapa[i-1][0]=2
            else:
                mapa[i-1][2]=2

def WypiszMape():
    WypiszWynik()
    for x in range(wysokosc):
        UstawCursor(x+2,0) 
        for y in range(szerokosc):
            stan = mapa[x][y]
            if stan == 0: #puste pole
                print("   ",end="")
            elif stan == 1: # pien
                print("███",end="")   
            elif stan == 2: #galaz
                print("───", end="")
            elif stan == 3: #postac lewo
                print(" ඞ┌",end="")
            elif stan == 4:  #postac prawo
                print("┐ඞ ",end="")
        print("")
    
def GenerujPostac():
    global mapa
    g = random.randint(0,1)
    if g == 0:
        mapa[wysokosc-1][0] = 3
    else:
        mapa[wysokosc-1][2] = 4 

def GenerujGore():
    global mapa
    g = random.randint(0,2)
    if g == 0:
        pass
    elif g == 1:
        mapa[0][0]=2
    else:
        mapa[0][2]=2

def Ruch():
    for i in range(wysokosc-1, -1, -1):
        #print(i)
        if i > 0:
            if mapa[i][0] == 3 or mapa[i][2] == 3:
                    pass
            else:
                mapa[i][0] = mapa[i-1][0]
                mapa[i][1] = mapa[i-1][1]
                mapa[i][2] = mapa[i-1][2]
        else:
                mapa[i][0] = 0
                mapa[i][1] = 1
                mapa[i][2] = 0
                GenerujGore()
    ZmienWynik()
def Sprawdzanie():
    if mapa[wysokosc-1][0] == 2 and mapa[wysokosc-1][2] == 3 or mapa[wysokosc-1][0] == 3 and mapa[wysokosc-1][2] == 2 or mapa[wysokosc-1][0] == 0 and mapa[wysokosc-1][2] == 3 or mapa[wysokosc-1][0] == 3 and mapa[wysokosc-1][2] == 0:
        return False
    else:
        return True

os.system('cls')
GenerujMape()
GenerujPostac()

def RuchGra():
    WypiszMape()
    Ruch()

klikniety = 0
ruchpoz = True

def kliknij(klawisz):
    global klikniety, ruchpoz, mapa
    if 'char' in dir(klawisz) and ruchpoz:
        ruchpoz = False
        klikniety = klawisz
        if klawisz.char == 'a':
            if mapa[wysokosc-1][0] == 2:
                #UstawCursor(wysokosc-1,0)
                print("przegrales!") 
            else:
                mapa[wysokosc-1][2] = 0
                mapa[wysokosc-1][0] = 3
                RuchGra()
        elif klawisz.char == 'd':
            if mapa[wysokosc-1][2] == 2:
                #UstawCursor(wysokosc-1,0)
                print("przegrales!") 
            else:
                mapa[wysokosc-1][0] = 0
                mapa[wysokosc-1][2] = 4
                RuchGra()
    if ruchpoz:
        ruchpoz = False
        klikniety = klawisz
        if klawisz == Key.left:
            if mapa[wysokosc-1][0] == 2:
                print("przegrales!") 
            else:
                mapa[wysokosc-1][2] = 0
                mapa[wysokosc-1][0] = 3
                RuchGra()
        elif klawisz == Key.right:
            if mapa[wysokosc-1][2] == 2:
                print("przegrales!") 
            else:
                mapa[wysokosc-1][0] = 0
                mapa[wysokosc-1][2] = 4
                RuchGra()

def zwolnij(klawisz):
    global klikniety, ruchpoz
    if klawisz == klikniety and not ruchpoz:
        ruchpoz = True
        klikniety = 0
    
    

with Listener(on_press=kliknij,on_release=zwolnij) as listener:
    listener.join()


# while True:
#     WypiszMape()
#     #RuchPostaci()
#     Ruch()
#     """
#     Sprawdzanie()
#     if Sprawdzanie == True:
#         print("Game over")
#         break
#     """
#     print("\n")
#     WypiszMape()
#     time.sleep(1)
    
#Do zrobienia:
# /Print w jednym miejscu
# /Poruszanie
# Sprawdzanie kolizji
# /Score
# time
# Przegrana 
# Wygląd    