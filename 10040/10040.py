"""
    Author : ParkEunsik
    Date   : 2019/08/29
    url    : https://www.acmicpc.net/problem/10040
"""

import sys

N, M = map(int, sys.stdin.readline().split())
play_cost = []
ticket = [0]*(N+1)
for i in range(N):
    play_cost.append(int(sys.stdin.readline()))
for i in range(M):
    judge = int(sys.stdin.readline())
    for j in range(len(play_cost)):
        if play_cost[j] <= judge:
            ticket[j] += 1
            break
print(ticket.index(max(ticket))+1)
