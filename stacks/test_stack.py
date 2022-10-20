"""
スタック(stack) : ラストインファーストアウト(LIFO)
先入れ後だし
古い   →     新しい
1, 2, 3, 4, 5, 6
pop()
6, 5, 4, 3, 2, 1
"""


class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last = len(self.items) - 1
        return self.items[last]
    
    def size(self):
        return len(self.items)

stack = Stack()

# 文字列を逆順にする。
# for c in "Hello":
#     stack.push(c)
# reverse = ""
# while stack.size():
#     reverse += stack.pop()
# print(reverse)

# print(stack.peek())
# print(stack.is_empty())