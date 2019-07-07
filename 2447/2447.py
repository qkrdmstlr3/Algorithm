"""
    Author : ParkEunsik
    Date   : 2019/07/07
    url    : https://www.acmicpc.net/problem/2447
"""
N = int(input())
li = ['***', '* *', '***']
count = 3

while True:
    if count == N:
        break
    count *= 3

    li2 = [None]*(len(li)*3)
    for i in range(count):
        temp = int(i % (count/3))   # count/3 = 9
        li2[i] = li[temp]*3
        if i >= count/3 and i < count/3*2:
            li2[i] = li[temp]+' '*int(count/3)+li[temp]
    li = li2
for i in range(N):
        print(li[i])
