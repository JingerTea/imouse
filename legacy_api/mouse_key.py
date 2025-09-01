from abc import abstractmethod
from typing import Optional, List, Union

from ..models import CommonResponse
from ..shared.base_api import BaseAPI
from ..shared.payload import Payload
from ..types import MouseSwipeParams


class MouseKey(BaseAPI):
    def __init__(self):
        super().__init__()
        if not hasattr(self, '_payload'):
            self._payload = self._get_payload()

    @abstractmethod
    def _get_payload(self) -> Payload:
        pass

    def mouse_click(self, device_id, button: str, x, y, time: int = 0) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%BC%A0%E6%A0%87%E9%94%AE%E7%9B%98/%E9%BC%A0%E6%A0%87%E7%82%B9%E5%87%BB"""
        return self._call_and_parse(CommonResponse, self._payload.mouse_click, device_id, button, x, y, time)

    def mouse_swipe(self, device_id, params: MouseSwipeParams) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%BC%A0%E6%A0%87%E9%94%AE%E7%9B%98/%E9%BC%A0%E6%A0%87%E6%BB%91%E5%8A%A8"""
        return self._call_and_parse(CommonResponse, self._payload.mouse_swipe, device_id, params)

    def mouse_up(self, device_id, button: str) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%BC%A0%E6%A0%87%E9%94%AE%E7%9B%98/%E9%BC%A0%E6%A0%87%E5%BC%B9%E8%B5%B7"""
        return self._call_and_parse(CommonResponse, self._payload.mouse_up, device_id, button)

    def mouse_down(self, device_id, button: str) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%BC%A0%E6%A0%87%E9%94%AE%E7%9B%98/%E9%BC%A0%E6%A0%87%E6%8C%89%E4%B8%8B"""
        return self._call_and_parse(CommonResponse, self._payload.mouse_down, device_id, button)

    def mouse_move(self, device_id: str, x, y: int) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%BC%A0%E6%A0%87%E9%94%AE%E7%9B%98/%E9%BC%A0%E6%A0%87%E7%A7%BB%E5%8A%A8"""
        return self._call_and_parse(CommonResponse, self._payload.mouse_move, device_id, x, y)

    def mouse_reset(self, device_id: str) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%BC%A0%E6%A0%87%E9%94%AE%E7%9B%98/%E9%BC%A0%E6%A0%87%E5%A4%8D%E4%BD%8D"""
        return self._call_and_parse(CommonResponse, self._payload.mouse_reset, device_id)

    def mouse_wheel(self, device_id, direction: str, len, number: int) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%BC%A0%E6%A0%87%E9%94%AE%E7%9B%98/%E9%BC%A0%E6%A0%87%E6%BB%9A%E8%BD%AE"""
        return self._call_and_parse(CommonResponse, self._payload.mouse_wheel, device_id, direction, len, number)

    def key_sendkey(self, device_id, key, fn_key: str) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%BC%A0%E6%A0%87%E9%94%AE%E7%9B%98/%E9%94%AE%E7%9B%98%E8%BE%93%E5%85%A5"""
        return self._call_and_parse(CommonResponse, self._payload.key_sendkey, device_id, key, fn_key)

    def key_sendhid(self, device_id, command_list: List[str]) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%BC%A0%E6%A0%87%E9%94%AE%E7%9B%98/%E9%94%AE%E7%9B%98%E9%AB%98%E7%BA%A7%E6%93%8D%E4%BD%9C"""
        return self._call_and_parse(CommonResponse, self._payload.key_sendhid, device_id, command_list)





