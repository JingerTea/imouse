from ..api import API
from ..helper import Helper


def api(host: str = "localhost"):
    return API(host)


def helper(api: API):
    return Helper(api)


__all__ = ["api", "helper"]
