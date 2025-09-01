from typing import TYPE_CHECKING, List, Optional

from ...models import UsbInfo, UsbListResponse, CommonResponse
from ...shared.base_api import BaseAPI

if TYPE_CHECKING:
    from . import Console


class Usb(BaseAPI):
    def __init__(self, console: "Console"):
        super().__init__()
        self._console = console
        self._client = console._helper._client
        self._payload = console._helper._payload

    def get(self) -> List[UsbInfo]:
        """获取硬件列表"""
        ret = self._call_and_parse(UsbListResponse, self._payload.config_usb_get)
        if not self._console.successful(ret):
            return []
        result_list = ret.data.usb_list if ret.data and ret.data.usb_list else []
        return result_list

    def restart(self, vpids: str) -> bool:
        """重启硬件"""
        return self._console.successful(self._call_and_parse(CommonResponse, self._payload.device_usb_restart, vpids))
