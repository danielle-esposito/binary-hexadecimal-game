import random

def hexgame():
    score = 0
    while True:
        x = int(random.randint(0,255))
        print(x)
        hexval = hex(x)
        print(hexval)
        userhex = input("pwease input hexadecimal number of the decimal value: ")
        if userhex == hexval:
            print("good job gaymers")
            score = score + 1
            print ("score:", score)
        else:
            print("go fuck yourself")
            score = score - 1
            print("score:", score)
def binarygame():
    score = 0
    while True:
        x = int(random.randint(0,255))
        print(x)
        binary = input("pwease input binary number of the decimal value: ")
        decimal = int(binary,2)
        if decimal == x:
            print("good job gaymers")
            score = score + 1
            print ("score:", score)
        else:
            print("go fuck yourself")
            score = score - 1
            print("score:", score)

gamemode = input("""
please select a game
1 = binary
2 = hexadecimal
please enter number: 
""")
if gamemode == "1":
    binarygame()
if gamemode == "2":
    hexgame()