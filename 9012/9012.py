"""
    Author : ParkEunsik
    Date   : 2019/07/10
    url    : https://www.acmicpc.net/problem/9012
    Correct percentage : 39.075%
"""


class Stack(list):
    push = list.append

    def top(self):
        return self[-1]

    def is_empty(self):
        if not self:
            return True
        else:
            return False


N = int(input())
for i in range(N):
    vps, s = list(input()), Stack()
    for j in range(len(vps)):
        if vps[j] == "(":
            s.push(vps[j])
        else:
            if s.is_empty() is True:
                print("NO")
                break
            else:
                s.pop()
        if j == len(vps)-1 and s.is_empty() is True:
            print("YES")
        elif j == len(vps)-1:
            print("NO")
