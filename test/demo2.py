from pyminitouch import MNTDevice
from config import CustomConfig

# 创建MNTDevice对象
device = MNTDevice(CustomConfig.DEVICE_ID)

# 连接设备
device.connect()

# 模拟触摸操作
device.tap(500, 500)  # 在坐标(500, 500)处进行点击操作

# 断开设备连接
device.disconnect()