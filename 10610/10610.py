"""
    Author : ParkEunsik
    Date   : 2019/07/23
    url    : https://www.acmicpc.net/problem/10610
    correct percentage : 35.360%
    모든 자리 숫자의 합이 3이고 0이 1개라도 있으면됨
"""

import sys
import itertools

N = list(sys.stdin.readline())
N.pop()  # 개행문자 제거
N = list(map(int, N))

if sum(N) % 3 != 0 or 0 not in N:
    print(-1)
else:
    N.sort(reverse=True)
    N = list(map(str, N))
    print(''.join(N))
