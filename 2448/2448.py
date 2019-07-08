"""
    Author             : ParkEunsik
    Date               : 2019/07/08
    url                : https://www.acmicpc.net/problem/2448
    Correct percentage : 36.477%
"""
"""
    맨 위에 가장 작은 피라미드를 기준으로 3에서 두배씩 늘어날 때마다
    li를 바꿔가면서 계산
"""
N = int(input())
li, count = ['  *  ', ' * * ', '*****'], 3

while count != N:
    li2, temp = [None]*(count*2), 0  # li2는 li보다 2배 더 큰 피라미드
    for i in range(count):
        li2[temp] = ' '*count+li[i]+' '*count
        temp += 1
    for i in range(count):
        li2[temp] = li[i]+' '+li[i]
        temp += 1
    li = li2
    count *= 2

for i in range(N):
    print(li[i])
