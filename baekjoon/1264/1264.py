"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/1264
"""

import sys

vocoid = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True:
    sentence, cnt = sys.stdin.readline(), 0
    if sentence == '#\n':  # 개행 조심
        break
    for i in range(len(sentence)-1):
        if sentence[i] in vocoid:
            cnt += 1
    print(cnt)
