"""
    Author : ParkEunsik
    Date   : 2019/08/28
    url    : https://www.acmicpc.net/problem/2755
"""

import sys


def switch(num):
    return {'A+':4.3, 'A0':4.0, 'A-':3.7, 'B+':3.3, 'B0':3.0, 'B-':2.7, 'C+':2.3, 'C0':2.0, 'C-':1.7, 'D+':1.3, 'D0':1.0, 'D-':0.7, 'F':0.0}[num]


score_sum = 0
result = 0
N = int(sys.stdin.readline())
if N == 0:
    print("0.00")
else:
    for i in range(N):
        subject, score, grade = sys.stdin.readline().split()
        score_sum += int(score)
        result += switch(grade)*int(score)
    result /= score_sum
    if result*100%10 == 5:
        print('{:.02f}'.format(round(result+0.001, 2)))
    else:
        print('{:.02f}'.format(round(result, 2)))
