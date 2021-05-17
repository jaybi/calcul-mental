#!/bin/python3

import random 
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

durations = []
true = 0
false = 0 

while(1):
    
    start = time.time()
    a = random.randint(9,99)
    b = random.randint(2,9)
    answer = int(input(repr(a) + " x " + repr(b) + " = ?"))
    end = time.time()
    durations.append(f"{(end-start):.2f}")
    if (answer==a*b):
        print(bcolors.OKGREEN + "OK!"+ bcolors.ENDC)
        true = true + 1
    else:
        print(bcolors.FAIL + "Faux: " + repr(a*b)+ bcolors.ENDC)
        false = false + 1 
    sum = 0.0
    for n in durations:
        sum = sum + float(n)
    print("Durée = " + f"{(end-start):.2f} Moy : " + f"{sum / len(durations):.2f}" + " | " + str(true) + " sur " + str(false+true) + "\n")

