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

for i in range(len(arr)):
    if arr[i] >= 1 and arr[i] <= 26 and chr(arr[i]+64) not in text:
        flag = False
        break
    elif arr[i] >= 27 and arr[i] <= 52 and chr(arr[i]+70) not in text:
        print(chr(arr[i]+70))
        flag = False
        break
    elif arr[i] == 0 and ' ' not in text:
        flag = False
        break
if flag is True:
    print("y")
else:
    print("n")
