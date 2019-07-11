"""
    Author : ParkEunsik
    Date   : 2019/07/10
    url    : https://www.acmicpc.net/problem/9012
    Correct percentage : 36.349%
"""

N = int(input())
num = list(map(int, input().split()))

list1 = []
print(0, end=' ')

for i in range(N):
    list2 = []
    for j in reversed(range(i)):
        if len(list1) != 0:
            list2.insert(0, list1[-1])
            if list1.pop(-1) >= num[i]:
                print(j+1, end=' ')
                break
        if len(list1) == 0:
            print(0, end=' ')
            break
    list1 = list1+list2
    list1.append(num[i])
