"""
    Author : ParkEunsik
    Date   : 2019/08/24
    url    : https://www.acmicpc.net/problem/1735
"""

import sys

M, N = map(int,input().split())
li = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
text_num = []
for i in range(M, N+1):
    text = list(str(i))
    txt = ''
    for j in range(len(text)):
        txt += li[int(text[j]) % 10]
    text_num.append([txt, i])
text_num.sort()
for i in range(len(text_num)):
    print(text_num[i][1], end=' ')
    if (i+1) % 10 == 0:
        print()
