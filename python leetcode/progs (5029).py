'''
@auther: Jedi.L
@Date: Wed, Feb 20, 2019 11:44
@Email: xiangyangan@gmail.com
'''

import random

# class Solution:
#     def __init__(self, n_rows, n_cols):
#         """
#         :type n_rows: int
#         :type n_cols: int
#         """
#         self.cols = n_cols
#         self.end = n_rows * n_cols - 1
#         self.hash = {}
#         self.start = 0

#     def flip(self):
#         """
#         :rtype: List[int]
#         """
#         position = random.randint(self.start, self.end)
#         res = self.hash.get(position, position)
#         self.hash[position] = self.d.get(self.start, self.start)
#         self.start += 1
#         return divmod(res, self.cols)

#     def reset(self):
#         """
#         :rtype: void
#         """
#         self.hash = {}
#         self.start = 0


class Solution:
    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.cols = n_cols
        self.end = n_rows * n_cols - 1
        self.fliped = set()
        self.start = 0

    def flip(self):
        """
        :rtype: List[int]
        """
        while True:
            position = random.randint(self.start, self.end)
            if position not in self.fliped:
                self.fliped.add(position)
                return divmod(position, self.cols)

    def reset(self):
        """
        :rtype: void
        """
        self.fliped = set()



# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
