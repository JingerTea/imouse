from .device import Device
from .console import Console
import json
from ..models import DeviceInfo, DeviceListResponse
from ..shared.client import Client
from ..shared.payload import Payload
from ..utils.utils import parse_model


class Helper:
    def __init__(self, host: str, port: int = 9911, timeout: int = 15):
        self._client = Client(host, port, timeout)
        self._payload = Payload()
        self._client.start()

    @property
    def console(self):
        return Console(self)

    
    def device(self, device_id: str, device_info: DeviceInfo = None):
        return Device(self, device_id, device_info)

    @property
    def devices(self):
        response = self._client._network_request(
            json.dumps(self._payload.device_get())
        )
        device_list_response = parse_model(DeviceListResponse, json.loads(response))
        ret = []
        for data in device_list_response.data.device_list:
            ret.append(self.device('', data))
        return ret
