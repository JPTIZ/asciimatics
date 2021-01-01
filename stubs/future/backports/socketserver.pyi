from typing import Any

class BaseServer:
    timeout: Any = ...
    server_address: Any = ...
    RequestHandlerClass: Any = ...
    def __init__(self, server_address: Any, RequestHandlerClass: Any) -> None: ...
    def server_activate(self) -> None: ...
    def serve_forever(self, poll_interval: float = ...) -> None: ...
    def shutdown(self) -> None: ...
    def service_actions(self) -> None: ...
    def handle_request(self) -> None: ...
    def handle_timeout(self) -> None: ...
    def verify_request(self, request: Any, client_address: Any): ...
    def process_request(self, request: Any, client_address: Any) -> None: ...
    def server_close(self) -> None: ...
    def finish_request(self, request: Any, client_address: Any) -> None: ...
    def shutdown_request(self, request: Any) -> None: ...
    def close_request(self, request: Any) -> None: ...
    def handle_error(self, request: Any, client_address: Any) -> None: ...

class TCPServer(BaseServer):
    address_family: Any = ...
    socket_type: Any = ...
    request_queue_size: int = ...
    allow_reuse_address: bool = ...
    socket: Any = ...
    def __init__(self, server_address: Any, RequestHandlerClass: Any, bind_and_activate: bool = ...) -> None: ...
    server_address: Any = ...
    def server_bind(self) -> None: ...
    def server_activate(self) -> None: ...
    def server_close(self) -> None: ...
    def fileno(self): ...
    def get_request(self): ...
    def shutdown_request(self, request: Any) -> None: ...
    def close_request(self, request: Any) -> None: ...

class UDPServer(TCPServer):
    allow_reuse_address: bool = ...
    socket_type: Any = ...
    max_packet_size: int = ...
    def get_request(self): ...
    def server_activate(self) -> None: ...
    def shutdown_request(self, request: Any) -> None: ...
    def close_request(self, request: Any) -> None: ...

class ForkingMixIn:
    timeout: int = ...
    active_children: Any = ...
    max_children: int = ...
    def collect_children(self) -> None: ...
    def handle_timeout(self) -> None: ...
    def service_actions(self) -> None: ...
    def process_request(self, request: Any, client_address: Any) -> None: ...

class ThreadingMixIn:
    daemon_threads: bool = ...
    def process_request_thread(self, request: Any, client_address: Any) -> None: ...
    def process_request(self, request: Any, client_address: Any) -> None: ...

class ForkingUDPServer(ForkingMixIn, UDPServer): ...
class ForkingTCPServer(ForkingMixIn, TCPServer): ...
class ThreadingUDPServer(ThreadingMixIn, UDPServer): ...
class ThreadingTCPServer(ThreadingMixIn, TCPServer): ...

class UnixStreamServer(TCPServer):
    address_family: Any = ...

class UnixDatagramServer(UDPServer):
    address_family: Any = ...

class ThreadingUnixStreamServer(ThreadingMixIn, UnixStreamServer): ...
class ThreadingUnixDatagramServer(ThreadingMixIn, UnixDatagramServer): ...

class BaseRequestHandler:
    request: Any = ...
    client_address: Any = ...
    server: Any = ...
    def __init__(self, request: Any, client_address: Any, server: Any) -> None: ...
    def setup(self) -> None: ...
    def handle(self) -> None: ...
    def finish(self) -> None: ...

class StreamRequestHandler(BaseRequestHandler):
    rbufsize: int = ...
    wbufsize: int = ...
    timeout: Any = ...
    disable_nagle_algorithm: bool = ...
    connection: Any = ...
    rfile: Any = ...
    wfile: Any = ...
    def setup(self) -> None: ...
    def finish(self) -> None: ...

class DatagramRequestHandler(BaseRequestHandler):
    rfile: Any = ...
    wfile: Any = ...
    def setup(self) -> None: ...
    def finish(self) -> None: ...