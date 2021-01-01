from typing import Any, Optional

class Generator:
    maxheaderlen: Any = ...
    policy: Any = ...
    def __init__(self, outfp: Any, mangle_from_: bool = ..., maxheaderlen: Optional[Any] = ..., **_3to2kwargs: Any) -> None: ...
    def write(self, s: Any) -> None: ...
    def flatten(self, msg: Any, unixfrom: bool = ..., linesep: Optional[Any] = ...) -> None: ...
    def clone(self, fp: Any): ...

class BytesGenerator(Generator):
    def write(self, s: Any) -> None: ...

class DecodedGenerator(Generator):
    def __init__(self, outfp: Any, mangle_from_: bool = ..., maxheaderlen: int = ..., fmt: Optional[Any] = ...) -> None: ...
