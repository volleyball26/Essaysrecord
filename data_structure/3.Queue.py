# -*- coding:utf-8 -*-

"""
    队列  数据集合, 仅允许在列表的一端进行插入，另一端进行删除
    FIFO   first in first out
    front 头  rear 尾

    ===环形队列===
    当队尾指针front == Maxsize + 1时，再前进一个位置就自动到0
    队首指针前进1 ： front = (front + 1) % Maxsize
    队尾指针前进1 ： rear = (rear + 1) % Maxsize
    队空条件： rear == front
    队满条件： (rear + 1) % Maxsize == front
"""


