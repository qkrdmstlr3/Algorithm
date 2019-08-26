"""
    Author : ParkEunsik
    Date   : 2019/08/26
    url    : https://www.acmicpc.net/problem/2607
    correct_percentage : 27.595%
"""

import sys

N = int(sys.stdin.readline())
main = list(sys.stdin.readline().rstrip())
alphabet = [0]*26
count = 0
for i in main:
    alphabet[ord(i)-65] += 1  # 메인 단어의 단어들의 숫자를 하나씩 늘려줌

for i in range(N-1):
    word = list(sys.stdin.readline().rstrip())
    sub_alphabet = alphabet[:]
    for j in word:
        sub_alphabet[ord(j)-65] -= 1  # 입력받은 단어의 단어들을 하나씩 빼줌
    plus_count = 0
    minus_count = 0
    for j in sub_alphabet:
        if j > 0:
            plus_count += j
        elif j < 0:
            minus_count += j
    if plus_count <= 1 and minus_count >= -1:  # -1보다 작거나 1보다 크면 그 문자를 두번 바꿔야 하기 때문에 안됨 -1, 1로 나오면 서로 바꿀수 있어서 가능
        count += 1
print(count)
