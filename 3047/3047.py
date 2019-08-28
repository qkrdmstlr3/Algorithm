"""
    Author : ParkEunsik
    Date   : 2019/08/28
    url    : https://www.acmicpc.net/problem/3047
"""

import sys

number = sorted(list(map(int, sys.stdin.readline().split())))
word =  sys.stdin.readline().rstrip()
for i in range(3):
    print(number[ord(word[i])-65], sep=' ')

