# -*- coding:utf-8 -*-


class Stack:
    # 实现栈的push、pop、 取栈顶 类
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

    def get_top(self):
        if len(self.stack) > 0:
            self.stack.pop(-1)
        return None