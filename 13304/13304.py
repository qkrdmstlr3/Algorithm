"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/13304
"""

import sys
import math

N, M = map(int, sys.stdin.readline().split())
o_grade = 0
t_grade = [0, 0]
s_grade = [0, 0]


for i in range(N):
    s, y = map(int, sys.stdin.readline().split())
    if y == 1 or y == 2:
        o_grade += 1
    elif y == 3 or y == 4:
        if s == 1:
            t_grade[0] += 1
        else:
            t_grade[1] += 1
    else:
        if s == 1:
            s_grade[0] += 1
        else:
            s_grade[1] += 1
print(math.ceil(o_grade/M) + math.ceil(t_grade[0]/M) + math.ceil(t_grade[1]/M) + math.ceil(s_grade[0]/M) + math.ceil(s_grade[1]/M))
# ceil은 올림함수
