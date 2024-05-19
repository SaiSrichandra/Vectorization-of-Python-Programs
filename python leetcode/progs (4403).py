"""

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.

"""

"""my solution：两个字符串只有一个值不同，类似于之前的一道题，一个数组中所有数字都出现了两次，只有一个数出现了一次，对数组中所有的数进行一次异或操作即可"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        c = s+t
        res = 0
        for single_char in c:
            res = res ^ ord(single_char)
        return chr(res)

"""可以写的更精炼"""


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(reduce(operator.xor, map(ord, (s + t))))