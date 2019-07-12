"""
    Author : ParkEunsik
    Date   : 2019/07/12
    url    : https://www.acmicpc.net/problem/3052
"""
import sys

result, cnt = [0]*42, 0
for i in range(10):
    result[int(sys.stdin.readline()) % 42] += 1
for i in range(len(result)):
    if result[i] != 0:
        cnt += 1
print(cnt)
