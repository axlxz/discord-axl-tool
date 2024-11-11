import requests
from scripts.utils.config import config, show_hits_menu, show_hitS_line, token_type, save_file, save_hits
from scripts.utils.clear import clear
from scripts.utils.menu import logo
from scripts.utils.logs import save_log

def show_hit(success, fail, error, text, number, config1, save_hits_option):
    if config1["show_hits_menu"]:
        clear()
        logo()
        show_hits_menu(fail, success, error)
    else:
        show_hitS_line("error", error)
    if number in str(save_hits_option):
        save_file(f"./tokens/results/{text}.txt", text)

def check_tokens():
    success = 0
    fail = 0
    error = 0
    token_mode = token_type()

    config1 = config()
    save_hits_option = save_hits()

    with open("./tokens/tokens.txt", "r") as file:
        for line in file:
            line = line.strip()

            if line:
                try:
                    if token_mode == 1:
                        if line.count(":") == 2:
                            token, email, password = line.split(":")
                        else:
                            save_log(f"Incorrect line format: '{line}'. Expected 'token:email:password'.")
                            error += 1

                            show_hit(success, fail, error, "error", "3", config1, save_hits_option)

                            continue
                    elif token_mode == 2:
                        if line.count(":") == 1:
                            token, password = line.split(":")
                        else:
                            save_log(f"Incorrect line format: '{line}'. Expected 'token:password'.")
                            error += 1
                            show_hit(success, fail, error, "error", "3", config1, save_hits_option)
                            continue
                    elif token_mode == 3:
                        if ":" in line:
                            save_log(f"Incorrect line format: '{line}'. Expected only 'token'.")
                            error += 1

                            show_hit(success, fail, error, "error", "3", config1, save_hits_option)

                            continue
                        token = line

                    if token is None:
                        save_log(f"Token not found in the line: '{line}'.")
                        continue

                    response = requests.get("https://discord.com/api/v9/auth/sessions", headers={"Authorization": token})

                    if response.status_code == 200:
                        success += 1
                        if config1["show_hits_menu"]:
                            clear()
                            logo()
                            show_hits_menu(fail, success, error)
                        else:
                            show_hitS_line("success", token)
                        if "1" in str(save_hits_option):
                            save_file("./tokens/results/success.txt", line)

                    elif response.status_code == 401:
                        fail += 1
                        if config1["show_hits_menu"]:
                            clear()
                            logo()
                            show_hits_menu(fail, success, error)
                        else:
                            show_hitS_line("fail", token)
                        if "2" in str(save_hits_option):
                            save_file("./tokens/results/fail.txt", line)

                    else:
                        error += 1
                        if config1["show_hits_menu"]:
                            clear()
                            logo()
                            show_hits_menu(fail, success, error)
                        else:
                            show_hitS_line("error", token)
                        if "3" in str(save_hits_option):
                            save_file("./tokens/results/error.txt", line)

                except requests.RequestException as e:
                    error += 1
                    save_log(f"Request error for token '{line}': {e}")
                    if config1["show_hits_menu"]:
                        clear()
                        logo()
                        show_hits_menu(fail, success, error)
                    else:
                        show_hitS_line("error", token)
                    if "3" in str(save_hits_option):
                        save_file("./tokens/results/error.txt", line)

                except Exception as e:
                    error += 1
                    save_log(f"Unknown error processing line: '{line}'. Details: {e}")
                    if config1["show_hits_menu"]:
                        clear()
                        logo()
                        show_hits_menu(fail, success, error)
                    else:
                        show_hitS_line("error", token)
                    if "3" in str(save_hits_option):
                        save_file("./tokens/results/error.txt", line)
