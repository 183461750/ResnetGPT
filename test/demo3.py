from pyminitouch import MNTDevice
from config import CustomConfig

# Connect to the device
device = MNTDevice(CustomConfig.DEVICE_ID)

# Get the device information
device_info = device.get_device_info()
print("Device Info:", device_info)

# Get the screen size
screen_size = device.get_screen_size()
print("Screen Size:", screen_size)

# Perform touch actions
device.touch_down(100, 100)
device.touch_move(200, 200)
device.touch_up()

# Perform swipe action
device.swipe(300, 300, 400, 400, duration=500)

# Perform pinch action
device.pinch(500, 500, 600, 600, duration=500)

# Perform multi-touch action
device.multi_touch_down(700, 700)
device.multi_touch_down(800, 800)
device.multi_touch_move(900, 900, 1000, 1000)
device.multi_touch_up()

# Disconnect from the device
device.disconnect()