"""
    Author : ParkEunsik
    Date   : 2019/07/21
    url    : https://www.acmicpc.net/problem/9086
"""

import sys
li = []
for i in range(int(sys.stdin.readline())):
    text = input()
    li.append(text[0]+text[-1])
for i in range(len(li)):
    print(li[i])
