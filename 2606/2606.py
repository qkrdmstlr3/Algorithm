"""
    Author : ParkEunsik
    Date   : 2019/08/30
    url    : https://www.acmicpc.net/problem/2606
    correct percentage : 41.094%
"""

import sys
sys.setrecursionlimit(100000)

computer = [[] for i in range(int(sys.stdin.readline())+1)]
virus = [1]


def check_virus(arr):
    while len(arr) != 0:
        com = arr.pop()
        if com not in virus:
            virus.append(com)
            check_virus(computer[com])


for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    computer[a].append(b)
    computer[b].append(a)  # 반대로도 추가를 시켜주어야 했다;; 
check_virus(computer[1])
print(len(virus)-1)
