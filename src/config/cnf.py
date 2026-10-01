from colorama import Fore, init
from src.core.utils import pather

init(autoreset=True)
obj = pather()

version = "1.0"
epitext = f"""
{Fore.LIGHTRED_EX}-h / {Fore.LIGHTYELLOW_EX}--help / {Fore.LIGHTGREEN_EX}Get commands/help
{Fore.LIGHTRED_EX}-src / {Fore.LIGHTYELLOW_EX}--source / {Fore.LIGHTGREEN_EX}Source IP
{Fore.LIGHTRED_EX}-dst / {Fore.LIGHTYELLOW_EX}--destination / {Fore.LIGHTGREEN_EX}Destination IP
{Fore.LIGHTRED_EX}-type / {Fore.LIGHTYELLOW_EX}--type / {Fore.LIGHTGREEN_EX}type of the packet: 1 - tcp, 2 - udp, 3 - icmp
{Fore.LIGHTRED_EX}-args / {Fore.LIGHTYELLOW_EX}--args / {Fore.LIGHTGREEN_EX}protocol params: like src port, dst port, syntax in the README.md
{Fore.LIGHTRED_EX}-http / {Fore.LIGHTYELLOW_EX}--http / {Fore.LIGHTGREEN_EX}HTTP/flood test
{Fore.LIGHTRED_EX}-time / {Fore.LIGHTYELLOW_EX}--timeout / {Fore.LIGHTGREEN_EX}Timeout for HTTP requests
{Fore.LIGHTRED_EX}-allow / {Fore.LIGHTYELLOW_EX}--allow / {Fore.LIGHTGREEN_EX}Allow redirects for HTTP requests
{Fore.LIGHTRED_EX}-u / {Fore.LIGHTYELLOW_EX}--url / {Fore.LIGHTGREEN_EX}Set URL for HTTP requests
{Fore.LIGHTRED_EX}-t / {Fore.LIGHTYELLOW_EX}--tasks / {Fore.LIGHTGREEN_EX}Set max parallel Tasks
{Fore.LIGHTWHITE_EX}
"""

lflag = ["-h", "-src", "-dst", "-type", "-args", "-http", "-time", "-allow", "-u", "-t"]
bflag = ["--help", "--source", "--destination", "--type", "--args", "--http", "--timeout", "--allow", "--url", "--tasks"]
hflag = ["Get commands/help", "Source IP", "Destination IP", "type of the packet: 1 - tcp, 2 - udp, 3 - icmp", "protocol params: like src port, dst port, syntax in the README.md", "HTTP/flood test", "Timeout for HTTP requests", "Allow redirects for HTTP requests", "Set URL for HTTP requests", "Parallel Tasks"]

typeindex = [3, 6, 9]
actionindex = [0, 5, 7]