#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__ = '12 05, 2014 '
__author__ = 'mkfsn'

t, n = [int(i) for i in raw_input().split(' ')[:2]] 

total = 0
result = 0

l = []
for i in range(n):
    num = int(raw_input())
    l.append(num)
    if t > 0:
        total += num
        t -= 1
    else:
        total -= l.pop(0)
        total += num

    if total > result:
        result = total
l = []

print result


"""
Test case 1
通過
実行時間： 0.02 秒
Test case 2
通過
実行時間： 0.03 秒
Test case 3
通過
実行時間： 0.02 秒
Test case 4
通過
実行時間： 7.39 秒
Test case 5
通過
実行時間： 7.39 秒
"""
