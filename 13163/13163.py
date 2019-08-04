"""
    Author : ParkEunsik
    Date   : 2019/08/04
    url    : https://www.acmicpc.net/problem/13163
"""
import sys

for i in range(int(sys.stdin.readline())):
    name = list(sys.stdin.readline().split())
    name[0] = "god"
    print(''.join(name))
