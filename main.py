from scripts.utils.menu import menu1
from scripts.discord_scripts.check_tokens import check_tokens
from scripts.discord_scripts.server_options import server_options

menu1()

choose = int(input("[>] Option: "))

if choose == 1:
    check_tokens()
elif choose == 2:
    server_options()
