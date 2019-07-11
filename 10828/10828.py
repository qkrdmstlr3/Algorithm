"""
    Author : ParkEunsik
    Date   : 2019/07/10
    url    : https://www.acmicpc.net/problem/10828
    Correct percentage : 41.331%
"""


class Stack(list):
    push = list.append

    def top(self):
        if self.size() == 0:
            return -1
        else:
            return self[-1]

    def is_empty(self):
        if not self:
            return True
        else:
            return False

    def size(self):
            return len(self)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0


N = int(input())
s = Stack()
for i in range(N):
    text = input().split()
    if text[0] == "push":
        s.push(int(text[1]))
    elif text[0] == "top":
        print(s.top())
    elif text[0] == "size":
        print(s.size())
    elif text[0] == "empty":
        print(s.empty())
    elif text[0] == "pop":
        if s.empty() == 1:
            print("-1")
        else:
            print(s.pop())
