from minitouch import Minitouch

# 创建Minitouch对象
mt = Minitouch()

# 连接到设备
mt.connect()

# 模拟触摸事件
mt.tap(500, 500)  # 在坐标(500, 500)处进行点击操作

# 断开连接
mt.disconnect()