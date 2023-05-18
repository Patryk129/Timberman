import random
import sys #print w jednym miejscu
from pynput.keyboard import Key, Listener #odczyt z klawiatury
import os #print w jednym miejscu + ustawienia ekranu                                              
os.system("mode 800")  
from colorama import Fore #kolorki

#Zmienne globalne
szerokosc = 3
wysokosc = 15 
mapa = []
wynik = 0
najlepszy = 0
Start = False
klikniety = 0
ruchpoz = True
kolor = Fore.WHITE


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

        
def Kolor():
    global kolor
    kolorlosuj = random.randint(1,13) 
    if kolorlosuj == 1:
        kolor = Fore.BLACK
    elif kolorlosuj == 2:
        kolor = Fore.BLUE
    elif kolorlosuj == 3:
        kolor = Fore.CYAN
    elif kolorlosuj == 4:
        kolor = Fore.GREEN
    elif kolorlosuj == 5:
        kolor = Fore.MAGENTA
    elif kolorlosuj == 6:
        kolor = Fore.RED
    elif kolorlosuj == 7:
        kolor = Fore.LIGHTBLACK_EX
    elif kolorlosuj == 8:
        kolor = Fore.LIGHTBLUE_EX
    elif kolorlosuj == 9:
        kolor = Fore.LIGHTCYAN_EX
    elif kolorlosuj == 10:
        kolor = Fore.LIGHTGREEN_EX
    elif kolorlosuj == 11:
        kolor = Fore.LIGHTMAGENTA_EX
    elif kolorlosuj == 12:
        kolor = Fore.LIGHTYELLOW_EX
    elif kolorlosuj == 13:
        kolor = Fore.YELLOW
    return kolor


def ZmienWynik():
    global wynik   
    wynik += 1


def WypiszWynik():
    kolorwynik = kolor
    if wynik >= 100:
        kolorwynik = Fore.GREEN
    elif wynik >= 200:
        kolorwynik = Fore.BLUE
    elif wynik >= 300:
        kolorwynik = Fore.CYAN
    elif wynik >= 400:
        kolorwynik = Fore.YELLOW
    elif wynik >= 500:
        kolorwynik = Fore.MAGENTA
    UstawCursor(1,100)
    print(kolorwynik + "┌", end="")
    print(kolorwynik + "─",end="")
    print(kolorwynik + "─",end="")
    print(kolorwynik + "─",end="")
    print(kolorwynik + "─",end="")
    print(kolorwynik + "─",end="")
    print(kolorwynik + "─",end="")
    print(kolorwynik + "─",end="")
    print(kolorwynik + "┐", end="")
    UstawCursor(2,100)
    print(kolorwynik + "│",end="")
    UstawCursor(2,108)
    print(kolorwynik + "│",end="")
    UstawCursor(3,100)
    print(kolorwynik + "└",end="")
    print(kolorwynik + "─", end="")
    print(kolorwynik + "─", end="")
    print(kolorwynik + "─", end="")
    print(kolorwynik + "─", end="")
    print(kolorwynik + "─", end="")
    print(kolorwynik + "─",end="")
    print(kolorwynik + "─",end="")
    print(kolorwynik + "┘",end="")
    UstawCursor(2,104) 
    print(wynik)


def WypiszMape():
    WypiszWynik()
    for x in range(wysokosc):
        UstawCursor(x+2+2,100) 
        for y in range(szerokosc):
            stan = mapa[x][y]
            if stan == 0: #puste pole
                print("   ",end="")
            elif stan == 1: # pien
                print(kolor + "███",end="")   
            elif stan == 2: #galaz
                print(kolor + "───", end="")
            elif stan == 3: #postac lewo
                print(Fore.WHITE +" ▄┌",end="")
            elif stan == 4:  #postac prawo
                print(Fore.WHITE +"┐▄ ",end="")
        print("")


def Ruch():
    for i in range(wysokosc-1, -1, -1):
        #print(i)
        if i > 0:
                mapa[i][0] = mapa[i-1][0]
                mapa[i][1] = mapa[i-1][1]
                mapa[i][2] = mapa[i-1][2]
        else:
                mapa[i][0] = 0
                mapa[i][1] = 1
                mapa[i][2] = 0
                GenerujGore()
    ZmienWynik()


def Przegrana():
    global Start
    Start = False
    xt = 10
    yt = 50
    os.system('cls') 
    RysowanieTabeli(xt,yt)
    UstawCursor(xt+1,yt+45) 
    print(kolor + "Przegrana")
    UstawCursor(xt+3,yt+3)
    print(kolor + "Wynik =",wynik)
    UstawCursor(xt+6,yt+3)
    print(kolor + "Zagraj ponownie:")
    UstawCursor(xt+7,yt+8)
    print(kolor + "SPACJA")
    UstawCursor(xt+6,yt+73)
    print(kolor + "Powrót do menu:")
    UstawCursor(xt+7,yt+78)
    print(kolor + "ENTER")
    

