import time
import os

print("Valitse: Suoran piirtäminen = P, Suoran yhtälön määritys = Y")
valittu = input("")


def juttu():
    akseli = input("Mikä akseli: ")
    k = int(input("Aste kerroin: "))
    b = int(input("Vakiotermi: "))
    tarkkuus = int(input("tarkkuus: "))

    if akseli.__contains__("x"):
        print("y | x")

        for x in range (0, tarkkuus):
            l = (x * k + b)
            print(x, '|', l)
    elif akseli.__contains__("y"):
        print("x | y")

        for y in range (0, tarkkuus):
            l = (y * k + b)
            print(y, '|', l)
    else:
        print("tapahtui virhe!")

def yhmä():
    deltax = int(input("ΔX: "))
    deltay = int(input("ΔY: "))
    b = int(input("Vakiotermi: "))


    lasku = int(deltay / deltax)
    if b > 0:
        print("y =",lasku,"x","+",b)
    elif b < 0:
        print("y =",lasku,"x","+",b)
    else:
        print("y =", lasku,"x") 


numero = 1

if valittu.__contains__("p"):
    while numero == 1:
        juttu()
        time.sleep(1)
        komento = input('Paina ENTER jatkaaksesi.')
        komento = "clear"
        os.system(komento)

if valittu.__contains__("y"):
    while numero == 1:
        yhmä()
        time.sleep(1)
        komento = input('Paina ENTER jatkaaksesi.')
        komento = "clear"
        os.system(komento)