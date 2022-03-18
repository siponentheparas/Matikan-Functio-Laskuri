import time
import os

print("Valitse: Suoran piirtäminen = P, Suoran yhtälön määritys = Y")
valittu = input("")

def jaollinen(jaettava, jakaja):
    if jaettava%jakaja == 0:
        return True
    else:
        return False

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

    if jaollinen(deltay, deltax) == True:
        if b != 0:
            print("y =",lasku,"x","+",b)
        elif b == 0:
            print("y =",lasku,"x")
    elif jaollinen(deltay, deltax) == False:
        if b != 0:
            print('  ',deltay)
            print('  ---  + ',b)
            print('  ',deltax)
        elif b == 0:
            print('  ',deltay)
            print('  ---  ')
            print('  ',deltax)

def testi():
    numero = int(input('eka'))
    toinen = int(input('toka'))
    tulos = jaollinen(numero, toinen)
    print(tulos)


numero = 1

if valittu.__contains__("p"):
    while numero == 1:
        juttu()
        time.sleep(1)
        input('Paina ENTER jatkaaksesi.')
        os.system('clear')

if valittu.__contains__("y"):
    while numero == 1:
        yhmä()
        time.sleep(1)
        input('Paina ENTER jatkaaksesi.')
        os.system('clear')
