from future.backports.urllib import response as urllib_response
from typing import Any, Optional

class URLError(IOError):
    args: Any = ...
    reason: Any = ...
    filename: Any = ...
    def __init__(self, reason: Any, filename: Optional[Any] = ...) -> None: ...

class HTTPError(URLError, urllib_response.addinfourl):
    code: Any = ...
    msg: Any = ...
    hdrs: Any = ...
    fp: Any = ...
    filename: Any = ...
    def __init__(self, url: Any, code: Any, msg: Any, hdrs: Any, fp: Any) -> None: ...
    @property
    def reason(self): ...
    def info(self): ...

class ContentTooShortError(URLError):
    content: Any = ...
    def __init__(self, message: Any, content: Any) -> None: ...