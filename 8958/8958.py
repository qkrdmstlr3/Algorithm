"""
    Author : ParkEunsik
    Date   : 2019/07/12
    url    : https://www.acmicpc.net/problem/8958
"""
import sys

for i in range(int(input())):
    case, num_sum, cnt = list(sys.stdin.readline()), 0, 0
    for j in range(len(case)-1):
        if case[j] == 'X':
            cnt = 0
        else:
            cnt += 1
            num_sum += cnt
    print(num_sum)
