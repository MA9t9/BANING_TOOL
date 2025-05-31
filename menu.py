
'''          CODE BY  𐏓꯭  𝗠𝗥ᬊ͜͡  M A LEGEND〆͎          '''

import os
import time
from banner import print_banner, print_code_by_awais
from colors import Colors
from mailer import send_whatsapp_mail
from enc import developer_info

def ban_number():
    os.system("clear")
    print_banner()
    print_code_by_awais()
    target_number = input(Colors.WHITE + Colors.BOLD + "\n   INPUT TARGET NUMBER : " + Colors.END)

    os.system("clear")
    print_banner()
    print_code_by_awais()

    options = {
        "1": "v1",
        "2": "v2",
        "3": "v3",
        "4": "v4",
        "5": "v5"
    }

    print()
    for key, val in options.items():
        Colors.typing_effect(f"     {key}. BAN NUMBER {val.upper()}", Colors.YELLOW + Colors.BOLD)

    choice = input(Colors.WHITE + Colors.BOLD + "\n   SELECT OPTION (1-5): " + Colors.END)

    if choice in options:
        send_whatsapp_mail(options[choice], target_number)
    else:
        Colors.typing_effect("\n INVALID CHOICE. RETURNING TO MAIN MENU...", Colors.RED + Colors.BOLD)
        time.sleep(2)

def main_menu():
    while True:
        os.system("clear")
        print_banner()
        print_code_by_awais()
        Colors.typing_effect("     1.  BAN NUMBER", Colors.YELLOW + Colors.BOLD)
        Colors.typing_effect("     2.  WA CHANNEL", Colors.GREEN + Colors.BOLD)
        Colors.typing_effect("     3.  YT CHANNEL", Colors.RED + Colors.BOLD)
        Colors.typing_effect("     4.  DEVELOPER ", Colors.CYAN + Colors.BOLD)
        Colors.typing_effect("     0.  EXIT", Colors.PINK + Colors.BOLD)

        choice = input(Colors.WHITE + Colors.BOLD + "\n YOUR CHOICE : " + Colors.END)

        if choice == "1":
            ban_number()
        elif choice == "2":
            os.system(f"termux-open-url https://whatsapp.com/channel/0029VbAFZQQ8KMqicghvYl1O")
        elif choice == "3":
            os.system("termux-open-url https://whatsapp.com/channel/0029VbAFZQQ8KMqicghvYl1O")
        elif choice == "4":
            developer_info()
        elif choice == "0":
            break
        else:
            Colors.typing_effect("INVALID CHOICE. TRY AGAIN.", Colors.RED + Colors.BOLD)
            time.sleep(2)

if __name__ == "__main__":
    main_menu()