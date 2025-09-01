from .api import API
from .helper import Helper


def api(host: str = "localhost", port: int = 9911):
    return API(host, port)


def helper(host: str = "localhost", port: int = 9911):
    return Helper(host, port)


__all__ = ["api", "helper"]
