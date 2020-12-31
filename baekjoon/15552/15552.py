"""
    Author : ParkEunsik
    Date   : 2019/07/12
    url    : https://www.acmicpc.net/problem/15552
"""
import sys

N = int(input())
for i in range(N):
    num1, num2 = map(int, sys.stdin.readline().split())
    print(num1+num2)
