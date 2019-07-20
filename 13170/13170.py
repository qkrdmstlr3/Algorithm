"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/13170
"""
import sys
import math

N, K, P, W = map(int, sys.stdin.readline().split())
print(math.ceil(P/W))
