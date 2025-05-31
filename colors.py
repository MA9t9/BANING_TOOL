
'''          CODE BY  𐏓꯭  𝗠𝗥ᬊ͜͡  M A LEGEND〆͎          '''

import sys
import time
import random

class Colors:
    # Text Colors (256-color mode)
    BLACK   = '\033[38;5;0m'
    RED     = '\033[38;5;196m'
    GREEN   = '\033[38;5;46m'
    YELLOW  = '\033[38;5;226m'
    BLUE    = '\033[38;5;33m'
    MAGENTA = '\033[38;5;201m'
    CYAN    = '\033[38;5;51m'
    WHITE   = '\033[38;5;15m'
    GREY    = '\033[38;5;240m'
    ORANGE  = '\033[38;5;208m'
    PURPLE  = '\033[38;5;93m'
    PINK    = '\033[38;5;205m'
    AQUA    = '\033[38;5;37m'

    # Background Colors (256-color mode)
    BG_RED     = '\033[48;5;196m'
    BG_GREEN   = '\033[48;5;46m'
    BG_YELLOW  = '\033[48;5;226m'
    BG_BLUE    = '\033[48;5;33m'
    BG_MAGENTA = '\033[48;5;201m'
    BG_CYAN    = '\033[48;5;51m'
    BG_WHITE   = '\033[48;5;15m'
    BG_GREY    = '\033[48;5;240m'

    # Text Styles
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    REVERSED  = '\033[7m'

    # Reset
    END       = '\033[0m'

    # List of all foreground colors
    COLORS = [
        BLACK, RED, GREEN, YELLOW, BLUE,
        MAGENTA, CYAN, WHITE, GREY,
        ORANGE, PURPLE, PINK, AQUA
    ]

    @staticmethod
    def random_color():
        return random.choice(Colors.COLORS)

    @staticmethod
    def typing_effect(text, color):
        for char in text:
            sys.stdout.write(color + char + Colors.END)
            sys.stdout.flush()
            time.sleep(0.01)
        print()

    @staticmethod
    def typing_effect2(text, color="", delay=0.0005):
        for char in text:
            sys.stdout.write(f"{color}{char}{Colors.END}")
            sys.stdout.flush()
            time.sleep(delay)