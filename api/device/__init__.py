from typing import TYPE_CHECKING
from .image import Image
from .keyboard import KeyBoard
from .mouse import Mouse
from .shortcut import Shortcut
from .action import Action
from ...models import DeviceInfo, DeviceListResponse

if TYPE_CHECKING:
    from .. import API


class Device:
    def __init__(self, api: "API", device_id: str, device_info: DeviceInfo = None):
        self._api = api
        self._device_info = device_info
        if self._device_info:
            self.device_id = self._device_info.device_id
        else:
            self.device_id = device_id


    @property
    def mouse(self) -> Mouse:
        """
        获取鼠标控制接口。

        Returns:
            Mouse: 当前设备的鼠标控制对象，可用于执行点击、滑动等操作。
        """
        return Mouse(self)

    @property
    def keyboard(self) -> KeyBoard:
        """
        获取键盘控制接口。

        Returns:
            KeyBoard: 当前设备的键盘控制对象，可用于执行键盘输入、热键等操作。
        """
        return KeyBoard(self)

    @property
    def image(self) -> Image:
        """
        获取图像接口。

        Returns:
            Image: 当前设备的图像对象，可用于执行截图、找色、找图、ocr等操作。
        """
        return Image(self)

    @property
    def shortcut(self) -> Shortcut:
        """
        获取快捷指令接口。

        Returns:
            Shortcut: 当前设备的快捷指令对象，可用于执行快捷指令里面传输照片、剪切板共享等操作。
        """
        return Shortcut(self)

    @property
    def action(self) -> Action:
        """
        获取自定义动作接口。

        Returns:
            Action: 当前设备的自定义动作对象，可用于执行标签页切换等复合操作。
        """
        return Action(self)

    def refresh(self):
        """
        从服务器重新获取设备信息，并更新内部缓存。
        当设备状态发生变化时（如分辨率、名称等），可调用此方法同步最新信息。
        """
        ret = self._api.call(DeviceListResponse, self._api._payload.device_get, self.device_id)
        if ret.status == 200 and ret.data.code == 0 and ret.data.device_list and len(ret.data.device_list) > 0:
            self._device_info = ret.data.device_list[0]

    @property
    def info(self) -> DeviceInfo:
        """
        获取设备信息。

        Returns:
            DeviceInfo: 当前设备的信息对象（如名称、IP、分辨率等）。
            - 若首次访问，自动调用 refresh() 拉取信息。
        """
        if self._device_info is None:
            self.refresh()
        return self._device_info
