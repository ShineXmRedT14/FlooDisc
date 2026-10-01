import logging
import platform
import os
import time
import random

from src.core.utils import ferr
from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich.rule import Rule

def cls() -> None:
    try:
        if platform.system() == "Windows":
            os.system('cls')
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            os.system('clear')
    except Exception as e:logging.warning(ferr(e))

def banner() -> None:
    try:
        banr = """
███████╗██╗      ██████╗  ██████╗ ██████╗ ██╗███████╗ ██████╗
██╔════╝██║     ██╔═══██╗██╔═══██╗██╔══██╗██║██╔════╝██╔════╝
█████╗  ██║     ██║   ██║██║   ██║██║  ██║██║███████╗██║
██╔══╝  ██║     ██║   ██║██║   ██║██║  ██║██║╚════██║██║
██║     ███████╗╚██████╔╝╚██████╔╝██████╔╝██║███████║╚██████╗
╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝╚══════╝ ╚═════╝
        """

        cnsl = Console()
        text = Text(banr)
        text.stylize("bold dark_red")
        text1 = Text("[  F l o o d   D i s c o v e r y  ]")
        text1.stylize("bold bright_red")

        cnsl.print(Align.center(text))
        time.sleep(1)
        cnsl.print(Align.center(text1))
        time.sleep(random.randint(1, 3))
        cnsl.print(Rule(style="bright_red", characters="______"))
    except Exception as e:
        logging.warning(ferr(e))

def inittool() -> None:
    try:
        time.sleep(random.randint(1, 2))

        cnsl = Console()

        text1 = Text("Parse Arguments...")
        text1.stylize("bold yellow")
        text2 = Text("Initializing datas...")
        text2.stylize("bold orange3")
        text3 = Text("Completed -> start")
        text3.stylize("bold bright_red")

        cnsl.print(Align.center(text1))
        time.sleep(random.randint(2, 4))
        cnsl.print(Align.center(text2))
        time.sleep(random.randint(2, 5))
        cnsl.print(Align.center(text3))

    except Exception as e:
        logging.warning(ferr(e))