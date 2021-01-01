from collections.abc import MutableMapping
from future.utils import PY2 as PY2, PY26 as PY26, PY3 as PY3, iteritems as iteritems, itervalues as itervalues
from heapq import nlargest as nlargest
from itertools import islice as islice
from operator import itemgetter as itemgetter
from typing import Any, Optional

def ceil(x: Any): ...
def recursive_repr(fillvalue: str = ...): ...

class _Link: ...

class OrderedDict(dict):
    def __init__(*args: Any, **kwds: Any) -> None: ...
    def __setitem__(self, key: Any, value: Any, dict_setitem: Any = ..., proxy: Any = ..., Link: Any = ...) -> None: ...
    def __delitem__(self, key: Any, dict_delitem: Any = ...) -> None: ...
    def __iter__(self) -> Any: ...
    def __reversed__(self) -> None: ...
    def clear(self) -> None: ...
    def popitem(self, last: bool = ...): ...
    def move_to_end(self, key: Any, last: bool = ...) -> None: ...
    def __sizeof__(self): ...
    update: Any = ...
    keys: Any = ...
    values: Any = ...
    items: Any = ...
    __ne__: Any = ...
    def pop(self, key: Any, default: Any = ...): ...
    def setdefault(self, key: Any, default: Optional[Any] = ...): ...
    def __reduce__(self): ...
    def copy(self): ...
    @classmethod
    def fromkeys(cls, iterable: Any, value: Optional[Any] = ...): ...
    def __eq__(self, other: Any) -> Any: ...

class Counter(dict):
    def __init__(*args: Any, **kwds: Any) -> None: ...
    def __missing__(self, key: Any): ...
    def most_common(self, n: Optional[Any] = ...): ...
    def elements(self): ...
    @classmethod
    def fromkeys(cls, iterable: Any, v: Optional[Any] = ...) -> None: ...
    def update(*args: Any, **kwds: Any) -> None: ...
    def subtract(*args: Any, **kwds: Any) -> None: ...
    def copy(self): ...
    def __reduce__(self): ...
    def __delitem__(self, elem: Any) -> None: ...
    def __add__(self, other: Any): ...
    def __sub__(self, other: Any): ...
    def __or__(self, other: Any): ...
    def __and__(self, other: Any): ...
    def __pos__(self): ...
    def __neg__(self): ...
    def __iadd__(self, other: Any): ...
    def __isub__(self, other: Any): ...
    def __ior__(self, other: Any): ...
    def __iand__(self, other: Any): ...

def check_output(*popenargs: Any, **kwargs: Any): ...
def count(start: int = ..., step: int = ...) -> None: ...

class ChainMap(MutableMapping):
    maps: Any = ...
    def __init__(self, *maps: Any) -> None: ...
    def __missing__(self, key: Any) -> None: ...
    def __getitem__(self, key: Any): ...
    def get(self, key: Any, default: Optional[Any] = ...): ...
    def __len__(self): ...
    def __iter__(self) -> Any: ...
    def __contains__(self, key: Any): ...
    def __bool__(self): ...
    __nonzero__: Any = ...
    @classmethod
    def fromkeys(cls, iterable: Any, *args: Any): ...
    def copy(self): ...
    __copy__: Any = ...
    def new_child(self, m: Optional[Any] = ...): ...
    @property
    def parents(self): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __delitem__(self, key: Any) -> None: ...
    def popitem(self): ...
    def pop(self, key: Any, *args: Any): ...
    def clear(self) -> None: ...

def create_connection(address: Any, timeout: Any = ..., source_address: Optional[Any] = ...): ...
def cmp_to_key(mycmp: Any): ...