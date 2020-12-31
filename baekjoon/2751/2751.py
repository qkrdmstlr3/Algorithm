"""
    Author : ParkEunsik
    Date   : 2019/07/16
    url    : https://www.acmicpc.net/problem/2751
    10989코드를 개조함!!
"""

import sys

result = [0]*2000002  # 1000001 이전은 음수 이후는 양수 구간
max, min = 0, 2000003  # 너무 많은 반복 방지 위함
for i in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if num > 0:
        result[num+1000000] += 1
    else:
        result[num+1000000] += 1
    if num > max:
        max = num
    if num < min:
        min = num
for i in range(min+1000000, max+1000001):
    for j in range(result[i]):
        print(i-1000000)
