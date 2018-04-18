# Mitmesugused katsetused

import math
from sys import argv

a = b = c = 0.
from_commandline = len(argv) > 3
if from_commandline:
    try:
        a = float(argv[1])
        b = float(argv[2])
        c = float(argv[3])
    except ValueError as erind:
        print("Arusaamatu sisend k2sureal: " + str(erind) + " " + str(argv))
if not from_commandline:   
    while True:
        try:
            a = float(input("Sisesta a: "))  # raw_input Python2 jaoks
            if abs(a) <= 0.0000001:   # a == 0
                print("Ruutliikme kordaja ei saa olla null!")
                continue
            b = float(input("Sisesta b: "))
            c = float(input("Sisesta c: "))
            break
        except ValueError as erind:
            print("Arusaamatu sisend: " + str(erind) + " Alustame algusest!")
print("a = " + str(a))
print("b = " + str(b))
print("c = " + str(c))
d = b*b - 4.*a*c
if d < 0:
    raise ArithmeticError("Reaallahendid puuduvad! Diskriminant: " + str(d))
x1 = (-b + math.sqrt(d))/(2.*a)
x2 = (-b - math.sqrt(d))/(2.*a)
print("x1 = " + str(x1))
print("x2 = " + str(x2))
