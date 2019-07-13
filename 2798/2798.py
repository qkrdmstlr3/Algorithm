"""
    Author : ParkEunsik
    Date   : 2019/07/13
    url    : https://www.acmicpc.net/problem/2798
    순열 조합!!!!!!!!!!!! itertools
"""

import itertools

n_sum = 0
N, M = map(int, input().split())
for i in itertools.combinations(list(map(int, input().split())), 3):
    if sum(i) <= M and n_sum < sum(i):
        n_sum = sum(i)
print(n_sum)
