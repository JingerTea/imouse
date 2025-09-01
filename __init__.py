from .api import API
from .legacy_api import LegacyAPI


def legacy(host: str = "localhost", port: int = 9911):
    return LegacyAPI(host, port)


def api(host: str = "localhost", port: int = 9911):
    return API(host, port)


__all__ = ["legacy", "api"]
