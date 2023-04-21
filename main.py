import win32api
import win32process
import win32con
import win32gui
import ctypes
import time

# 获取游戏窗口句柄
window = win32gui.FindWindow(None, "Plants vs. Zombies 1.2.0.1073 RELEASE")

_, pid = win32process.GetWindowThreadProcessId(window)

# 打开游戏进程
phand = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, pid)
print(phand)


date = ctypes.c_long()
mydll = ctypes.windll.LoadLibrary('kernel32.dll')

# 读进程内存，找到阳光地址
base = 0x7794f8
print('基址:', hex(base))
mydll.ReadProcessMemory(int(phand), base, ctypes.byref(date), 4, None)
print('一级指针:', hex(date.value))
mydll.ReadProcessMemory(int(phand), date.value + 0x868,
                        ctypes.byref(date), 4, None)
print('二级指针:', hex(date.value))
sun_address = date.value + 0x5578
print('阳光地址:', hex(sun_address))
mydll.ReadProcessMemory(int(phand), sun_address,
                        ctypes.byref(date), 4, None)

print('阳关值:', date.value)
new_date = ctypes.c_long(1000)
mydll.WriteProcessMemory(int(phand), sun_address,
                         ctypes.byref(new_date), 4, None)
