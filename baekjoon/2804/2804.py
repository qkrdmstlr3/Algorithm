"""
    Author : ParkEunsik
    Date   : 2019/08/01
    url    : https://www.acmicpc.net/problem/2804
"""

import sys

a, b = input().split()
word = ''
for i in range(len(a)):
    if a[i] in b:
        word = a[i]
        break
for i in range(len(b)):
    if b.index(word) == i:
        print(''.join(a))
    else:
        print('.'*a.index(word)+b[i]+'.'*(len(a)-a.index(word)-1), sep='')
