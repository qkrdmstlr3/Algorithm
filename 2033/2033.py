"""
    Author : ParkEunsik
    Date   : 2019/08/02
    url    : https://www.acmicpc.net/problem/2033
    correct percentage : 38.129%
"""

import sys
import math

N = int(sys.stdin.readline())
N_len = len(str(N))

for i in range(1, N_len):
    if str(N)[N_len-i] == '5':  # 그 자릿수가 5라면 6으로 바꿔서 계산 > python은 5에서 버림이 됨;;
        text = list(str(N))
        text[N_len-i] = '6'
        N = int(''.join(text))
        N = round(N, -i)
    else:
        N = round(N, -i)
print(N)
