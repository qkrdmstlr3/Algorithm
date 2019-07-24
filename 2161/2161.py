"""
    Author : ParkEunsik
    Date   : 2019/07/24
    url    : https://www.acmicpc.net/problem/2161
"""

import sys

card = list(range(1, int(sys.stdin.readline())+1))
result = []
for i in range(len(card)):
    if len(card) == 1:
        break
    elif len(card) == 2:
        result.append(card.pop(0))
        break
    result.append(card.pop(0))
    card.append(card.pop(0))
for i in range(len(result)):
    print(result[i], end=' ')
print(card[0])
