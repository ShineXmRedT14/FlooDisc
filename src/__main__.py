import argparse
import logging
import sys

from src.core.utils import ferr, pather
from src.config.cnf import version, epitext, lflag, bflag, hflag, typeindex, actionindex, obj

obj(fpath=__file__)

logging.basicConfig(
    filename=obj.path("logs/errno.log"),
    level=logging.INFO
)

def floodisc():
    try:
        from colorama import Fore

        def helptext() -> None:print(epitext, flush=True)

        parser = argparse.ArgumentParser(add_help=False, description=f"{Fore.LIGHTCYAN_EX}Netcrawl tool, {Fore.LIGHTRED_EX}Version - {Fore.LIGHTYELLOW_EX}{version}", epilog=epitext)

        for index in range(len(lflag)):
            if index in typeindex:
                parser.add_argument(lflag[index], bflag[index], help=hflag[index], type=int)
            elif index in actionindex:
                parser.add_argument(lflag[index], bflag[index], help=hflag[index], action="store_true")
            else: parser.add_argument(lflag[index], bflag[index], help=hflag[index])

        args = parser.parse_args()

        if args.source and args.destination and args.type:
            from src.core.params import PackArg
            from src.core.parser import ParseFrg

            context = PackArg()
            ParseFrg(object=args, address=context).regparse()

            if context.tcp is not None or context.udp is not None or context.icmp is not None:
                from src.core.executor import executor

                execontext = executor()

                if args.source:execontext(source=args.source)
                if args.destination:execontext(destination=args.destination)
                execontext(args=context)

                execontext.packets()
                sys.exit(0)
            else:
                print(f"{Fore.LIGHTRED_EX}Invalid Arguments\n -> -type int:<type> and -src str:<source-ip>, -dst str:<destination-ip>, -args str:<args> or without packets -http\n -> For help -h or --help{Fore.LIGHTWHITE_EX}", flush=True)
                sys.exit(0)
        elif args.http and args.url:
            from src.core.executor import executor

            execontext = executor()

            if args.timeout:execontext(timeout=int(args.timeout))
            if args.url:execontext(url=args.url)
            if args.allow:execontext(allow=True)
            if args.tasks:execontext(tasks=int(args.tasks))

            execontext.requests()
            sys.exit(0)

        elif args.help:
            helptext()
            sys.exit(0)
        else:
            print(f"{Fore.LIGHTRED_EX}Invalid Arguments\n -> -type int:<type> and -src str:<source-ip>, -dst str:<destination-ip>, -args str:<args> or without packets -http\n -> For help -h or --help{Fore.LIGHTWHITE_EX}", flush=True)
            sys.exit(0)
    except Exception as e:
        logging.error(ferr(e), exc_info=True)
        raise Exception(e)