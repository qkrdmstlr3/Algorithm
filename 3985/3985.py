"""
    Author : ParkEunsik
    Date   : 2019/08/04
    url    : https://www.acmicpc.net/problem/3985
"""
import sys

roll = [0]*(int(sys.stdin.readline())+1)
audience = [0]*(int(sys.stdin.readline())+1)
piece, real, expected = 0, 0, 0
for i in range(len(audience)-1):
    p, k = map(int, sys.stdin.readline().split())
    if k-p+1 > piece:
        expected = i+1
        piece = k-p+1
    for j in range(p, k+1):
        if roll[j] == 0:
            roll[j] = i+1
for i in range(1, len(roll)):
    audience[roll[i]] += 1
real = audience[1:].index(max(audience[1:]))+1
print(expected, real, sep='\n')
