"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/10102
"""

import sys

v = int(sys.stdin.readline())
text, cnt = sys.stdin.readline(), 0
for i in range(len(text)-1):
    if text[i] == 'A':
        cnt += 1
    elif text[i] == 'B':
        cnt -= 1
if cnt > 0:
    print("A")
elif cnt < 0:
    print("B")
else:
    print("Tie")
