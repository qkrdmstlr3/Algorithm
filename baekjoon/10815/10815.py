"""
    Author : ParkEunsik
    Date   : 2019/09/02
    url    : https://www.acmicpc.net/problem/10815
    correct percentage : 47.394%
    이분탐색
"""

import sys

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
card.sort()
M = int(sys.stdin.readline())

for i in list(map(int, sys.stdin.readline().split())):
    front = 0
    back = N-1
    while True:
        center = (front+back)//2
        if front > back:
            print(0, end=' ')
            break
        if card[center] < i:
            front = center+1
        elif card[center] > i:
            back = center-1
        elif card[center] == i:
            print(1, end=' ')
            break
