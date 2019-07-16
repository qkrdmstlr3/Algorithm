"""
    Author : ParkEunsik
    Date   : 2019/07/16
    url    : https://www.acmicpc.net/problem/17176
"""

import sys

N = sys.stdin.readline()
arr = list(map(int, sys.stdin.readline().split()))
text = list(sys.stdin.readline())
flag = True

for i in range(len(text)):
    if text[i] >= 'A' and text[i] <= 'Z' and ord(text[i])-64 not in arr:
        flag = False
        break
    elif text[i] >= 'a' and text[i] <= 'z' and ord(text[i])-70 not in arr:
        flag = False
        break
    elif text[i] == ' ' and 0 not in arr:
        flag = False
        break
if flag is True:
    print("y")
else:
    print("n")
