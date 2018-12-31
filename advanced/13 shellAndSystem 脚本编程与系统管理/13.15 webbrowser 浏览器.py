# 通过脚本启动打开指定的网页

import webbrowser

# 使用默认浏览器打开网页
webbrowser.open('http://www.python.org')
webbrowser.open_new_tab('http://www.python.org')

c = webbrowser.get('firefox')
c.open('http://www.python.org')
c.open_new_tab('http://docs.python.org')

## 非常实用哦


