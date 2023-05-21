import random
import time
import keyboard
import sys
import os
os.system("mode 100")

szerokosc = 3
wysokosc = 10
mapa = []

def UstawKursor(x,y):
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
    for x in range(wysokosc): 
        UstawKursor(x,0)
        for y in range(szerokosc):
            stan = mapa[x][y]
            if stan == 0:
                print("   ",end="")
            elif stan == 1:
                print("███",end="")   
            elif stan == 2:
                print("───", end="")
            elif stan == 3:
                print("┐▄┌",end="")
        print("")

def GenerujPostac():
    global mapa
    g = random.randint(0,1)
    if g == 0:
        mapa[wysokosc-1][0] = 3
    else:
        mapa[wysokosc-1][2] = 3
#def WypiszPostac()
       
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
def RuchPostaci():
    global mapa
    while True:
        if keyboard.is_pressed("a"):
            SprawdzanieA
            mapa[wysokosc-1][0] = 3
            mapa[wysokosc-1][2] = 0 
            break
        elif keyboard.is_pressed("d"):
            SprawdzanieB
            mapa[wysokosc-1][0] = 0
            mapa[wysokosc-1][2] = 3
            break
        
def SprawdzanieA():
    if mapa[wysokosc-1][0] == 2:
        print("Game over")
def SprawdzanieB():
    if mapa[wysokosc-1][2] == 2:
        print("Game over") 
def Sprawdzanie():
    if mapa[wysokosc-1][0] == 2 and mapa[wysokosc-1][2] == 3 or mapa[wysokosc-1][0] == 3 and mapa[wysokosc-1][2] == 2 or mapa[wysokosc-1][0] == 0 and mapa[wysokosc-1][2] == 3 or mapa[wysokosc-1][0] == 3 and mapa[wysokosc-1][2] == 0:
        return False
    else:
        return True

os.system('cls')    
GenerujMape()
GenerujPostac()

while True:
    WypiszMape()
    #RuchPostaci()
    Ruch()
    """
    Sprawdzanie()
    if Sprawdzanie == True:
        print("Game over")
        break
    """
    #print("\n")
    #WypiszMape()
    time.sleep(1)
    
#Do zrobienia:
# Print w jednym miejscu
# Poruszanie
# Sprawdzanie kolizji
# Score, time
# Przegrana 
# Wygląd    
#           if mapa[i][0] == 3 or mapa[i][2] == 3:
#                    mapa[i][0] = mapa[i-1][0]
#           elif mapa[i][2] == 1:
#                   mapa[i][2] = mapa[i-1][2]
