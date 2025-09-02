from typing import TYPE_CHECKING, List

from ...models import UsbInfo, UsbListResponse, CommonResponse

if TYPE_CHECKING:
    from .. import API


class Usb:
    def __init__(self, api: "API"):
        self._api = api

    def get(self) -> List[UsbInfo]:
        """获取硬件列表"""
        ret = self._api._call_and_parse(UsbListResponse, self._api._payload.config_usb_get)
        if not self._api.successful(ret):
            return []
        return ret.data.usb_list or []

    def restart(self, vpids: str) -> bool:
        """重启硬件"""
        return self._api.successful(self._api._call_and_parse(CommonResponse, self._api._payload.device_usb_restart, vpids))
