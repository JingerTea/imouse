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

    def send_keys(self, keys: str) -> bool:
        """发送字符键"""
        ret = self._api._call_and_parse(CommonResponse, self._api._payload.key_sendkey,
                                       self._device_id, keys, "")
        return self._api.successful(ret)

    def send_fn_key(self, fn_key: FunctionKeys) -> bool:
        """发送功能键"""
        ret = self._api._call_and_parse(CommonResponse, self._api._payload.key_sendkey,
                                       self._device_id, "", fn_key.value)
        return self._api.successful(ret)

    def send_hid(self, command_list: List[str]) -> bool:
        """键盘高级操作"""
        ret = self._api._call_and_parse(CommonResponse, self._api._payload.key_sendhid,
                                       self._device_id, command_list)
        return self._api.successful(ret)
