from ..api import API
from .device import Device
from .console import Console
from ..models import DeviceInfo


class Helper:
    def __init__(self, host: str):
        self._api = API(host)

    @property
    def console(self):
        return Console(self)

    
    def device(self, device_id: str, device_info: DeviceInfo = None):
        return Device(self, device_id, device_info)

    @property
    def devices(self):
        device_list_response = self._api.device_get()
        ret = []
        for data in device_list_response.data.device_list:
            ret.append(self.device('', data))
        return ret
