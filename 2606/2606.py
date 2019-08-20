"""
    Author : ParkEunsik
    Date   : 2019/08/20
    url    : https://www.acmicpc.net/problem/2606
"""

import sys

computer = [[] for i in range(int(sys.stdin.readline())+1)]
virus = []


def check_virus(arr):
    while len(arr) != 0:
        com = arr.pop(0)
        if com not in virus:
            virus.append(com)
            viru(computer[com])


for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    computer[a].append(b)
check_virus(computer[1])
print(len(virus))
