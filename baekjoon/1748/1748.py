"""
    Author : ParkEunsik
    Date   : 2019/08/03
    url    : https://www.acmicpc.net/problem/1748
"""
import sys

N = int(sys.stdin.readline())

cnt, sm = 1, 0
while N >= 10**cnt:
    sm += (9*(10**(cnt-1)))*cnt
    cnt += 1
sm += (N-(10**(cnt-1))+1)*cnt
print(sm)
