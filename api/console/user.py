from typing import TYPE_CHECKING, Optional

from ...models import UserData, UserResponse, CommonResponse

if TYPE_CHECKING:
    from .. import API


class User:
    def __init__(self, api: "API"):
        self._api = api

    def get(self) -> Optional[UserData]:
        """获取imouse账号信息"""
        ret = self._api._call_and_parse(UserResponse, self._api._payload.config_user_info)
        if not self._api.successful(ret):
            return None
        return ret.data

    def login(self, user_name: str, password: str, utag: int) -> Optional[UserData]:
        """登录imouse账号"""
        ret = self._api._call_and_parse(UserResponse, self._api._payload.config_user_login, user_name, password, utag)
        if not self._api.successful(ret):
            return None
        return ret.data

    def logout(self) -> bool:
        """退出imouse账号"""
        return self._api.successful(self._api._call_and_parse(CommonResponse, self._api._payload.config_user_logout))

    def switch_utag(self, utag: int) -> bool:
        """切换imouse子账号"""
        return self._api.successful(self._api._call_and_parse(CommonResponse, self._api._payload.config_user_switch, utag))
