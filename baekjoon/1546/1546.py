"""
    Author : ParkEunsik
    Date   : 2019/07/12
    url    : https://www.acmicpc.net/problem/1546
    correct percentage: 47.194%
"""
import sys

N = int(input())
score = list(map(int, sys.stdin.readline().split()))
score.sort()
for i in range(N):
    score[i] = score[i]/score[-1]*100
print(sum(score)/N)
