"""
    Author : ParkEunsik
    Date   : 2019/09/06
    url    : https://www.acmicpc.net/problem/1697
    correct percentage : 24.839%
    bfs 
"""

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
move = (1, -1, 2)
q = deque()
check = [False]*(100001)

def bfs(start, final):
    q.append([start, 0])
    while q:
        location, count = q.popleft()
        if check[location]:
            continue
        if location == final:
            return count
        
        check[location] = True
        for i in range(2):
            if 0 > location+move[i] or 100000 < location+move[i]:
                continue
            q.append([location+move[i], count+1])
        if 0 <= location*2 <= 100000:
            q.append([location*2, count+1])

print(bfs(n, k))
