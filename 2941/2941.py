"""
    Author : ParkEunsik
    Date   : 2019/07/13
    url    : https://www.acmicpc.net/problem/2941
    개선해보기 if2개 줄이는거
"""
import sys

li, cnt = sys.stdin.readline(), 0
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in range(len(li)-1):
    if li[i]+li[i+1] in alphabet:
        cnt += 1
    if li[i]+li[i+1] == 'dz' and li[i+1]+li[i+2] == 'z=':
        cnt += 1
print(len(li)-cnt-1)
