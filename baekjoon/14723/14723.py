"""
    Author : ParkEunsik
    Date   : 2019/07/11
    url    : https://www.acmicpc.net/problem/14723
"""
N = int(input())
bj, bm = 1, 1
for i in range(1, N):
    if bj == 1:
        bj = bm+bj
        bm = 1
    else:
        bj -= 1
        bm += 1
print(str(bj) + " " + str(bm))
