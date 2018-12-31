# configparser 读取配置文件

from configparser import ConfigParser

print('=========1===========')
cfg = ConfigParser()
cfg.read('config.ini')
print(cfg)

sections = cfg.sections()
print(sections)


print('=========2===========')
ele1 = cfg.get('installation', 'library')
print(ele1)

ele2 = cfg.getboolean('debug', 'log_errors')
print(ele2)

ele3 = cfg.getint('server', 'nworkers')
print(ele3)

print(cfg.get('server', 'signature'))


print('=========3===========')
## 配置写回去
cfg.set('server','port','9000')
cfg.set('debug','log_errors','False')

import sys
cfg.write(sys.stdout)

## 1.下面语法等效， 名字不区分大小写
# prefix=/usr/local
# prefix: /usr/local

## 2.getBoolean() 查找任何可行的值，如下表述等价
# log_errors = true
# log_errors = TRUE
# log_errors = Yes
# log_errors = 1

## 3.配置文件作为整体被读取，变量定义可以放在随意位置
# 如案例中的%(prefix)s

## 4.ConfigParser 能一次读取多个配置，合并成一个配置
# 采用'后发置人策略'，后加载的覆盖先加载的

print('=========4===========')
print("previous configuration", cfg.get('installation', 'prefix'))
import os
# cfg.read(os.path.expanduser('~/.config.ini'))
cfg.read('myconfig.ini')
print('merged configuration', cfg.get('installation', 'prefix'))
print('merged configuration', cfg.get('installation', 'library'))
print('merged configuration', cfg.getboolean('debug', 'log_errors'))





















