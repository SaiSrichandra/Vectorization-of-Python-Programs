"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""

class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        N = len(s)
        if N == 0 or s[0] == '0':
            return 0
        dp = [0 for i in range(N+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, N+1):
            if s[i-1] == '0' and s[i-2] not in ['1', '2']:
                return 0
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2: i]) <= 26:
                dp[i] += dp[i-2]
        return dp[N]

    # Note:
    # 1. State: dp[i] means from char 0 to char i-1 how many decode ways
    # 2. Init: dp[0] = 1; dp[1] = 1
    # 3. Function:
    #      dp[i] = if s[i-1] == 0 and s[i-2] not in ['1', '2'] : return 0
    #              if s[i-1] != 0                              : += dp[i-1]
    #              if 10 <= int(s[i-2:i]) <= 26                : += dp[i-2]
    # 4. Result: dp[N]

    # i.   dp size is len(s)+1
    # ii.  10 <= x <= 26
    # iii. use if += instead of if dp = xx else dp = xx

    # Another idea
    def numDecodings_2(self, s):
        if s == '' or s[0] == '0': return 0
        dp = [1, 1]
        length = len(s)
        for i in xrange(2, length + 1):
            if 10 <= int(s[i-2:i]) <= 26 and '1' <= s[i-1] <= '9':
                dp.append(dp[i-1] + dp[i-2])
            elif 10 <= int(s[i-2:i]) <= 26: # s[i-1] == '0'
                dp.append(dp[i-2])
            elif '1' <= s[i-1] <= '9':
                dp.append(dp[i-1])
            else:  # s[i] == '0'
                return 0
        return dp[length]
