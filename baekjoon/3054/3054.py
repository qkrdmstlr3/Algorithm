"""
    Author : ParkEunsik
    Date   : 2019/08/28
    url    : https://www.acmicpc.net/problem/3054
"""

import sys

word = input()
result = []
piter_frame = ['..#..', '.#.#.', '#..#', '.#.#.']
wendy_frame = ['..*..', '.*.*.', '*..*', '.*.*.']

for i in range(1, len(word)+1):
    if i % 3 == 0:
        result.append(wendy_frame[0])
        result.append(wendy_frame[1])
        result.append(wendy_frame[2][:2]+word[i-1]+wendy_frame[2][2:])
        result.append(wendy_frame[3])
    else:
        if i != 1 and i % 3 == 1:
            result.append(wendy_frame[0])
        else:
            result.append(piter_frame[0])
        result.append(piter_frame[1])
        result.append(piter_frame[2][:2]+word[i-1]+piter_frame[2][2:])
        result.append(piter_frame[3])
if len(word) % 3 == 0:
    result.append(wendy_frame[0])
else:
    result.append(piter_frame[0])
for i in range(5):
    for j in range(4*len(word)+1):
        print(result[j][i], end='')
    print()
