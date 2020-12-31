"""
    Author : ParkEunsik
    Date   : 2019/08/03
    url    : https://www.acmicpc.net/problem/5533
"""

import sys

game_score = []
for i in range(int(sys.stdin.readline())):
    game_score.append(list(map(int, sys.stdin.readline().split())))
result_score = [0]*len(game_score)
for i in range(3):
    for j in range(len(result_score)):
        flag = True
        for k in range(len(result_score)):
            if game_score[j][i] == game_score[k][i] and j != k:
                flag = False
                break
        if flag:
            result_score[j] += game_score[j][i]
print('\n'.join(map(str, result_score)))
