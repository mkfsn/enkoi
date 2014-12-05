#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__ = '12 05, 2014 '
__author__ = 'mkfsn'

line = int(raw_input())

total = 0

for i in range(line):
    x = raw_input().rstrip('\n').split(' ')

    t, s, p = [int(x[0]), int(x[1]), int(x[2])]

    if t > s:
        total += ( (t-s)*p )

print total

"""
Test case 1
通過
実行時間： 0.03 秒
Test case 2
通過
実行時間： 0.02 秒
Test case 3
通過
実行時間： 0.02 秒
"""
