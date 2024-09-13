import os
import time
import sys

A="   _      _      _   "
B=" >(.)__ <(.)__ =(.)__"
C="  (___/  (___/  (___/"
D="~~-~~^-~-~^~-~~-~-^~--"

A+=A
B+=B
C+=C
D+=D

def rotate1(s):
    return s[1:]+s[0]

def rotate2(s):
    return s[2:]+s[:2]

while True:
    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Print Ducks
    print(A,B,C,D,sep="\n");
    A=rotate1(A)
    B=rotate1(B)
    C=rotate1(C)
    D=rotate2(D)
    
    # Flush the output buffer to ensure it is printed immediately
    sys.stdout.flush()
    
    # Wait for a second (optional)
    time.sleep(1)
