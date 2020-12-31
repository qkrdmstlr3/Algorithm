"""
    Author : ParkEunsik
    Date   : 2019/07/29
    url    : https://www.acmicpc.net/problem/5586
"""

import sys

text = input()
joi_cnt, ioi_cnt = 0, 0
for i in range(len(text)-2):
    if text[i]+text[i+1]+text[i+2] == 'JOI':
        joi_cnt += 1
    elif text[i]+text[i+1]+text[i+2] == 'IOI':
        ioi_cnt += 1
print(joi_cnt, ioi_cnt, sep='\n')
