from dataclasses import dataclass

# tonp - type of network protocol

@dataclass
class PackArg:
    tonp: int = 1
    tcp: dict | None = None
    udp: dict | None = None
    icmp: dict | None = None

@dataclass
class HTTPArg:
    url: str | None = None
    timeout: int | float = 1
    allow: bool = False

@dataclass
class SaveArg:
    source: str | None = None
    destination: str | None = None
    type: str | None = None