import random
import time

szerokosc = 3
wysokosc = 10
mapa = []

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
        for y in range(szerokosc):
            stan = mapa[x][y]
            if stan == 0:
                print("   ",end="")
            elif stan == 1:
                print("███",end="")
            elif stan == 2:
                print("───", end="")
        print("")
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
    for i in range(wysokosc):
        if i<wysokosc:
            mapa[-i][0]=mapa[-i-1][0]
            mapa[-i][1]=mapa[-i-1][1]
            mapa[-i][2]=mapa[-i-1][2]
    GenerujGore()

GenerujMape()
while True:
    WypiszMape()
    Ruch()
    print("\n")
    WypiszMape()
    time.sleep(1)
SebuQ — 07.05.2023 17:27
a
asdsaidjgafd
SebuQ — 07.05.2023 17:56
import random
import time

szerokosc = 3
wysokosc = 10
mapa = []

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
        for y in range(szerokosc):
            stan = mapa[x][y]
            if stan == 0:
                print("   ",end="")
            elif stan == 1:
                print("███",end="")
            elif stan == 2:
                print("───", end="")
        print("")
    print("")
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
        print(i)
        if i > 0:
            mapa[i][0] = mapa[i-1][0]
            mapa[i][1] = mapa[i-1][1]
            mapa[i][2] = mapa[i-1][2]
        else:
            mapa[i][0] = 0
            mapa[i][1] = 1
            mapa[i][2] = 0
            GenerujGore()
    #GenerujGore()

GenerujMape()
while True:
    WypiszMape()
    Ruch()
    time.sleep(1)