from typing import TYPE_CHECKING, List, Union
from ...imouse_types import FunctionKeys
from ...models import CommonResponse

if TYPE_CHECKING:
    from . import Device


class KeyBoard:
    def __init__(self, device: "Device"):
        self._device = device
        self._api = device._api
        self._device_id = device.id

    def send_keys(self, keys: str) -> CommonResponse:
        """发送字符键"""
        return self._api.call(CommonResponse, self._api._payload.key_sendkey,
                             self._device_id, keys, "")

    def send_fn_key(self, fn_key: Union[FunctionKeys, str]) -> CommonResponse:
        """发送功能键"""
        key_value = fn_key.value if hasattr(fn_key, 'value') else fn_key
        return self._api.call(CommonResponse, self._api._payload.key_sendkey,
                             self._device_id, "", key_value)

    def send_hid_key(self, keys: Union[str, List[str]], delay: int = 20) -> CommonResponse:
        """发送HID按键序列（自动处理修饰键）"""
        if isinstance(keys, str):
            # 自动检测修饰键并创建序列
            modifier_keys = ["ctrl", "shift", "alt", "win", "fn", "tab"]
            
            # 找到第一个（最高优先级）修饰键
            first_modifier = None
            for modifier in modifier_keys:
                if modifier + "+" in keys:
                    first_modifier = modifier
                    break
            
            if first_modifier:
                # 只按住第一个修饰键，再按组合键
                keys = [first_modifier, keys]
            else:
                keys = [keys]
        
        actions = []
        for i, key in enumerate(keys):
            actions.append({
                "delayed": 0 if i == 0 else delay,
                "key": key
            })
        
        return self._api.call(CommonResponse, self._api._payload.key_sendhidkey,
                             self._device_id, actions)

