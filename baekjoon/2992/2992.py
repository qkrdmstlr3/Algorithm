"""
    Author : ParkEunsik
    Date   : 2019/08/04
    url    : https://www.acmicpc.net/problem/2992
"""
import sys
import itertools

flag = True
num, mi = list(input()), '999999'
for i in itertools.permutations(num, len(num)):
    if ''.join(i) <= ''.join(num):
        continue
    elif ''.join(i) > ''.join(num):
        mi = min(mi, ''.join(i))
        flag = False
if flag:
    print(0)
else:
    print(mi)
