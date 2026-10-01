import sys

class InvalidPacketType(Exception):
    def __init__(self, message: str = "Invalid Type Of Packet"):
        self.message = message
        super().__init__(self.message)

    @property
    def TypeText(self) -> str:return self.message

class SetTypeError(Exception):
    def __init__(self, message: str = "SetTypeError, please, set type of packet"):
        self.message = message
        super().__init__(self.message)
        sys.exit(0)

    @property
    def SetText(self) -> str:return self.message

class InvalidUdpArgs(Exception):
    def __init__(self, message: str = "Invalid Udp Kwargs"):
        self.message = message
        super().__init__(self.message)
        sys.exit(0)

    @property
    def UdpText(self) -> str:return self.message

class InvalidTcpArgs(Exception):
    def __init__(self, message: str = "Invalid Tcp Kwargs"):
        self.message = message
        super().__init__(self.message)
        sys.exit(0)

    @property
    def TcpText(self) -> str:return self.message

class InvalidIcmpArgs(Exception):
    def __init__(self, message: str = "Invalid Icmp Kwargs"):
        self.message = message
        super().__init__(self.message)
        sys.exit(0)

    @property
    def IcmpText(self) -> str:return self.message

class ExecutorInitError(Exception):
    def __init__(self, message: str = "Executor Init. Error (Critical)"):
        self.message = message
        super().__init__(self.message)
        sys.exit(0)

    @property
    def ExecutorText(self) -> str:return self.message

class ExecutorCallError(Exception):
    def __init__(self, message: str = "Exector Call. Argument Set Error (Critical)."):
        self.message = message
        super().__init__(self.message)
        sys.exit(0)

    @property
    def ExecutorText(self) -> str:return self.message

class HTTPNetworkError(Exception):
    def __init__(self, message: str = "HTTP Network. ERROR (Mid level)"):
        self.message = message
        super().__init__(self.message)
        sys.exit(0)

    @property
    def HTTPText(self) -> str:return self.message

class AsyncHandlerError(Exception):
    def __init__(self, message: str = "An Async Handler Error."):
        self.message = message
        super().__init__(self.message)
        sys.exit(0)

    @property
    def AsyncText(self) -> str:return self.message

class JsonSaveError(Exception):
    def __init__(self, message: str = "Json Save Error."):
        self.message = message
        super().__init__(self.message)
        sys.exit(0)

    @property
    def JsonText(self) -> str:return self.message

class ReverseDnsError(Exception):
    def __init__(self, message: str = "Reverse Dns Error."):
        self.message = message
        super().__init__(self.message)
        sys.exit(0)

    @property
    def DnsText(self) -> str:return self.message

class HTTPCallError(Exception):
    def __init__(self, message: str = "HTTP Call Error."):
        self.message = message
        super().__init__(self.message)
        sys.exit(0)

    @property
    def CallText(self) -> str:return self.message