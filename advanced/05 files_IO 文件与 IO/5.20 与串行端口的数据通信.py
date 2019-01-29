# 与串行端口的数据通信
## 想通过串行端口独写数据，典型场景就是和一些硬件设备打交道（如一个机器人或传感器）

# 1.通过Python内置的 I/O 模块完成这个任务
# 2.通过pySerial包完成这个任务

import serial

ser = serial.Serial('/dev/tty.usbmodem641', # Device name varies
                    baudrate=9600,
                    bytesize=8,
                    parity='N',
                    stopbits=1)

## 设备名对于不同的设备和操作系统是不一样的，如在Windows系统上，可以使用0,1等表示的一个设备来打开通信端口"COM0","COM1"
#  端口打开后可以使用 read(), readline() 和 write() 函数读写数据了

ser.write(b'G1 X50 Y50\r\n')
resp = ser.readline()

## 推荐使用 pySerial, 它提供了对高级特性的支持(如超时、控制流、缓冲区刷新、握手协议等)
## 所有涉及到串口的I/O都是二进制模式的
## 创建二进制编码的指令或数据包的时候, struct 包也非常有用


































