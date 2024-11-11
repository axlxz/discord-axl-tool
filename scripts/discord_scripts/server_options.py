from scripts.utils.clear import clear
from scripts.utils.menu import logo

def joinserver():
    print("soon...")

def leaveserver():
    print("soon...")
    
def server_options():
    clear()
    logo()
    print("""
        [1] Join Server                     [2] Leave Server
""")
    
    choose = int(input("\n\n[>] Option: "))

    if choose == 1:
        joinserver()
    elif choose == 2:
        leaveserver()