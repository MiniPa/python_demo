# 与串行端口的数据通信
## 想通过串行端口独写数据，典型场景就是和y一些硬件设备打交道（如一个机器人或传感器）

# 1.通过Python内置的 I/O 模块完成这个任务
# 2.通过pySerial包完成这个任务

import serial

ser = serial.Serial('/dev/tty.usbmodem641', # Device name varies
                    baudrate=9600,
                    bytesize=8,
                    parity='N',
                    stopbits=1)




































