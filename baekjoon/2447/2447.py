"""
    Author : ParkEunsik
    Date   : 2019/07/07
    url    : https://www.acmicpc.net/problem/2447
"""
"""
3*3을 전제로 계속 3배씩 늘려나감과 동시에 리스트를 수정해나감
"""
N = int(input())
li, count = ['***', '* *', '***'], 3

while count != N:
    count *= 3

    li2 = [None]*(len(li)*3)
    for i in range(count):
        temp = int(i % (count/3))
        li2[i] = li[temp]*3  # 빈 칸 위 아래 줄 만들어주기
        if i >= count/3 and i < count/3*2:  # 가운데 빈 칸 만들어주기
            li2[i] = li[temp]+' '*int(count/3)+li[temp]
    li = li2

for i in range(N):
        print(li[i])
