"""
    Author : ParkEunsik
    Date   : 2019/08/01
    url    : https://www.acmicpc.net/problem/3023
"""

import sys

R, C = map(int, sys.stdin.readline().split())
card, card2 = [], []
for i in range(R):
    pattern = sys.stdin.readline().rstrip()
    card.append(pattern+''.join(reversed(pattern)))
for i in range(R):
    card2.append(card[-i-1])
card = card+card2

a, b = map(int, sys.stdin.readline().split())
if card[a-1][b-1] == '#':
    li = list(card[a-1])
    li[b-1] = '.'
    card[a-1] = ''.join(li)
else:
    li = list(card[a-1])
    li[b-1] = '#'
    card[a-1] = ''.join(li)

print('\n'.join(card))
