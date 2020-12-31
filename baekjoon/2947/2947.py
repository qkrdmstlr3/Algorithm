"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/2947
"""
import sys

stack = list(map(int, sys.stdin.readline().split()))
temp = [1, 2, 3, 4, 5]
while temp != stack:
    for i in range(4):
        if stack[i] > stack[i+1]:
            tmp = stack[i]
            stack[i] = stack[i+1]
            stack[i+1] = tmp
            for j in range(5):
                print(stack[j], end=' ')
            print()
