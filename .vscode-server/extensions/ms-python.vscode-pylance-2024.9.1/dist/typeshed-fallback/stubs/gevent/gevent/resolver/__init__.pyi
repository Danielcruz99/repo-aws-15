from collections.abc import Callable
from typing import Any, TypeVar

from gevent._types import _AddrinfoResult, _NameinfoResult, _SockAddr

_F = TypeVar("_F", bound=Callable[..., Any])

class AbstractResolver:
    HOSTNAME_ENCODING: str
    EAI_NONAME_MSG: str
    EAI_FAMILY_MSG: str
    def close(self) -> None: ...
    @staticmethod
    def fixup_gaierror(func: _F) -> _F: ...
    def gethostbyname(self, hostname: str, family: int = 2) -> str: ...
    def gethostbyname_ex(self, hostname: str, family: int = 2) -> tuple[str, list[str], list[str]]: ...
    def getaddrinfo(
        self, host: str, port: int, family: int = 0, socktype: int = 0, proto: int = 0, flags: int = 0
    ) -> _AddrinfoResult: ...
    def gethostbyaddr(self, ip_address: str) -> tuple[str, list[str], list[str]]: ...
    def getnameinfo(self, sockaddr: _SockAddr, flags: int) -> _NameinfoResult: ...
