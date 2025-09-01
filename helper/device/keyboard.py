from typing import TYPE_CHECKING, List
from ...types import FunctionKeys
from ...models import CommonResponse
from ...shared.base_api import BaseAPI

if TYPE_CHECKING:
    from . import Device


class KeyBoard(BaseAPI):
    def __init__(self, device: "Device"):
        super().__init__()
        self._client = device._client
        self._payload = device._payload
        self._device = device
        self._device_id = device.device_id

    def send_keys(self, keys: str) -> bool:
        """发送字符键"""
        ret = self._call_and_parse(CommonResponse, self._payload.key_sendkey,
                                       self._device_id, keys, "")
        return self._device.successful(ret)

    def send_fn_key(self, fn_key: FunctionKeys) -> bool:
        """发送功能键"""
        ret = self._call_and_parse(CommonResponse, self._payload.key_sendkey,
                                       self._device_id, "", fn_key.value)
        return self._device.successful(ret)

    def send_hid(self, command_list: List[str]) -> bool:
        """键盘高级操作"""
        ret = self._call_and_parse(CommonResponse, self._payload.key_sendhid,
                                       self._device_id, command_list)
        return self._device.successful(ret)
