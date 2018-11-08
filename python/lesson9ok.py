import matplotlib.pyplot as plt

## 1.饼状图
animals = [10, 20, 30, 40]
labels = 'chicken', 'ducks', 'gooses', 'rabbits'
colors = 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral'
explode = [0, 0.2, 0, 0]
plt.pie(animals, colors=colors, labels=labels, autopct='%1.1f%%',
        explode=explode, shadow=True, startangle=30)
plt.axis('equal')
plt.show()


## 2.柱状图
# import numpy as np
# scoreLily = [75, 88, 80]  # Chinese, Math, English
# subjectNum = 3
# x = np.arange(subjectNum)
# width = 0.4 / subjectNum
# scoreTom = [91, 70, 86]
# scoreJerry = [87, 100, 90]
# scoreJack = [77, 80, 70]
# personNum = 4
# plt.bar(x, scoreLily, width=width, color='yellowgreen', label='Lily')
# plt.bar(x + 1 * width, scoreTom, color='gold', width=width, label='Tom')
# plt.bar(x + 2 * width, scoreJerry, color='lightskyblue', width=width, label='Jerry')
# plt.bar(x + 3 * width, scoreJack, color='lightcoral', width=width, label='Jack')
# plt.xticks(x + (width/2)*(personNum-1), ['Chinese', 'Math', 'English'])
# plt.legend()
# plt.title("Monthly Examination ---- April")
# plt.show()


## 3.柱状图 课堂实践
# import numpy as np
#
# scoreLily = [75, 88, 80]  # Chinese, Math, English
# scoreTom = [91, 70, 86]
# scoreJerry = [87, 100, 90]
# scoreJack = [77, 80, 70]
# scoreChinese = [75, 91, 87, 77]
# scoreMath = [88, 70, 100, 80]
# scoreEnglish = [75, 91, 87, 70]
# subjectNum = 3
# personNum = 4
# x = np.arange(personNum)
# width = 0.8 / personNum
# plt.bar(x, scoreChinese, width=width, color='yellowgreen', label='Chinese')
# plt.bar(x + 1 * width, scoreMath, color='gold', width=width, label='Math')
# plt.bar(x + 2 * width, scoreEnglish, color='lightskyblue', width=width, label='English')
# plt.xticks(x + (width / 2) * (subjectNum - 1), ['Lily', 'Tom', 'Jerry', 'Jack'])
# plt.legend()
# plt.title("Monthly Examination ---- April")
# plt.show()


## 4.折线图/函数图
# import numpy as np
#
# x = np.linspace(0, 2 * np.pi, 100)
# y1 = 2 * x + 1
# y2 = 1 / x
# y3 = x * x - 5 * x + 7
# plt.plot(x, y1, color='lightskyblue', label='y = 2x+1')
# plt.plot(x, y2, color='lightcoral', label='y = 1/x')
# plt.plot(x, y3, color='yellowgreen', label='y = x^2-5x+7',
#          ls='-.')
# plt.scatter(1, 2, color='red', marker='*')
# plt.title('line chart')
# plt.xlim([0, 5])
# plt.ylim([0, 5])
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()


# 折线图/函数图 课堂实践
# import numpy as np
#
# x = np.linspace(0, 2 * np.pi, 100)
# y1 = 2*x+1
# y2 = 1/x
# plt.plot(x, y1, label='y = 2x+1')
# plt.plot(x, y2, label='y = 1/x')
# plt.title('line chart')
# plt.xlim([0, 5])
# plt.ylim([0, 5])
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()


## 一元线性回归
## 如报错 xxx module can't be found 缺失模块的异常 可在命令行中运行"pip install xxxx" 安装相应模块

# import numpy as np
# from sklearn.linear_model import LinearRegression
#
# x = np.linspace(1, 2 * np.pi, 100)
# y1 = 2*x+1
# y2 = 1/x
# plt.plot(x, y2)
#
# square = [150, 200, 250, 300, 350, 400, 600]
# price = [6450, 7450, 8450, 9450, 11450, 15450, 18450]
# plt.scatter(square, price, color='red', marker='*')
# regr = LinearRegression()
# xparam = []
# for item in square:
#     xparam.append([item])
# regr.fit(xparam, price)
# plt.plot(square, regr.predict(xparam), color='lightskyblue')
# plt.title('house price')
# plt.show()

# '-'       solid line style
# '--'      dashed line style
# '-.'      dash-dot line style
# ':'       dotted line style
#
# '.'       point marker
# ','       pixel marker
# 'o'       circle marker
# 'v'       triangle_down marker
# '^'       triangle_up marker
# '<'       triangle_left marker
# '>'       triangle_right marker
# '1'       tri_down marker
# '2'       tri_up marker
# '3'       tri_left marker
# '4'       tri_right marker
# 's'       square marker
# 'p'       pentagon marker
# '*'       star marker
# 'h'       hexagon1 marker
# 'H'       hexagon2 marker
# '+'       plus marker
# 'x'       x marker
# 'D'       diamond marker
# 'd'       thin_diamond marker
# '|'       vline marker
# '_'       hline marker


## 随机数产生
# import numpy as np
# print(np.random.random())  # 随机产生0-1间小数
# print(np.random.randint(0, 6))  # 随机产生[0,4)整数


## 课堂作业1
# import numpy as np
# scoreLily = [75, 88, 80]  # Chinese, Math, English
# subjectNum = 3
# x = np.arange(subjectNum)
# width = 0.4 / subjectNum
# scoreTom = [91, 70, 86]
# scoreJerry = [87, 100, 90]
# scoreJack = [77, 80, 70]
# personNum = 4
# plt.bar(x, scoreLily, width=width, color='yellowgreen', label='Lily')
# plt.bar(x + 1 * width, scoreTom, color='gold', width=width, label='Tom')
# plt.bar(x + 2 * width, scoreJerry, color='lightskyblue', width=width, label='Jerry')
# plt.bar(x + 3 * width, scoreJack, color='lightcoral', width=width, label='Jack')
# plt.xticks(x + (width/2)*(personNum-1), ['Chinese', 'Math', 'English'])
# plt.legend()
# plt.title("Monthly Examination ---- April")
# plt.show()


## 课堂作业二
# import numpy as np
# count = [0, 0, 0, 0, 0, 0]
# for i in range(1000000):
#     count[np.random.randint(0, 6)] += 1
# labels = '1', '2', '3', '4', '5', '6'
# colors = 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'springgreen', 'violet'
# plt.pie(count, colors=colors, labels=labels, autopct='%1.1f%%', startangle=0)
# plt.axis('equal')
# plt.show()


## 课堂作业三
# from matplotlib import pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
#
# fig = plt.figure()
# ax = Axes3D(fig)
# X = np.arange(-4, 4, 0.25)
# Y = np.arange(-4, 4, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(32 - X**2 - Y**2)
# Z = X**2 - Y**2
#
# # 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
# ax.plot_surface(X, Y, R, rstride=1, cstride=1, cmap='rainbow')
#
# plt.show()