"""
    Author : ParkEunsik
    Date   : 2019/07/12
    url    : https://www.acmicpc.net/problem/2920
"""
import sys

N = list(map(int, sys.stdin.readline().split()))
if N == [1, 2, 3, 4, 5, 6, 7, 8]:
    print("ascending")
elif N == [8, 7, 6, 5, 4, 3, 2, 1]:
    print("descending")
else:
    print("mixed")
