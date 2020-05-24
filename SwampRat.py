################################################################################
# Developer: John Weis
# Execution Name: SwampRat.py
# Program Name: Swamp Rat
# Version Number: 0.1
# Development Date: 13 May 2020
# Latest Update: 23 May 2020
# Program Purpose: Security Tool for scanning open network ports, detecting services running on those ports, determine if services are vulnerable to known CVEs, attempting to log into them with default credentials
# Current Branch Name: 00001-feature-tcp-port-scanner
# Initial Branch Name: 00001-feature-tcp-port-scanner
# Git Link: https://github.com/weisje/SwampRat.git
################################################################################

#*IMPORT BLOCK BEGIN*(23/05/2020 -JW)
from datetime import datetime
import os
from queue import Queue
import socket
#import subprocess
import sys
import threading
import time
#*IMPORT BLOCK END*(23/05/2020 -JW)

#*GLOBAL LAMBDA BLOCK BEGIN*(13/05/2020 -JW)
sleep = lambda x: time.sleep(x)
#GLOBAL LAMBDA BLOCK END*(13/05/2020 -JW)

#*CLASS BLOCK BEGIN*(23/05/2020 -JW)

#*CLASS BLOCK END*(23/05/2020 -JW)

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

###############################################################################
# Notes:
#
# -Version Goals:
#   0.1 - Successfully scan for open TCP/UDP Ports across a range of IP Addresses and report the results
#
# -Sources:
#
###############################################################################
