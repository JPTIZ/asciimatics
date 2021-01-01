from typing import Any

class BaseNewList(type):
    def __instancecheck__(cls, instance: Any): ...

class newlist(_builtin_list, metaclass=BaseNewList):
    def copy(self): ...
    def clear(self) -> None: ...
    def __new__(cls, *args: Any, **kwargs: Any): ...
    def __add__(self, value: Any): ...
    def __radd__(self, left: Any): ...
    def __getitem__(self, y: Any): ...
    def __native__(self): ...
    def __nonzero__(self): ...
