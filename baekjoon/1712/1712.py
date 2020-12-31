"""
    Author : ParkEunsik
    Date   : 2019/07/13
    url    : https://www.acmicpc.net/problem/1712
    correct percentage : 30.795%
"""
import sys

li = list(map(int, sys.stdin.readline().split()))
if li[1] >= li[2]:
    print(-1)
else:
    print(li[0]//(li[2]-li[1])+1)
