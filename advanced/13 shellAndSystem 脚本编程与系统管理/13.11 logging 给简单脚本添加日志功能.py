# 给简单脚本添加日志功能

import logging
import logging.config

def main():
    '''Configure the logging system'''
    # 硬编码
    # logging.basicConfig(
    #     filename='app.log',
    #     level=logging.ERROR,
    #     format='%(levelname)s:%(asctime)s:%(message)s'
    # )

    logging.config.fileConfig('logconfig.ini')

    # Variables (to make the calls that follow work)
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    # Example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')

if __name__ == '__main__':
    main()

## 参考 https://docs.python.org/3/howto/logging-cookbook.html



















