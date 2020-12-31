"""
    Author : ParkEunsik
    Date   : 2019/07/10
    url    : https://www.acmicpc.net/problem/14724
"""
N = int(input())
club, max = ["PROBRAIN", "GROW",  "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY",""], 0
for i in range(len(club)-1):
    scores = list(map(int, input().split()))
    for j in range(N):
        if max < scores[j]:
            max = scores[j]
            club[9] = club[i]
print(club[9])
