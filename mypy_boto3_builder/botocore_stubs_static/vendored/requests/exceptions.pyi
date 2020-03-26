from typing import Any
from botocore.vendored.requests.packages.urllib3.exceptions import (
    HTTPError as BaseHTTPError,
)

class RequestException(IOError):
    def __init__(self, *args: Any, **kwargs: Any):
        self.response: Any
        self.request: Any

class HTTPError(RequestException): ...
class ConnectionError(RequestException): ...
class ProxyError(ConnectionError): ...
class SSLError(ConnectionError): ...
class Timeout(RequestException): ...
