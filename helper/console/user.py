from typing import TYPE_CHECKING, List, Optional

from ...models import UserData, UserResponse, CommonResponse
from ...shared.base_api import BaseAPI

if TYPE_CHECKING:
    from . import Console


class User(BaseAPI):
    def __init__(self, console: "Console"):
        super().__init__()
        self._console = console
        self._client = console._helper._client
        self._payload = console._helper._payload

    def get(self) -> Optional[UserData]:
        """获取imouse账号信息"""
        ret = self._call_and_parse(UserResponse, self._payload.config_user_info)
        if not self._console.successful(ret):
            return None
        return ret.data

    def login(self, user_name: str, password: str, utag: int) -> Optional[UserData]:
        """登录imouse账号"""
        ret = self._call_and_parse(UserResponse, self._payload.config_user_login, user_name, password, utag)
        if not self._console.successful(ret):
            return None
        return ret.data

    def logout(self) -> bool:
        """退出imouse账号"""
        return self._console.successful(self._call_and_parse(CommonResponse, self._payload.config_user_logout))

    def switch_utag(self, utag: int) -> bool:
        """切换imouse子账号"""
        return self._console.successful(self._call_and_parse(CommonResponse, self._payload.config_user_switch, utag))
