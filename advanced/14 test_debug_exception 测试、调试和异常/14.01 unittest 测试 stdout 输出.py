# 测试 stdout 输出

from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import advanced.mymodule

class TestURLPrint(TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'www'
        domain = 'example.com'
        expected_url = '{}://{}.{}\n'.format(protocol, host, domain)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            advanced.mymodule.urlprint(protocol, host, domain)
            self.assertEqual(fake_out.getvalue(), expected_url)

## 使用 unittest.mock 模块的 patch() 可以很方便的在测试上下文中替换对象
#  并且当测试完成时候返回它们原有的状态

## fake_out 变量是在该进程中被创建的模拟对象
#  在 with 语句中使用它可以执行各种检查
#  StringIO 对象来代替 sys.stdout































