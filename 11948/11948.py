"""
    Author : ParkEunsik
    Date   : 2019/08/03
    url    : https://www.acmicpc.net/problem/11948
"""

import sys
import itertools

main_subject, sub_subject = [], []
total_score = 0
for i in range(4):
    main_subject.append(int(sys.stdin.readline()))
for i in range(2):
    sub_subject.append(int(sys.stdin.readline()))
for i in itertools.combinations(main_subject, 3):
    for j in itertools.combinations(sub_subject, 1):
        total_score = max(total_score, sum(i)+sum(j))
print(total_score)
