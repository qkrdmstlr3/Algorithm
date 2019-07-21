"""
    Author : ParkEunsik
    Date   : 2019/07/21
    url    : https://www.acmicpc.net/problem/2744
"""

import sys

word = sys.stdin.readline()
for i in range(len(word)-1):
    if ord(word[i]) < 97:
        print(chr(ord(word[i])+32), end='')
    else:
        print(chr(ord(word[i])-32), end='')
