from typing import TYPE_CHECKING, List
from ...imouse_types import FunctionKeys
from ...models import CommonResponse

if TYPE_CHECKING:
    from . import Device


class KeyBoard:
    def __init__(self, device: "Device"):
        self._device = device
        self._api = device._api
        self._device_id = device.device_id

    def send_keys(self, keys: str) -> CommonResponse:
        """发送字符键"""
        return self._api.call(CommonResponse, self._api._payload.key_sendkey,
                             self._device_id, keys, "")

    def send_fn_key(self, fn_key: FunctionKeys) -> CommonResponse:
        """发送功能键"""
        return self._api.call(CommonResponse, self._api._payload.key_sendkey,
                             self._device_id, "", fn_key.value)

    def send_hid(self, command_list: List[str]) -> CommonResponse:
        """键盘高级操作"""
        return self._api.call(CommonResponse, self._api._payload.key_sendhid,
                             self._device_id, command_list)