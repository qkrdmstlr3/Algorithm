"""
    Author : ParkEunsik
    Date   : 2019/07/13
    url    : https://www.acmicpc.net/problem/1157
"""

import sys

word = sys.stdin.readline().upper()
result, cnt, temp, mx = [0]*26, 0, 0, -1
for i in range(len(word)-1):
    result[ord(word[i])-65] += 1
    if result[ord(word[i])-65] > mx:
        mx = result[ord(word[i])-65]
for i in range(26):
    if result[i] == mx:
        cnt += 1
        temp = i
if cnt == 1:
    print(chr(temp+65))
else:
    print("?")
