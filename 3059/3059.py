"""
    Author : ParkEunsik
    Date   : 2019/08/29
    url    : https://www.acmicpc.net/problem/3059
"""

import sys

for i in range(int(sys.stdin.readline())):
    S = sys.stdin.readline().rstrip()
    alphabet = [False]*26
    num_sum = 0
    for j in range(len(S)):
        alphabet[ord(S[j])-65] = True
    for j in range(26):
        if alphabet[j] is False:
            num_sum += j+65
    print(num_sum)
