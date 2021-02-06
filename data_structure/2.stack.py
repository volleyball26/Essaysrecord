# -*- coding:utf-8 -*-


class Stack:
    # 实现栈的push、pop、 取栈顶 类
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return None


# 实现括号匹配问题
# ({()})
def bracket_math(s):
    match = {']': '[', '}': '{', ')': '('}
    stack = Stack()
    for i in s:
        if i in {"[", "{", "("}:
            stack.push(i)
        else:
            if stack.is_empty():
                return False
            elif stack.get_top() == match[i]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False


if __name__ == '__main__':

    print(bracket_math('{}'))  # return True
    print(bracket_math('{)))}'))  # return False