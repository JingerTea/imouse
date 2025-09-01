from abc import abstractmethod
from typing import Optional, Union

from ..models import CommonResponse, UserResponse
from ..shared.base_api import BaseAPI
from ..shared.payload import Payload


class User(BaseAPI):
    def __init__(self):
        super().__init__()
        if not hasattr(self, '_payload'):
            self._payload = self._get_payload()

    @abstractmethod
    def _get_payload(self) -> Payload:
        pass

    def config_user_login(self, account_number, password: str, utag: int = 1) -> Optional[UserResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E7%94%A8%E6%88%B7%E7%9B%B8%E5%85%B3/%E7%99%BB%E5%BD%95"""
        return self._call_and_parse(UserResponse, self._payload.config_user_login, account_number, password, utag)

    def config_user_logout(self) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E7%94%A8%E6%88%B7%E7%9B%B8%E5%85%B3/%E9%80%80%E5%87%BA%E7%99%BB%E5%BD%95"""
        return self._call_and_parse(CommonResponse, self._payload.config_user_logout)

    def config_user_info(self) -> Optional[UserResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E7%94%A8%E6%88%B7%E7%9B%B8%E5%85%B3/%E8%8E%B7%E5%8F%96%E7%94%A8%E6%88%B7%E4%BF%A1%E6%81%AF"""
        return self._call_and_parse(UserResponse, self._payload.config_user_info)

    def config_user_switch(self, utag: int) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E7%94%A8%E6%88%B7%E7%9B%B8%E5%85%B3/%E5%88%87%E6%8D%A2%E5%AD%90%E8%B4%A6%E5%8F%B7"""
        return self._call_and_parse(CommonResponse, self._payload.config_user_switch, utag)
