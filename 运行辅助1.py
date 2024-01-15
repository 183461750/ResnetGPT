import Quartz
from PIL import Image
from pyminitouch import MNTDevice

class MyMNTDevice(MNTDevice):
    def __init__(self,ID):
        MNTDevice.__init__(self,ID)

    def 发送(self,内容):
        self.connection.send(内容)

def 取图(window_name):
    window_id = None
    windows = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionOnScreenOnly | Quartz.kCGWindowListExcludeDesktopElements, Quartz.kCGNullWindowID)
    for window in windows:
        if window_name in window.get("kCGWindowName", ""):
            window_id = window["kCGWindowNumber"]
            break

    if window_id:
        window_rect = Quartz.CGRectMake(window["kCGWindowBounds"]["X"], window["kCGWindowBounds"]["Y"], window["kCGWindowBounds"]["Width"], window["kCGWindowBounds"]["Height"])
        image = Quartz.CGWindowListCreateImage(window_rect, Quartz.kCGWindowListOptionOnScreenOnly, window_id, Quartz.kCGWindowImageDefault)
        bitmap = Image.frombytes("RGB", (image.width, image.height), image.data, "raw", "BGRX", image.bytesPerRow)
        cropped_image = bitmap.crop((8,31,968,511))  # 根据需要进行裁剪
        return cropped_image

    return None