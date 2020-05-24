################################################################################
# Developer: John Weis
# Execution Name: SwampRat.py
# Program Name: Swamp Rat
# Version Number: 0.1
# Development Date: 13 May 2020
# Latest Update: 23 May 2020
# Program Purpose: Security Tool for scanning open network ports, detecting services on those ports, and attempting to log into them with default credentials
# Git Link: None as of Latest Update
###############################################################################
# Notes:
# -Sources:
#
###############################################################################

#*IMPORT BLOCK BEGIN*(13/05/2020 -JW)
import os
import socket
import subprocess
import sys
import time
from datetime import datetime
#*IMPORT BLOCK END*(13/05/2020 -JW)

#*GLOBAL LAMBDA BLOCK BEGIN*(13/05/2020 -JW)
sleep = lambda x: time.sleep(x)
#GLOBAL LAMBDA BLOCK END*(13/05/2020 -JW)

#*FUNCTION BLOCK BEGIN*(13/05/2020 -JW)

# def foo():
#     #**VARIABLE BLOCK BEGIN**
#
#     #**VARIABLE BLOCK END**
#     pass

def logo():
        print("\n\n")
        print("""
      ██████  █     █░ ▄▄▄       ███▄ ▄███▓ ██▓███      ██▀███   ▄▄▄     ▄▄▄█████▓
    ▒██    ▒ ▓█░ █ ░█░▒████▄    ▓██▒▀█▀ ██▒▓██░  ██▒   ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒
    ░ ▓██▄   ▒█░ █ ░█ ▒██  ▀█▄  ▓██    ▓██░▓██░ ██▓▒   ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░
      ▒   ██▒░█░ █ ░█ ░██▄▄▄▄██ ▒██    ▒██ ▒██▄█▓▒ ▒   ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░
    ▒██████▒▒░░██▒██▓  ▓█   ▓██▒▒██▒   ░██▒▒██▒ ░  ░   ░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░
    ▒ ▒▓▒ ▒ ░░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒░   ░  ░▒▓▒░ ░  ░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░
    ░ ░▒  ░ ░  ▒ ░ ░    ▒   ▒▒ ░░  ░      ░░▒ ░          ░▒ ░ ▒░  ▒   ▒▒ ░   ░
    ░  ░  ░    ░   ░    ░   ▒   ░      ░   ░░            ░░   ░   ░   ▒    ░
          ░      ░          ░  ░       ░                  ░           ░  ░
                                                                                  """)
        print("""

                 __             _,-"~^"-.
               _// )      _,-"~`         `.
             ." ( /`"-,-"`                 ;
            / 6                             ;
           /           ,             ,-"     ;
          (,__.--.      \           /        ;
           //'   /`-.\   |          |        `._________
             _.-'_/`  )  )--...,,,___\     \-----------,)
           ((("~` _.-'.-'           __`-.   )         //
                 ((("`             (((---~"`         //
                                                    ((________________
                                                    `----/"/"/"/"~~~~^^^```
    """)

def clear():
    '''Function for clearing the console when running operations.  Will attempt to check if the operating system is Windows & send the proper clear command to the terminal.
    Function does not accept any arguments or return any values'''
    #**VARIABLE BLOCK BEGIN**(13/05/2020 -JW)
    sendCommand = 'clear'
    #**VARIABLE BLOCK END**(13/05/2020 -JW)

    if sys.platform == "win32":
        sendCommand = 'cls'
    try:
        os.system(sendCommand)
    except:
        pass

def main():
    #**VARIABLE BLOCK BEGIN**(13/05/2020 -JW)

    #**VARIABLE BLOCK END**(13/05/2020 -JW)
    print("Success")
#*FUNCTION BLOCK END*(13/05/2020 -JW)

if __name__ == '__main__':
    logo()
    main()
    sys.exit(0)
