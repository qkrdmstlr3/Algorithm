"""
    Author : ParkEunsik
    Date   : 2019/08/27
    url    : https://www.acmicpc.net/problem/15873
"""

import sys

num = sys.stdin.readline().rstrip()
if '0' in num:
    a = num[:num.index('0')+1]
    b = num[num.index('0')+1:]
    if b == '':
        print(int(num[:1])+int(num[1:]))
    else:
        print(int(a)+int(b))
else:
    print(int(num[0])+int(num[1]))
