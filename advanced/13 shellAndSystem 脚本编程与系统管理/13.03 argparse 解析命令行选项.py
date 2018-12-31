# 解析命令行选项
## argparse中
## dest 指定解析结果被指派给属性的名字
## metavar 用来生成帮助信息
## action 指定跟属性对应的处理逻辑，通常值为verbose


# search.py
'''
Hypothetical command-line tool for searching a collection of
files for one or more text patterns.
'''
import argparse
parser = argparse.ArgumentParser(description='Search some files')
parser.add_argument(dest='filenames', metavar='filename', nargs='*')
parser.add_argument('-p', '--pat', metavar='pattern', required=True, dest='patterns', action='append',
                    help='text pattern for search for')

parser.add_argument('-v', dest='verbose', action='store_true', help='verbose mode')
parser.add_argument('-o', dest='outfile', action='store_true', help='output file')
parser.add_argument('--speed', dest='outfile', action='store', help='output file')
parser.add_argument('--speed', dest='speed', action='store',choices={'slow', 'fast'}, default='slow', help='search speed')

args = parser.parse_args()

# Output the collected arguments
# print(args.filenames)
# print(args.patterns)
# print(args.verbose)
# print(args.outfile)
# print(args.speed)

# 如上该程序定义了一个如下使用的命令行解析器
# bash % python3 search.py -h
# usage: search.py [-h] [-p pattern] [-v] [-o OUTFILE] [--speed {slow,fast}] [filename [filename ...]]

# Search some files

# positional arguments: filename
# optional arguments: -h, --help show this help message and exit -p pattern, --pat pattern text pattern to search for
# -v verbose mode -o OUTFILE output file --speed {slow,fast} search speed

## 使用案例
# bash % python3 search.py -v -p spam --pat=eggs foo.txt bar.txt -o results \ --speed=fast
# filenames = ['foo.txt', 'bar.txt']
# patterns = ['spam', 'eggs']
# verbose = True
# outfile = results
# speed = fast


## action='xxx' 指定参数对应的处理逻辑
# 01 根据参数是否存在设定一个Boolean标志
parser.add_argument('-v', dest='verbose', action='store_true', help='verbose mode')
# 02 接受一个单独值并将其存储为一个字符串
parser.add_argument('-o', dest='outfile', action='store', help='output file')
# 03 允许某参数出现多次，并将其追加到一个列表中，required标志该参数至少要有一个 -p 和 --pat 表示两个参数名形式都可以
parser.add_argument('-p', '--pat',metavar='pattern', required=True, dest='patterns', action='append',
                    help='text pattern to search for')
# 04 下面参数说明接受一个值，但会将其和可能的选择值做比较，检测合法性
parser.add_argument('--speed', dest='speed', action='store', choices={'slow','fast'}, default='slow', help='search speed')

## parser.parse() 会处理sys.argv的值并返回一个结果实例，该参数值会被设置成该实例中 add_argument() 方法的 dest 参数指定的属性值

## 类似的有 optparse 但没有 argparse 先进







