def RysowanieTabeli(xt,yt): 
    UstawCursor(xt,yt) 
    print(kolor + "┌", end="")
    for i in range(100):
        print(kolor + "─",end="")
    print(kolor + "┐", end="")
    for j in range(1,12):
        UstawCursor(xt+j,yt) 
        print(kolor + "│",end="")
        UstawCursor(xt+j,yt+101) 
        print(kolor + "│",end="")
    UstawCursor(xt+12,yt)
    print(kolor + "└",end="")
    for i in range(100):
        print(kolor + "─", end="")
    print(kolor + "┘",end="")


def kliknij(klawisz):
    global klikniety, ruchpoz, mapa, Start, kolor
    if 'char' in dir(klawisz) and ruchpoz and Start:
        ruchpoz = False
        klikniety = klawisz
        if klawisz.char == 'a':
            if mapa[wysokosc-1][0] == 2:
                #print("przegrales!") 
                Przegrana()
            else:
                mapa[wysokosc-1][2] = 0
                mapa[wysokosc-1][0] = 3
                RuchGra()
        elif klawisz.char == 'd':
            if mapa[wysokosc-1][2] == 2:
                #print("przegrales!") 
                Przegrana()
            else:
                mapa[wysokosc-1][0] = 0
                mapa[wysokosc-1][2] = 4 
                RuchGra()
    if ruchpoz and Start:
        ruchpoz = False
        klikniety = klawisz
        if klawisz == Key.left:
            if mapa[wysokosc-1][0] == 2:
                Przegrana()
            else:
                mapa[wysokosc-1][2] = 0
                mapa[wysokosc-1][0] = 3
                RuchGra()
        elif klawisz == Key.right:
            if mapa[wysokosc-1][2] == 2:
                Przegrana()
            else:
                mapa[wysokosc-1][0] = 0
                mapa[wysokosc-1][2] = 4
                RuchGra()
    if Start == False:
        if klawisz == Key.space:
            Gra()
            Start = True
        elif klawisz == Key.enter:
            Menu()
        elif klawisz.char == 'l':
            Kolor()
            Menu()
        elif klawisz.char == 'r':
            kolor = Fore.WHITE
            Menu()


def zwolnij(klawisz):
    global klikniety, ruchpoz
    if klawisz == klikniety and not ruchpoz:
        ruchpoz = True
        klikniety = 0


def Najlepszy(): 
    global najlepszy
    if wynik > najlepszy:
        najlepszy = wynik
    return(najlepszy)

def Napis():
    UstawCursor(1,63) 
    print(kolor + "████████╗██╗███╗░░░███╗██████╗░███████╗██████╗░███╗░░░███╗░█████╗░███╗░░██╗")
    UstawCursor(2,63) 
    print(kolor + "╚══██╔══╝██║████╗░████║██╔══██╗██╔════╝██╔══██╗████╗░████║██╔══██╗████╗░██║")
    UstawCursor(3,63) 
    print(kolor + "░░░██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝██╔████╔██║███████║██╔██╗██║")
    UstawCursor(4,63) 
    print(kolor + "░░░██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗██║╚██╔╝██║██╔══██║██║╚████║")
    UstawCursor(5,63) 
    print(kolor + "░░░██║░░░██║██║░╚═╝░██║██████╦╝███████╗██║░░██║██║░╚═╝░██║██║░░██║██║░╚███║")
    UstawCursor(6,63) 
    print(kolor + "░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝")


def Menu():
    global Start
    Start = False
    xt = 10
    yt = 50 #+102=152 50 pocz 152 kon
    os.system('cls') 
    Napis()
    RysowanieTabeli(xt,yt)
    UstawCursor(xt+1,yt+40)
    print(kolor + "Timberman w konsoli")
    UstawCursor(xt+3,yt+3)
    print(kolor + "Ostatni Wynik:",wynik)
    UstawCursor(xt+4,yt+3)
    print(kolor + "Najlepszy Wynik:",Najlepszy())
    UstawCursor(xt+6,yt+3)
    print(kolor + "Zmień kolor gry:  Wciśnij L")
    UstawCursor(xt+7,yt+3)
    print(kolor + "Kolor początkowy:  Wciśnij R")
    UstawCursor(xt+9,yt+3)
    print(kolor + "Graj:  Wciśnij SPACE")
    UstawCursor(xt+11,yt+3)
    print(kolor + "Autorzy: Patryk Polak   Sebastian Świątek")


def Gra():
    global wynik
    os.system('cls')
    wynik = 0
    GenerujMape()
    GenerujPostac()
    WypiszMape()


def RuchGra():
    WypiszMape()
    Ruch()


def main():
    os.system('cls')
    Menu()
    with Listener(on_press=kliknij,on_release=zwolnij) as listener:
        listener.join()

main()
   