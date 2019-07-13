"""
    Author : ParkEunsik
    Date   : 2019/07/13
    url    : https://www.acmicpc.net/problem/1152
    correct percentage : 24.459%
"""

import sys

word, cnt = sys.stdin.readline(), 1
if(word[-2] == ' '):
    cnt = 0
for i in range(1, len(word)-1):
    if word[i] == ' ':
        cnt += 1
print(cnt)
