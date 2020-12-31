"""
    Author : ParkEunsik
    Date   : 2019/09/02
    url    : https://www.acmicpc.net/problem/10825
    correct percentage : 46.259%
"""

import sys
from operator import itemgetter

student = []
for i in range(int(sys.stdin.readline())):
    name, korea, english, math = sys.stdin.readline().split()
    student.append([name, -int(korea), int(english), -int(math)])
    # 여러개를 역방향, 순방향으로 한번에 정렬하고 싶으면 음수를 사용!!
student.sort(key=itemgetter(1, 2, 3, 0))
for i in student:
    print(i[0])
