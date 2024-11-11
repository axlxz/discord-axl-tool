import json
import colorama
from colorama import Fore, init

init(autoreset=True)

def config():
    with open("config.json", "r") as r:
        data = json.load(r)
        
        return data

def show_hits_menu(fail, sucess, error):
    print(Fore.GREEN + f"                                   [>] Sucess: {sucess}")
    print(Fore.RED + f"                                   [>] Fail(s): {fail}")
    print(Fore.YELLOW + f"                                   [>] Error(s): {error}\n\n")

def show_hitS_line(var, token):
    if var == "sucess":
        print(Fore.GREEN+ f"   [VALID] {token}")
    elif var == "fail":
        print(Fore.RED + f"   [FAIL] {token}")
    elif var == "error":
        print(Fore.YELLOW + f"   [ERROR] {token}")

def token_type():
    data = config()
    if data["type_token_list"]["token_email_pass"] == True:
        return 1
    elif data["type_token_list"]["token_pass"] == True:
        return 2
    elif data["type_token_list"]["token"] == True:
        return 3

def save_hits():
    data = config()

    result = ""

    if data["save_sucess"] == True:
        result += "1"
    if data["save_fail"] == True:
        result += "2"
    if data["save_error"] == True:
        result += "3"
    
    return result

def save_file(file_name, text):
    with open(file_name, "a") as file:
        file.write(text + "\n")