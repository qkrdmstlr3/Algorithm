"""
    Author : ParkEunsik
    Date   : 2019/08/04
    url    : https://www.acmicpc.net/problem/2997
"""
import sys

num = sorted(list(map(int, sys.stdin.readline().split())))
if num[0]-num[1] == num[1]-num[2]:
    print(num[2]+num[1]-num[0])
elif (num[0]-num[1])//2 == num[1]-num[2]:
    print(num[0]+(num[2]-num[1]))
elif num[0]-num[1] == (num[1]-num[2])//2:
    print(num[2]-(num[1]-num[0]))
