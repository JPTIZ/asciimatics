import future.backports.email.charset as _charset
from typing import Any, Optional

Charset = _charset.Charset

def decode_header(header: Any): ...
def make_header(decoded_seq: Any, maxlinelen: Optional[Any] = ..., header_name: Optional[Any] = ..., continuation_ws: str = ...): ...

class Header:
    def __init__(self, s: Optional[Any] = ..., charset: Optional[Any] = ..., maxlinelen: Optional[Any] = ..., header_name: Optional[Any] = ..., continuation_ws: str = ..., errors: str = ...) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def append(self, s: Any, charset: Optional[Any] = ..., errors: str = ...) -> None: ...
    def encode(self, splitchars: str = ..., maxlinelen: Optional[Any] = ..., linesep: str = ...): ...

class _ValueFormatter:
    def __init__(self, headerlen: Any, maxlen: Any, continuation_ws: Any, splitchars: Any) -> None: ...
    def newline(self) -> None: ...
    def add_transition(self) -> None: ...
    def feed(self, fws: Any, string: Any, charset: Any) -> None: ...

class _Accumulator(list):
    def __init__(self, initial_size: int = ...) -> None: ...
    def push(self, fws: Any, string: Any) -> None: ...
    def pop_from(self, i: int = ...): ...
    def pop(self): ...
    def __len__(self): ...
    def reset(self, startval: Optional[Any] = ...) -> None: ...
    def is_onlyws(self): ...
    def part_count(self): ...
