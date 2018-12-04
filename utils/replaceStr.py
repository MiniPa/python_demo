# 字符串匹配和替换
import re

pat = re.compile(r'("username" : "*")')

with open(r'./in.txt', 'r+', encoding='utf8') as fin:
    # 将所有用户名字添加"-"
    with open(r'./out.txt', 'w+', encoding='utf8') as fout:
        for line in fin:
            if re.search(pat, line):
                reline = re.sub(pat, r'\1-', line)
                line = reline
                print(line)
            fout.write(line)


