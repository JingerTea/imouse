from typing import TYPE_CHECKING, List, Optional

from ...models import GroupInfo, GroupListResponse, IdListResponse
from ...shared.base_api import BaseAPI

if TYPE_CHECKING:
    from . import Console


class Group(BaseAPI):
    def __init__(self, console: "Console"):
        super().__init__()
        self._console = console
        self._client = console._helper._client
        self._payload = console._helper._payload

    def get(self, gids: str = "") -> List[GroupInfo]:
        """获取分组"""
        ret = self._call_and_parse(GroupListResponse, self._payload.device_group_get, gids)
        if not self._console.successful(ret):
            return []
        result_list = ret.data.group_list if ret.data and ret.data.group_list else []
        return result_list


    def set(self, gid: str, name: str) -> Optional[GroupInfo]:
        """设置分组"""
        ret = self._call_and_parse(GroupListResponse, self._payload.device_group_set, gid, name)
        if self._console.successful(ret):
            if len(ret.data.group_list) == 0:
                return None
            return ret.data.group_list[0]
        return None

    def add(self, name: str) -> Optional[GroupInfo]:
        """新增分组"""
        return self.set("0", name)

    def delete(self, gids: str) -> Optional[List[str]]:
        """删除分组"""
        ret = self._call_and_parse(IdListResponse, self._payload.device_group_del, gids)
        if not self._console.successful(ret):
            return []
        result_list = ret.data.id_list if ret.data and ret.data.id_list else []
        return result_list
