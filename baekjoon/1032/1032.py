"""
    Author : ParkEunsik
    Date   : 2019/07/07
    url    : https://www.acmicpc.net/problem/1032
"""
N = int(input())
li = []
for i in range(N):
    li.append(input())

li_result = list(li[0])

for i in range(len(li[0])):
    for j in range(N-1):
        if li[j][i] != li[j+1][i]:  # j+1!!!!!!
            li_result[i] = '?'
            break
print(''.join(li_result))  # 리스트를 합쳐서 문자열로 변환
