import colorama
from colorama import Fore, init
import os
from scripts.utils.clear import clear

init(autoreset=True)

def logo():
    print(Fore.RED + """
        
                            ░█████╗░██╗░░██╗██╗░░░░░
                            ██╔══██╗╚██╗██╔╝██║░░░░░
                            ███████║░╚███╔╝░██║░░░░░
                            ██╔══██║░██╔██╗░██║░░░░░
                            ██║░░██║██╔╝╚██╗███████╗
                            ╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝
    """)

def menu1():
    clear()
    logo()
    print("""
            [1] Check Tokens
            [2] Join/Leave Server
    """)

    