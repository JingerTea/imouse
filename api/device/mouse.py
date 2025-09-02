from typing import TYPE_CHECKING

from ...imouse_types import MouseSwipeParams
from ...models import CommonResponse

if TYPE_CHECKING:
    from . import Device


class Mouse:
    def __init__(self, device: "Device"):
        self._device = device
        self._api = device._api
        self._device_id = device.device_id

    def click(self, x: int, y: int, time: int = 0, button: int = 1) -> bool:
        """点击"""
        ret = self._api._call_and_parse(CommonResponse, self._api._payload.mouse_click,
                                       self._device_id, str(button), x, y, time)
        return self._api.successful(ret)

    def swipe(self, params: MouseSwipeParams) -> bool:
        """滑动"""
        ret = self._api._call_and_parse(CommonResponse, self._api._payload.mouse_swipe,
                                       self._device_id, params)
        return self._api.successful(ret)

    def down(self, button: int = 1) -> bool:
        """按下"""
        ret = self._api._call_and_parse(CommonResponse, self._api._payload.mouse_down,
                                       self._device_id, str(button))
        return self._api.successful(ret)

    def up(self, button: int = 1) -> bool:
        """弹起"""
        ret = self._api._call_and_parse(CommonResponse, self._api._payload.mouse_up,
                                       self._device_id, str(button))
        return self._api.successful(ret)

    def move(self, x: int, y: int) -> bool:
        """移动"""
        ret = self._api._call_and_parse(CommonResponse, self._api._payload.mouse_move,
                                       self._device_id, x, y)
        return self._api.successful(ret)

    def reset(self) -> bool:
        """复位"""
        ret = self._api._call_and_parse(CommonResponse, self._api._payload.mouse_reset,
                                       self._device_id)
        return self._api.successful(ret)

    def wheel(self, direction: str, len, number: int) -> bool:
        """滚轮"""
        ret = self._api._call_and_parse(CommonResponse, self._api._payload.mouse_wheel,
                                       self._device_id, direction, len, number)
        return self._api.successful(ret)
