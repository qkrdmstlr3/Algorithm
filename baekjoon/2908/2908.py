"""
    Author : ParkEunsik
    Date   : 2019/07/13
    url    : https://www.acmicpc.net/problem/2908
"""
import sys

li = list(sys.stdin.readline().split())
li[0] = ''.join(reversed(li[0]))
li[1] = ''.join(reversed(li[1]))
li = list(map(int, li))
print(max(li))
