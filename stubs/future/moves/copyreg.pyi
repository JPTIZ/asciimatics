from typing import Any, Optional

def pickle(ob_type: Any, pickle_function: Any, constructor_ob: Optional[Any] = ...) -> None: ...
def constructor(object: Any) -> None: ...
def add_extension(module: Any, name: Any, code: Any) -> None: ...
def remove_extension(module: Any, name: Any, code: Any) -> None: ...
def clear_extension_cache() -> None: ...
