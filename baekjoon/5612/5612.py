"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/5612
"""
import sys

N = int(sys.stdin.readline())
car_cnt, mx = int(sys.stdin.readline()), 0
if car_cnt == 2 < 0:
    print(0)
    exit()
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    car_cnt += (a - b)
    if car_cnt < 0:
        mx = 0
        break
    else:
        mx = max(car_cnt, mx)
print(mx)
