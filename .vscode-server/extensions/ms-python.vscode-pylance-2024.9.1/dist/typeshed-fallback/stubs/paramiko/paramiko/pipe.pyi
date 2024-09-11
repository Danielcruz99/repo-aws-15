from typing import Protocol

class _BasePipe(Protocol):
    def clear(self) -> None: ...
    def set(self) -> None: ...

class _Pipe(_BasePipe, Protocol):
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def set_forever(self) -> None: ...

def make_pipe() -> _Pipe: ...

class PosixPipe:
    def __init__(self) -> None: ...
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def clear(self) -> None: ...
    def set(self) -> None: ...
    def set_forever(self) -> None: ...

class WindowsPipe:
    def __init__(self) -> None: ...
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def clear(self) -> None: ...
    def set(self) -> None: ...
    def set_forever(self) -> None: ...

class OrPipe:
    def __init__(self, pipe: _Pipe) -> None: ...
    def set(self) -> None: ...
    def clear(self) -> None: ...

def make_or_pipe(pipe: _Pipe) -> tuple[OrPipe, OrPipe]: ...
