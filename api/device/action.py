from typing import TYPE_CHECKING
from ...models import CommonResponse

if TYPE_CHECKING:
    from . import Device


class Action:
    def __init__(self, device: "Device"):
        self._device = device
        self._api = device._api
        self._device_id = device.id


    # Basic actions
    def help(self):
        self._device.keyboard.send_hid_key("TAB+H")

    # Movement actions
    def move_forward(self):
        self._device.keyboard.send_hid_key("TAB")

    def move_backward(self):
        self._device.keyboard.send_hid_key("SHIFT+TAB")

    def move_up(self):
        self._device.keyboard.send_hid_key("UpArrow")

    def move_down(self):
        self._device.keyboard.send_hid_key("DownArrow")

    def move_left(self):
        self._device.keyboard.send_hid_key("LeftArrow")

    def move_right(self):
        self._device.keyboard.send_hid_key("RightArrow")

    def move_to_beginning(self):
        self._device.keyboard.send_hid_key("TAB+LeftArrow")

    def move_to_end(self):
        self._device.keyboard.send_hid_key("TAB+RightArrow")

    def move_to_next_item(self):
        self._device.keyboard.send_hid_key("CTRL+TAB")

    def move_to_previous_item(self):
        self._device.keyboard.send_hid_key("CTRL+SHIFT+TAB")

    def find(self):
        self._device.keyboard.send_hid_key("TAB+F")

    # Interaction actions
    def activate(self):
        self._device.keyboard.send_hid_key(" ")

    def go_back(self):
        self._device.keyboard.send_hid_key("TAB+B")

    def contextual_menu(self):
        self._device.keyboard.send_hid_key("TAB+M")

    def actions(self):
        self._device.keyboard.send_hid_key("TAB+Z")

    # Device actions
    def home(self):
        self._device.keyboard.send_hid_key("FN+H")

    def app_switcher(self):
        self._device.keyboard.send_hid_key("FN+UpArrow")

    def control_center(self):
        self._device.keyboard.send_hid_key("FN+C")

    def notification_center(self):
        self._device.keyboard.send_hid_key("FN+N")

    def lock_screen(self):
        self._device.keyboard.send_hid_key("TAB+L")

    def restart(self):
        self._device.keyboard.send_hid_key("CTRL+ALT+SHIFT+WIN+R")

    def siri(self):
        self._device.keyboard.send_hid_key("FN+S")

    def accessibility_shortcut(self):
        self._device.keyboard.send_hid_key("TAB+X")

    def sos(self):
        self._device.keyboard.send_hid_key("CTRL+ALT+SHIFT+WIN+S")

    def rotate_device(self):
        self._device.keyboard.send_hid_key("TAB+R")

    def analytics(self):
        self._device.keyboard.send_hid_key("CTRL+ALT+SHIFT+WIN+.")

    def pass_through_mode(self):
        self._device.keyboard.send_hid_key("CTRL+ALT+WIN+P")

    # Gestures actions
    def keyboard_gestures(self):
        self._device.keyboard.send_hid_key("TAB+G")

    # Custom actions
    def spotlight(self):
        self._device.keyboard.send_hid_key("WIN+ ")