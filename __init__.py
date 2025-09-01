from .api import API
from .helper import Helper


def api(host: str = "localhost"):
    return API(host)


def helper(host: str = "localhost"):
    return Helper(host)


__all__ = ["api", "helper"]
