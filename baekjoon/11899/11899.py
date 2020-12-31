"""
    Author : ParkEunsik
    Date   : 2019/07/21
    url    : https://www.acmicpc.net/problem/11899
"""

import sys

sen = sys.stdin.readline()
q1, q2, cnt = [], [], 0

for i in range(len(sen)-1):
    if sen[i] == ')':
        if len(q2) != 0:
            q2.pop()
        else:
            cnt += 1
    elif sen[i] == '(':
        q2.append('(')
print(cnt+len(q2))
