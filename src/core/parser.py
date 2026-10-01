import logging
import argparse

from src.core.utils import ferr
from src.core.params import PackArg
from src.core.exceptions import InvalidPacketType, SetTypeError

# address - pointer for the flooarg class address in python memory

class ParseFrg:
    def __init__(self, object: argparse.Namespace, address: PackArg):
        self.object = object
        self.address = address

    def regparse(self) -> None:
        try:
            pktype = self.object.type

            if not pktype:
                logging.error(ferr(SetTypeError().SetText))
                raise SetTypeError()

            try:pktype = int(pktype)
            except:
                logging.error(ferr(InvalidPacketType().TypeText))
                raise InvalidPacketType()

            if pktype == 1:self.ptcp()
            elif pktype == 2:self.pudp()
            elif pktype == 3:self.picmp()
            else:
                logging.error(ferr(InvalidPacketType().TypeText))
                raise InvalidPacketType()

            self.address.tonp = pktype

        except Exception as e:logging.critical(ferr(e), exc_info=True)

    def ptcp(self) -> None:
        try:
            if self.object.args:
                arguments = self.object.args.split(";")

                if arguments:
                    setflg = False

                    for item in arguments:
                        if not setflg:
                            self.address.tcp = {}
                            self.address.tcp["kwargs"] = []
                            setflg = True

                        splited = item.split("*")

                        if splited and len(splited) == 2:
                            flag = splited[0]
                            arg = splited[1]

                            match flag:
                                case "sport":
                                    dataoff = {"bin": "sport", "arg": int(arg)}
                                    self.address.tcp["kwargs"].append(dataoff)
                                case "dport":
                                    dataoff = {"bin": "dport", "arg": int(arg)}
                                    self.address.tcp["kwargs"].append(dataoff)
                                case "flags":
                                    dataoff = {"bin": "flags", "arg": arg}
                                    self.address.tcp["kwargs"].append(dataoff)
        except Exception as e:
            logging.critical(ferr(e), exc_info=True)
            raise Exception(ferr(e))

    def pudp(self) -> None:
        try:
            if self.object.args:
                arguments = self.object.args.split(";")

                if arguments:
                    setflg = False

                    for item in arguments:
                        if not setflg:
                            self.address.udp = {}
                            self.address.udp["kwargs"] = []
                            setflg = True

                        splited = item.split("*")

                        if splited and len(splited) == 2:
                            flag = splited[0]
                            arg = splited[1]

                            match flag:
                                case "sport":
                                    dataoff = {"bin": "sport", "arg": int(arg)}
                                    self.address.udp["kwargs"].append(dataoff)
                                case "dport":
                                    dataoff = {"bin": "dport", "arg": int(arg)}
                                    self.address.udp["kwargs"].append(dataoff)
        except Exception as e:
            logging.critical(ferr(e), exc_info=True)
            raise Exception(ferr(e))
    def picmp(self) -> None:
        try:
            if self.object.args:
                arguments = self.object.args.split(";")

                if arguments:
                    setflg = False

                    for item in arguments:
                        if not setflg:
                            self.address.icmp = {}
                            self.address.icmp["kwargs"] = []
                            setflg = True

                        splited = item.split("*")

                        if splited and len(splited) == 2:
                            flag = splited[0]
                            arg = splited[1]

                            match flag:
                                case "type":
                                    dataoff = {"bin": "type", "arg": int(arg)}
                                    self.address.icmp["kwargs"].append(dataoff)
                                case "code":
                                    dataoff = {"bin": "code", "arg": int(arg)}
                                    self.address.icmp["kwargs"].append(dataoff)
        except Exception as e:
            logging.critical(ferr(e), exc_info=True)
            raise Exception(ferr(e))