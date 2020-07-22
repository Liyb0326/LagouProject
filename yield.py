#!/usr/bin/python3
"""
斐波那契数列
"""
import sys


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        print('yieldbef' + str(a))
        yield a
        print('yieldafter' + str(a))
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
cout = 0
while True:
    try:
        cout = cout+1
        print(f'-----{cout}--------')
        print(next(f), end=" ")

    except StopIteration:
        sys.exit()