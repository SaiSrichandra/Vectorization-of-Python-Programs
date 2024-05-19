"""
Given an array A of integers, find the index of values that satisfy A + B = C + D, where A,B,C & D are integers values
in the array

Note:

1) Return the indices `A1 B1 C1 D1`, so that
  A[A1] + A[B1] = A[C1] + A[D1]
  A1 < B1, C1 < D1
  A1 < C1, B1 != D1, B1 != C1

2) If there are more than one solutions,
   then return the tuple of values which are lexicographical smallest.

Assume we have two solutions
S1 : A1 B1 C1 D1 ( these are values of indices int the array )
S2 : A2 B2 C2 D2

S1 is lexicographically smaller than S2 iff
  A1 < A2 OR
  A1 = A2 AND B1 < B2 OR
  A1 = A2 AND B1 = B2 AND C1 < C2 OR
  A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
Example:

Input: [3, 4, 7, 1, 2, 9, 8]
Output: [0, 2, 3, 5] (O index)
If no solution is possible, return an empty list.
"""


class Solution:

    def equal(self, arr):
        from collections import defaultdict
        sum_table = defaultdict(list)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if i not in sum_table[arr[i] + arr[j]] and j not in sum_table[arr[i] + arr[j]]:
                    sum_table[arr[i] + arr[j]] += [i, j]
        res = []
        print(sum_table)
        for k in sum_table.keys():
            if len(sum_table[k]) >= 4:
                pair = sum_table[k][:4]
                res.append(pair)
        res.sort()
        if not res:
            return []
        else:
            return res[0]


s = Solution()
ar = [1, 1, 1, 1, 1]
print(s.equal(ar))
