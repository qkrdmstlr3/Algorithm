"""
    Author : ParkEunsik
    Date   : 2019/07/13
    url    : https://www.acmicpc.net/problem/10809
"""
N = input()
result = [-1]*26
for i in reversed(range(len(N))):
    result[ord(N[i])-97] = i
for i in range(26):
    print(result[i], end=' ')
