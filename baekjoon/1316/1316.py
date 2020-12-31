"""
    Author : ParkEunsik
    Date   : 2019/07/13
    url    : https://www.acmicpc.net/problem/1316
"""

import sys

cnt = 0
for i in range(int(input())):
    word = sys.stdin.readline()
    alphbet, flag = [0]*26, True
    for j in range(len(word)-1):
        if alphbet[ord(word[j])-97] != 0 and word[j] != word[j-1]:
            flag = False
            break
        alphbet[ord(word[j])-97] += 1
    if flag is False:
        continue
    else:
        cnt += 1
print(cnt)
