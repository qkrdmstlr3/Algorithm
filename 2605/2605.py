"""
    Author : ParkEunsik
    Date   : 2019/08/26
    url    : https://www.acmicpc.net/problem/2605
"""

import sys

line = []
num_student = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

for i in range(num_student):
    line.insert(numbers[i], i+1)
line.reverse()
print(' '.join(map(str, (line))))
