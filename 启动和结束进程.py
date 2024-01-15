
import os
from config import CustomConfig

# os.system('taskkill /IM scrcpy.exe /F')
# os.system('taskkill /IM adb.exe /F')
os.system("scrcpy -s " + CustomConfig.DEVICE_ID + " --max-size 960")
