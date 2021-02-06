# -*- coding:utf-8 -*-
class Solution(object):
    def maxScore(self, cardPoints, k):
        # cardPoints = [1, 2, 3, 4, 5, 6, 1]
        #       index = 0, 1, 2, 3, 4, 5, 6
        # k = 3
        card_len = len(cardPoints)  # 7
        win = card_len - k  # 4
        result = sum(cardPoints[:win])  # [1, 2, 3, 4]  10
        min_Sum = result  # 最小初始值
        for i in range(win, card_len):  # [4, 7]
            print(cardPoints[i])
            print(cardPoints[i - win])
            print(cardPoints[i] - cardPoints[i - win])
            print('end')
            result += cardPoints[i] - cardPoints[i - win]
            min_Sum = min(min_Sum, result)  # 比对谁小
        return sum(cardPoints) - min_Sum


if __name__ == '__main__':
    so = Solution()
    cardPoints = [1,2,3,4,5,6,1]
    k = 3
    print(so.maxScore(cardPoints, k))