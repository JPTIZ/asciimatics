from typing import Any

class newopen:
    f: Any = ...
    enc: Any = ...
    def __init__(self, fname: Any, mode: str = ..., encoding: str = ...) -> None: ...
    def write(self, s: Any): ...
    def read(self, size: int = ...): ...
    def close(self): ...
    def __enter__(self): ...
    def __exit__(self, etype: Any, value: Any, traceback: Any) -> None: ...
