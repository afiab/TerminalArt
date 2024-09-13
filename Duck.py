import os
import time
import sys

A="   _  "
B="__(.)<"
C="\___) "

switch = False

while True:
    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Print counter
    print(A,B,C,sep="\n");

    # update B
    B = B[:-1]+"< \"Quack!\"" if switch else B[:5]+"="
    switch = not switch
    # Flush the output buffer to ensure it is printed immediately
    sys.stdout.flush()
    
    # Wait for a second (optional)
    time.sleep(1)
