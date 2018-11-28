# 1.3 保留最后N个元素 "collections.deque"   ========== deque 队列
from collections import deque
def search(lines, pattern, history=5):
    previous_line = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            previous_line.append(line)
        yield line, previous_line
## Example use on a file
if __name__ == '__main__':
    with open(r'./somefile.txt') as f:
        print("start search() ==>")
        for line, prevlines in search(f, 'welcome', 2):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
## 队列两端插入元素，时间复杂度是o(1); 列表开头插入或删除时间复杂度是


# 1.4 查找最大或最小的N个元素 ========== heap 堆
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s:s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s:s['price'])

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print(heap)

## 堆特征： heap[0]为最小元素，heapq.heappop()获取元素--时间复杂度O(logN),N为堆大小
## 根据堆与要取得的集合大小不同，依次采用min()/max(), nlargest()/nsmallest(), sorted(items)[:N] 不同的方式











