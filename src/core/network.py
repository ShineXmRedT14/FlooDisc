import scapy.all as scapy
import logging
import time as tm
import asyncio

from scapy.packet import Packet
from src.core.utils import ferr
from src.core.params import PackArg, HTTPArg
from src.core.exceptions import InvalidTcpArgs, InvalidIcmpArgs, InvalidPacketType, InvalidUdpArgs, HTTPNetworkError, ReverseDnsError, HTTPCallError

"""
pfb - part from bin
pfa - part from argument
"""

from aiohttp import ClientSession

class HTTPReq:
    def __init__(self, session: ClientSession = None, args: HTTPArg = None):
        self.session = None
        self.url = None
        self.allow = False
        self.timeout = 1

        if session is not None:self.session = session
        if args is not None:
            self.url = args.url

            if args.allow is not None:self.allow = self.allow
            if args.timeout is not None:self.timeout = self.timeout

    def __call__(self, session: ClientSession | None = None, args: HTTPArg | None = None) -> None:
        try:
            if session is not None:self.session = session
            if args is not None:
                self.allow = args.allow
                self.timeout = args.timeout
                self.url = args.url

        except Exception as e:
            logging.critical(ferr(e), exc_info=True)
            raise HTTPCallError(message=e)

    async def request(self) -> dict:
        try:
            async with self.session.get(url=self.url, allow_redirects=self.allow, timeout=self.timeout) as rs:
                return {"status": rs.status, "time": round(tm.time(), 10)}
        except Exception as e:
            logging.critical(ferr(e), exc_info=True)
            raise HTTPNetworkError(message=e)

class PackRegs:
    def __init__(self, src: str, dst: str, params: PackArg):
        self.src = src
        self.dst = dst
        self.params = params
        self.obj = HTTPReq()

        try:
            import socket as ssc

            domain, _ = ssc.gethostbyaddr(self.dst)
            self.domain = domain
        except Exception as e:
            logging.error(ferr(e), exc_info=True)
            raise ReverseDnsError(message=e)

    def __call__(self) -> int:
        try:
            context = HTTPArg()
            context.url = self.domain
            context.timeout = 5
            context.allow = False

            async def handler() -> dict:
                try:
                    async with ClientSession() as session:
                        self.obj(session=session, args=context)
                        data = await self.obj.request()
                        return data
                except Exception as e:logging.warning(ferr(e))

            return asyncio.run(handler())["status"]
        except Exception as e:
            logging.critical(ferr(e), exc_info=True)
            raise HTTPNetworkError(message=e)

    def regpkt(self) -> Packet:
        try:
            ip = scapy.IP(src=self.src, dst=self.dst)
            proto = self.regproto()

            return ip/proto
        except Exception as e:logging.critical(ferr(e), exc_info=True)

    def sendpkt(self, packet: Packet, count: int) -> None:
        try:scapy.send(packet, count=count, inter=round(1/count, 10), verbose=False)
        except Exception as e:logging.critical(ferr(e), exc_info=True)

    def regproto(self) -> scapy.TCP | scapy.UDP | scapy.ICMP:
        try:
            if self.params.tonp == 1:
                return self.ctcp()
            elif self.params.tonp == 2:
                return self.cudp()
            elif self.params.tonp == 3:
                return self.cicmp()
            else:
                logging.error(ferr(InvalidPacketType().TypeText))
                raise InvalidPacketType()

        except Exception as e:logging.critical(ferr(e), exc_info=True)

    def ctcp(self) -> scapy.TCP:
        try:
            tcp_args = {}
            if self.params.tcp is not None:
                for navigate in self.params.tcp["kwargs"]:
                    pfb = self.params.tcp[navigate["bin"]]
                    pfa = self.params.tcp[navigate["arg"]]
                    tcp_args[pfb] = pfa
            else:
                logging.error(ferr(InvalidTcpArgs().TcpText))
                raise InvalidTcpArgs()

            return scapy.TCP(**tcp_args)
        except Exception as e:logging.critical(ferr(e), exc_info=True)
    def cudp(self) -> scapy.UDP:
        try:
            udp_args = {}
            if self.params.udp is not None:
                for navigate in self.params.udp["kwargs"]:
                    pfb = self.params.udp[navigate["bin"]]
                    pfa = self.params.udp[navigate["arg"]]
                    udp_args[pfb] = pfa
            else:
                logging.error(ferr(InvalidUdpArgs().UdpText))
                raise InvalidUdpArgs()

            return scapy.UDP(**udp_args)
        except Exception as e:logging.critical(ferr(e), exc_info=True)
    def cicmp(self) -> scapy.ICMP:
        try:
            icmp_args = {}
            if self.params.icmp is not None:
                for navigate in self.params.icmp["kwargs"]:
                    pfb = self.params.icmp[navigate["bin"]]
                    pfa = self.params.icmp[navigate["arg"]]
                    icmp_args[pfb] = pfa
            else:
                logging.error(ferr(InvalidIcmpArgs().IcmpText))
                raise InvalidIcmpArgs()

            return scapy.ICMP(**icmp_args)
        except Exception as e:logging.critical(ferr(e), exc_info=True)