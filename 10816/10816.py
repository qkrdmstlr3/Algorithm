"""
    Author : ParkEunsik
    Date   : 2019/09/02
    url    : https://www.acmicpc.net/problem/10816
    correct percentage : 33.632%
    이분탐색
"""

import sys
import bisect

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
card.sort()
M = int(sys.stdin.readline())

for i in list(map(int, sys.stdin.readline().split())):
    count = bisect.bisect_left(card, i)
    if count < len(card) and card[count]==i: # 리스트에 있어야함
        count2 = bisect.bisect_left(card, i+1)
        print(count2 - count, end=' ')
    else:
        print(0, end=' ')
